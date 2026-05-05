class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for n in matrix:
            left, right = 0, len(n) - 1
            while left <= right:
                mid = (left + right) // 2

                if target == n[mid]:
                    return True
                elif target < n[mid]:
                    right = mid - 1
                elif target > n[mid]:
                    left = mid + 1
        return False
