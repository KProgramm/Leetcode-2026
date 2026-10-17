class Solution:
    def isPalindrome(self, s: str) -> bool:
        #left and right pointers
        #while left pointer < right pointer
        # if s[left].isalnum()

        ss = ""
        for i in s:
            if i.isalnum():
                ss += i
        #this string will have a, A, 1

        left = 0
        right = len(ss) - 1

        while left<=right:
            if ss[left].lower() == ss[right].lower():
                left +=1
                right -=1
            else:
                return False
        return True
        
            
