class Solution:
    def isValid(self, s: str) -> bool:
        map = {']':'[',')':'(','}':'{'} 
        stack = []
        for i in range(len(s)):
            if s[i] in map and stack and map[s[i]] == stack[-1]:
                stack.pop()
            else:
                stack.append(s[i])
        return len(stack) == 0