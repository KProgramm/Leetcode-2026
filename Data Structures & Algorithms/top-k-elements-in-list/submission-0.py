class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for i in nums:
            count[i] += 1
        
        pairs = list(count.items())
        pairs.sort(key=lambda p: p[1], reverse=True)

        result = []
        for i in range(k):
            result.append(pairs[i][0])
        return result


        