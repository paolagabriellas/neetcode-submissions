class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}

        for num in nums:
            if num in freqs:
                freqs[num] += 1
            else:
                freqs[num] = 1
        
        top = dict(sorted(freqs.items(), key=lambda item: item[1], reverse=True))
        return list(top.keys())[:k]
