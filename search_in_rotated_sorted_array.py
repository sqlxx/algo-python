class Solution:
    def search(self, nums: [int], target: int) -> int:
            def bsearch(nums, left, right, target) -> int:
                if left > right:
                    return -1
                if left == right:
                    if nums[left] == target:
                        return left
                    else:
                        return -1
                elif right - left == 1:
                    if nums[left] == target:
                        return left
                    elif nums[right] == target:
                        return right
                    else:
                        return -1 
                else:
                    middleIdx = int((left + right)/2)
                    if nums[middleIdx] == target:
                        return middleIdx
                    else:
                        rotateLeft = False
                        if nums[right] > nums[middleIdx]:
                            rotateLeft = True

                        if nums[middleIdx] < target:
                            if rotateLeft:
                                if nums[right] >= target:
                                    return bsearch(nums, middleIdx + 1, right, target)
                                else:
                                    return bsearch(nums, left, middleIdx - 1, target)
                            else:
                                return bsearch(nums, middleIdx + 1, right, target)
                                

                        if nums[middleIdx] > target:
                            if rotateLeft:
                                return bsearch(nums, left, middleIdx -1, target)
                            else:
                                if nums[left] <= target:
                                    return bsearch(nums, left, middleIdx -1, target)
                                else:
                                    return bsearch(nums, middleIdx + 1, right, target)


            return bsearch(nums, 0, len(nums) -1, target)   

if __name__ == '__main__':
    sol = Solution()
    print(sol.search([4,5,6,7,0,1,2], 0)) # 4
    print(sol.search([4,5,6,7,0,1,2], 3)) # -1
    print(sol.search([4,5,6,7,8,1,2,3], 3)) # -1


