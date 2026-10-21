from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = Counter(nums)
        ordered = sorted(count, key=count.get, reverse=True)

        final = []
        for i in range(k):
            final.append(ordered[i])
        return final




        