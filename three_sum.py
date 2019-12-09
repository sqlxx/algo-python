class Solution:
    def threeSum(self, nums: [int]) -> [[int]]:
        nums.sort()
        result = []
        print(nums)
        for i in range(len(nums) -2):
            if nums[i] > 0:
                break;

            l = i + 1
            r = len(nums) - 1
            
            if i > 0 and nums[i] == nums[i-1]:
                continue

            while l < r:
                sum = nums[l] + nums[r] + nums[i]

                if sum > 0:
                    r = r - 1
                elif sum < 0:
                    l = l + 1
                else:
                    result.append([nums[i], nums[l], nums[r]])
                    l = l + 1
                    while l < r and nums[l] == nums[l-1]:
                        l = l + 1
            

        return result

if __name__ == "__main__":
    sol = Solution()
    print(sol.threeSum([0, 0, 0]))