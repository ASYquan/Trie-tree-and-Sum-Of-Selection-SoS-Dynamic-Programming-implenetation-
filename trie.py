import numpy as np

class TrieNode:
    def __init__(self):
        self.children = {}
        self.nodeEnd= False
        

class Trie:
    def __init__(self) -> None:
        """
        Initialize the Trie data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the Trie.

        Parameters:
            word (str): The word to insert. Assume the word is lowercase.

        Returns:
            None
        """
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]
        current_node.nodeEnd = True
             
    def look_up(self, word: str) -> bool:
        """
        Checks if a word has been inserted into the Trie.

        Parameters:
            word (str): The word to look up. Assume it's always lowercase.

        Returns:
            bool: True if the word is found, False otherwise. If 'high' is inserted and the function receives 'hight', it should return False. Only inserted words should return True.
        """
        current = self.root
        for letter in word:
            current = current.children.get(letter)
            if current is None:
                return False
        return current.nodeEnd
    
    
    def collect_common_prefix(self, node: TrieNode) -> tuple[str, TrieNode]:
        """
        Help-method for TrieString which collects the longest common prefix from the current node.
        
        Parameters:
            node (TrieNode): The starting node to collect the prefix from.
        
        Returns:
            str, TrieNode: The longest common prefix and the node where the prefix ends.
        """
        prefix = ""
        while len(node.children) == 1 and not node.nodeEnd:
            char, node = next(iter(node.children.items()))
            prefix += char
        return prefix, node

    
    def TrieString(self, node : TrieNode = None, prefix : str = "") -> str:
        """
        Help method for print_tree which produces a string representation of the Trie with a given prefix from a starting node.

        Parameters:
            node (TrieNode): The starting node for the string representation.
            prefix (str): The prefix to prepend to current node's string representation.
        
        Returns:
            str: The string representation of the Trie from the given node.
        """
        if node is None:
            node = self.root
        
        prefix, node = self.collect_common_prefix(node)
        result = prefix

        if node.nodeEnd:
            result += ""
        sorted_children = sorted(node.children.items())  # Sort children by key (character)

        if node.children:
            result += "("
            for i, (char, child_node) in enumerate(sorted_children):
                if i > 0:
                    result += ")("
                result += char + self.TrieString(child_node)
            result += ")"

        return result
    
    def print_tree(self) -> str:
        """
        Prints the Trie in alphabetical order.

        Example:
            internet: (internet)
            interview: (inter(net)(view))
            inter: (inter(net)(view))

        Returns:
            str: A string that shows the state of the Trie.
        """
        return f"({self.TrieString()})"

        
        
    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        current = self.root 
        
        for letter in prefix:
            current = current.children.get(letter)
            if not current:
                return False
        
        return True
    
    
if __name__ == "__main__":
    trie = Trie()
    trie.insert("algorithm")
    trie.insert("all")
    trie.insert("internally")
    trie.insert("internet")
    trie.insert("interview")
    trie.insert("web")
    trie.insert("world")
    
    #print(trie.startsWith("view")) #Returns False 
    #print("Look up 'internally':", trie.look_up("internally"))  # should return True
    #print("Look up 'internet':", trie.look_up("internet"))      # should return True
    #print("Look up 'intra':", trie.look_up("intra"))            # should return False

    print("\nTrie contents:")
    #print(trie.longest_common_prefix())
    print(trie.print_tree())
    #rint(trie.longest_common_prefix(trie.print_tree()))