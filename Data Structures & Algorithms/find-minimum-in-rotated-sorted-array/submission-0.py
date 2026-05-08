class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return nums[0]
        res = 0 
        
        mid = (len(nums))//2
        min_left = self.findMin(nums[:mid])
        min_right = self.findMin(nums[mid:]) 
        
        if min_left < min_right:
            return min_left
        else:
            return min_right
        
        