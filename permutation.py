class Solution:
    def permute(self, nums: [int]) -> [[int]]:
        if len(nums) == 0:
            return [[]]

        if len(nums) == 1:
            return [[nums[0]]]
        result = []
        for num in nums:
            copy_nums = nums.copy()
            copy_nums.remove(num)
            res = self.permute(copy_nums)
            for ele in res:
                ele.insert(0, num)
                result.append(ele)

        
        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.permute([1, 2, 3]))
