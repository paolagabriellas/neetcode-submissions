class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seqs = []
        length = 1
        longest = 0
        nums = {value: index for index, value in enumerate(nums)}

        for num in nums:
            if (num - 1) not in nums:
                length = 1
                val = 1
                while (num + val) in nums:
                    length += 1
                    val += 1
                if length > longest:
                    longest = length
        return longest
