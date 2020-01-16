class Solution:
    def jump2(self, nums: [int]) -> int:
        memo = [0] * len(nums)

        def dp(nums, index) -> int:
            if index == len(nums) -1:
                return 0

            if memo[index] != 0:
                return memo[index]
            
            allowed_steps = nums[index]
            if allowed_steps + index >= len(nums) -1:
                memo[index] = 1
                return memo[index]

            min_steps = 9999999
            for i in range(1, allowed_steps + 1):
                # print(i, ", ", index)
                if i + index <= len(nums) -1:
                    steps = dp(nums, i + index)
                    min_steps = min(steps, min_steps)
                    if min_steps == 1:
                        break
            
            memo[index] = min_steps + 1
            #print("<---", memo[index])
            return memo[index]

        return dp(nums, 0)
    
    def jump1(self, nums: [int]) -> int:
        memo = [0] * (len(nums))
    
        def minimal(startIndex, endIndex):
            if startIndex == endIndex:
                return memo[startIndex]

            return min(memo[startIndex: endIndex + 1])

        for i in range(len(nums) - 2 , -1, -1, ):
            allowed_steps = nums[i]
            if allowed_steps + i >= len(nums) -1:
                memo[i] = 1
                continue

            memo[i] = minimal(i + 1, i + allowed_steps) + 1
            
        return memo[0]

    def jump(self, nums: [int]) -> int:
        
        if len(nums) ==1:
            return 0
        
        jumps = 0
        i = 0
        while True:
            if i >= len(nums) -1:
                return jumps + 1
            allowed_steps = nums[i]
            if i + allowed_steps >= len(nums) -1:
                return jumps + 1

            max = 0
            furthest_index = 0
            for j in range(i + 1, i + allowed_steps + 1):
                if nums[j] + j > max:
                    max = nums[j] + j 
                    furthest_index = j
            
            i = furthest_index 
            jumps += 1
        
        return jumps
            

if __name__ == "__main__":
    sol = Solution()
    print(sol.jump([2,3,1,1,4]))
    print(sol.jump([1,2,0,1]))
    print(sol.jump([1,1,1,1]))
