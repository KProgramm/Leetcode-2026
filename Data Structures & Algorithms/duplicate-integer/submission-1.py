class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        checkDuplicate = set(nums)
        if(len(nums)>len(checkDuplicate)):
            return True
        return False
        