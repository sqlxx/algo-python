class Solution:
    def nextPermutation2(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        highestIdx = -1 
        lowestIdx = len(nums)
        for i in range(len(nums) - 1, 0, -1):
            for j in range(i -1, -1, -1):
                if nums[i] > nums[j]:
         #           print("switch ", i, ":", j)
                    if highestIdx < j:
                        highestIdx = j
                        lowestIdx = i
        # print("final switch:", highestIdx, ":", lowestIdx)
        if lowestIdx != len(nums):
            nums[highestIdx], nums[lowestIdx] = nums[lowestIdx], nums[highestIdx]

        startIdx = highestIdx + 1
        
        for i in range(startIdx, len(nums) - 1):
            minIdx = i
            for j in range(i + 1, len(nums)):
                  if nums[minIdx] > nums[j] :
                    minIdx = j
            if minIdx != i:
                nums[minIdx], nums[i] = nums[i], nums[minIdx]
                  
    def nextPermutation(self, nums: [int]) -> None:
        reverseStart = 0
        for i in range(len(nums) -1, 0, -1):
            if nums[i-1] < nums[i]:
                reverseStart = i
                
                for j in range(i, len(nums)):
                    if nums[i-1] >= nums[j]:
                        break
                    
                if nums[j] > nums[i-1]:
                    j += 1
                nums[i-1], nums[j-1] = nums[j-1], nums[i-1]
                break

        reverseEnd = len(nums) -1

        while reverseStart < reverseEnd:

            nums[reverseStart], nums[reverseEnd] = nums[reverseEnd], nums[reverseStart]
            reverseStart += 1
            reverseEnd -= 1

