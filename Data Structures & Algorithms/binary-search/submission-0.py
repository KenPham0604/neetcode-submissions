class Solution:
    
        
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            midd = (left + right) // 2
            
            if nums[midd] == target:
                return midd
            elif target < nums[midd]:
                right = midd - 1
            else:
                left = midd + 1
        return -1
