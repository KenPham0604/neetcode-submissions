class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        p1, p2 = 0,0
        res = 0
        while p2 < len(s):
            if s[p2] not in set(s[p1:p2]):
                res = max(res, p2 - p1 + 1)
                p2 += 1
            else:
                
                p1 += 1
        return res
