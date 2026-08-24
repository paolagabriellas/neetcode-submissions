class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = [1] * len(nums)
        prev = 1
        for i, num in enumerate(nums):
            product[i] = product[i] * prev
            prev = prev * nums[i]
        suf = 1
        for i in range(len(nums) -1, -1, -1):
            product[i] = product[i] * suf
            suf = suf * nums[i]

        return product