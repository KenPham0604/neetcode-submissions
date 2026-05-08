class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
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
        '''
        l,r = 0, len(nums) - 1
        
        while l < r:
            mid = (l+r)//2 
            if nums[mid] < nums[r]:
                r = mid 
            else:
                l = mid + 1
        return nums[l]
        
        