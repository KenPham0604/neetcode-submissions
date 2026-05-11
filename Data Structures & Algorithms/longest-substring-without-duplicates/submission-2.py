class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        p1, p2 = 0,0
        res = 0
        check = [False]*200
        while p2 < len(s):
            if not check[ord(s[p2])]:
                check[ord(s[p2])] = True
                res = max(res, p2-p1+1)
                p2 += 1
            else: 
                check[ord(s[p1])] = False
                p1 += 1
        return res
