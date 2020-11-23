class Solution:
    def searchRange(self, nums: [int], target: int) -> [int]:

        def search(nums, left, right, target):
            if left > right:
                return [-1, -1]

            if left == right:
                if nums[left] == target:
                    return left
                else:
                    return [-1, -1]

            middleIdx = (left + right) // 2
            if nums[middleIdx] == target:
                startIdx = endIdx = middleIdx
                for i in range(startIdx -1, left -1 , -1):
                    if nums[i] == target:
                        startIdx = i
                    else:
                        break
                
                for i in range(endIdx + 1, right + 1):
                    if nums[i] == target:
                        endIdx = i
                    else:
                        break
            
                return [startIdx, endIdx]

            elif nums[middleIdx] > target:
                return search(nums, left, middleIdx - 1, target)
            else:
                return search(nums, middleIdx + 1, right, target)