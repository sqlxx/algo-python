class Solution:
    def permuteUnique(self, nums: [int]) -> [[int]]:
        def permute(nums: [int]) -> [[int]]:

            if len(nums) == 0:
                return [[]]

            if len(nums) == 1:
                return [[nums[0]]]
            result = []
            prev_num = -1
            for num in nums:
                if num == prev_num:
                    continue
                copy_nums = nums.copy()
                copy_nums.remove(num)
                res = permute(copy_nums)
                for ele in res:
                    ele.insert(0, num)
                    result.append(ele)

                prev_num = num
        
            return result
    
        nums.sort()
        return permute(nums)

if __name__ == "__main__":
    sol = Solution()
    print(sol.permuteUnique([1, 1, 3]))
