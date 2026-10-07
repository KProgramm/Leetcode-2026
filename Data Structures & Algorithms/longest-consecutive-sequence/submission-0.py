class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numy = set(nums)
        for i in numy:
            if i-1 in numy:
                pass
            else:
                current = 1
                index = 1
                while i +index in numy:
                    current +=1
                    index +=1
                longest = max(longest, current)
        return longest