from typing import List, Optional

# Macro variables for table values
NONE = 0
FALSE = 1
TRUE = 2


class TopDownSos:
    def __init__(self, sequence: List[int]) -> None:
        """
        Initializes the TopDownSos class and fills the first column and row of the table.

        Parameters:
            sequence (List[int]): An array of positive integers.
        """
        self.sequence = sequence
        total_sum = sum(self.sequence)
        
        self.n = len(sequence)
        self.memo = [[None] * (sum(sequence) + 1) for _ in range(self.n + 1)]  # Memoization table to store results
        for i in range(self.n + 1):
            self.memo[i][0] = True  # Sum of 0 is always achievable with an empty subset

    def _is_subset_sum_possible(self, i: int, k: int) -> bool:
        """
        Help-method to be used in check_sum with the purpose as a 
        recursive function to determine if a subset sum equal to k is possible.

        Parameters:
            i (int): Index of the current element in the sequence.
            k (int): Target sum to check for subsets.

        Returns:
            bool: True if a subset sum of k is possible, False otherwise.
        """
        if k < 0:
            return False
        if i == 0:
            return k == 0

        if self.memo[i][k] is not None:
            return self.memo[i][k]

        include_current = self._is_subset_sum_possible(i - 1, k - self.sequence[i - 1])
        exclude_current = self._is_subset_sum_possible(i - 1, k)

        self.memo[i][k] = include_current or exclude_current
        return self.memo[i][k]

    def check_sum(self, k: int) -> Optional[List[int]]:
        """
        Calls a recursive function that fills in the necessary parts of the table.

        Parameters:
            k (int): The target sum.

        Returns:
            Optional[List[int]]: Returns a list of integers that make up the subsequence that can achieve the target sum k. Returns None if it can't be made.
        """
        if not self._is_subset_sum_possible(self.n, k):
            return None

        subset = []
        i, current_sum = self.n, k

        while i > 0 and current_sum > 0:
            if self.memo[i][current_sum] and not self.memo[i-1][current_sum]:
                subset.append(self.sequence[i-1])
                current_sum -= self.sequence[i-1]
            i -= 1

        return subset[::-1]  # Reverse to return in the original order

