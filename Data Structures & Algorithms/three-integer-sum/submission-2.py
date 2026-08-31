class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums  = sorted(nums)

        for i in range(0, len(nums) - 1):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if i != left and i != right:
                    total = nums[left] + nums[right] + nums[i]
                    if  total == 0:
                        triplet = [nums[i], nums[left], nums[right]]
                        if triplet not in triplets:
                            triplets.append(triplet)
                        left = left + 1
                        right = right - 1
                    elif total > 0:
                        right = right - 1
                    else:
                        left = left + 1
                
        
        return triplets
