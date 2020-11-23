class Solution:
    def removeElement(self, nums: [int], val: int) -> int:
        if len(nums) == 0: 
            return 0
        lastPoint = len(nums) -1
        while nums[lastPoint] == val and lastPoint >= 0:
                lastPoint -= 1
        
        if lastPoint < 0:
            return 0
            
        for i in range(len(nums)):

            if (nums[i] == val):
                nums[i]= nums[lastPoint]
                nums[lastPoint] = val
                while nums[lastPoint] == val and lastPoint >= 0:
                    lastPoint -= 1

            if i >= lastPoint:
                break

        
        return lastPoint + 1

    def removeElement2(self, nums: [int], val: int) -> int:
        lastPoint = len(nums)
        i = 0
        while i < lastPoint:
            if nums[i] == val:
                nums[i] = nums[lastPoint-1]
                lastPoint -= 1
            else:
                i += 1
        
        return lastPoint



if __name__ == '__main__':
    sol = Solution()
    print(sol.removeElement2([2, 2, 3], 2))