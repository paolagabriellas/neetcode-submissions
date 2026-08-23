class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictNums = {}
        for i, num in enumerate(nums):
            if num in dictNums:
                dictNums[num].append(i)
            else:
                dictNums[num] = [i]
        
        for num in nums:
            diff = target - num
            if diff in dictNums and diff != num:
                return dictNums[num] + dictNums[diff]
            elif diff == num and len(dictNums[num]) > 1:
                return dictNums[num]
