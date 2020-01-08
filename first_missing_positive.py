class Solution:
    def firstMissingPositive(self, nums: [int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] < 0 or nums[i] > n:
                nums[i] = 0
                
        for i in range(n):
            
            if nums[i] == 0:
                continue
            elif nums[i] <= n:
                if nums[i] - 1 == i:
                    continue
                if nums[nums[i] - 1] > n: # already added
                    nums[i] = 0
                    continue
                nums[nums[i]-1] = nums[nums[i]-1] + nums[i] -1 + n
                nums[i] = 0
            else: # nums[i] > n
                actual_value = nums[i] - i - n
                if actual_value != 0:
                    if nums[actual_value-1] > n:
                        nums[i] = i + 1 
                        continue
                    nums[actual_value-1] = nums[actual_value -1] + actual_value - 1 + n
                nums[i] = i + 1

            
        for i in range(n):
            if nums[i] == 0:
                return i + 1
        
        return n + 1
