class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        precalcs = [1] * len(nums)

        for i in range(1, len(nums)):
            precalcs[i] = precalcs[i] * precalcs[i-1] * nums[i-1]
        
        mult = 1
        for i in range(len(nums) - 2, -1, -1):
            mult = nums[i+1] * mult
            precalcs[i] = precalcs[i] * mult

        return(precalcs)