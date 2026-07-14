class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        current = 0
        for i in range(len(nums)):
            mult = 1
            for j in range(len(nums)):
                if j!= current:
                    mult *= nums[j]
            out.append(mult)
            current+=1
        return out
        
