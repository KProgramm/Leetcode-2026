class Solution:
    def isValid(self, s: str) -> bool:
        
        #for true:
        #1. ALL open brackets are closed
        #2. openings closed in the right order
        #3. 
        stack = []
        paren = {
            "(": ")",
            "{": "}",
            "[": "]"
        }

        for char in s:
            if char in paren: #an opener
                stack.append(char)
            else: #closer
                if not stack:
                    return False
                if paren[stack.pop()] != char:
                    return False
        return not stack


                
