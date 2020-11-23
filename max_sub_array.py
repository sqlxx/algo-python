class Solution:
    def maxSubArray(self, nums: [int]) -> int:
        current_sum = nums[0]
        current_max = nums[0]
        for num in nums[1:]:
            # print(num, ',', current_sum)
            if current_sum >= 0:
                current_max = max(current_sum, current_max)
                current_sum += num
                current_max = max(current_sum, current_max)
            else:
                if num < 0:
                    current_max = max(current_sum, current_max, num)
                    current_sum = max(current_sum, num)
                else:
                    current_sum = num
                    current_max = max(current_max, num)
        
        return current_max
