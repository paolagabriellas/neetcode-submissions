class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        for i, val in enumerate(nums):
            if target - val in nums:
                for j in range(i, len(nums)):
                    if nums[j] == target - val and i != j:
                        return [i, j]