from typing import List, Optional


class BottomUpSos:
    def __init__(self, sequence: List[int]) -> None:
        """
        Initializes the BottomUpSos class and calculates the table.

        Parameters:
            sequence (List[int]): An array of positive integers.
        """
        self.sequence = sequence
        self.n = len(sequence)
        # Create the table with (n+1) rows and (K+1) columns
        self.table = None

    def _initialize_table(self, K: int) -> None:
        """
        Initialize the DP table with base case values.

        Parameters:
            K (int): The target sum to check for subsets.
        """
        self.table = [[False] * (K + 1) for _ in range(self.n + 1)]
        for i in range(self.n + 1):
            self.table[i][0] = True  # Sum of 0 is always achievable with an empty subset

    def is_subset_sum_possible(self, K: int) -> bool:
        """
        Help method for check_sum which
        determines if a subset sum equal to K is possible.

        Parameters:
            K (int): The target sum to check for subsets.

        Returns:
            bool: True if a subset sum of K is possible, False otherwise.
        """
        self._initialize_table(K)
        
        for i in range(1, self.n + 1):
            for j in range(1, K + 1):
                if self.sequence[i - 1] <= j:
                    # Include or exclude the current element
                    self.table[i][j] = self.table[i - 1][j] or self.table[i - 1][j - self.sequence[i - 1]]
                else:
                    # Exclude the current element
                    self.table[i][j] = self.table[i - 1][j]

        return self.table[self.n][K]
    
    
    
    def check_sum(self, k: int) -> Optional[List[int]]:
        """
        Checks if a subsequence exists that sums up to the target sum k.

        Parameters:
            k (int): The target sum.

        Returns:
            Optional[List[int]]: Returns a list of integers that make up the subsequence that can achieve the target sum k. Returns None if it can't be made.
        """

        
        if not self.is_subset_sum_possible(k):
            return None

        subset = []
        i, j = self.n, k

        while i > 0 and j > 0:
            if self.table[i][j] and not self.table[i-1][j]:
                subset.append(self.sequence[i-1])
                j -= self.sequence[i-1]
            i -= 1
    
        return subset[::-1]
    
    
if __name__ == "__main__":
    
    arr = [ 3, 34, 4, 12, 5, 2 ]
    
    K = 9
    obj = BottomUpSos(arr)
    print(obj.check_sum(K))

    # Print the table
