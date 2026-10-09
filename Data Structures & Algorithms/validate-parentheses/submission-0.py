class Solution:
    def isValid(self, s: str) -> bool:
        hmap = {
            
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = []
        for i in s:
            if i == "(" or i == "{" or i == '[':
                stack.append(i)
            elif i in hmap and len(stack)>0 and hmap[i] == stack.pop():
                pass
            else:
                return False
        return len(stack) == 0
        
                
