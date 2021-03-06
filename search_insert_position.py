class Solution:
    def searchInsert(self, nums: [int], target: int) -> int:

        if len(nums) == 1:
            if target > nums[0]:
                return 1
            else:
                return 0

        for i in range(1, len(nums)):
            if target > nums[i-1] and target <= nums[i]:
                return i
        

        return len(nums)