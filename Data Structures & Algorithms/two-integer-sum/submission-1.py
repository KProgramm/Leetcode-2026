class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        #key - value: number - index

        #psuedo:
        #calc complement (target-current)
        #if complement in seen, return complement index, then current index
        #else, add current to seen

        for i in range(len(nums)):
            complement = target-nums[i]
            if complement in seen:
                return [seen[complement], i]
            else:
                seen[nums[i]] = i
