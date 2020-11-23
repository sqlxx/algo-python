class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            possibles = self.threeSum(nums[i + 1:], target - nums[i])
            for possible in possibles:
                result.append(possible.insert(0, nums[i]))
            
        return result
        
    
    def threeSum(self, nums: [int], target:int) -> [[int]]:
        result = []
        for i in range(len(nums) -2):
            if nums[i] > target:
                break;

            l = i + 1
            r = len(nums) - 1
            
            if i > 0 and nums[i] == nums[i-1]:
                continue

            while l < r:
                sum = nums[l] + nums[r] + nums[i]

                if sum > target:
                    r = r - 1
                elif sum < target:
                    l = l + 1
                else:
                    result.append([nums[i], nums[l], nums[r]])
                    l = l + 1
                    while l < r and nums[l] == nums[l-1]:
                        l = l + 1
            

        return result

