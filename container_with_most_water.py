class Solution:
    def maxArea2(self, height: [int]) -> int:
        currentMax = 0
        num = len(height)
        for i in range(0, num - 1):
            for j in range(i+1, num):
                if height[j] > height[i]:
                    continue 
                else:
                    area = (j-i) * min(height[i], height[j]) 
                    currentMax = max(area, currentMax)
        
        return currentMax

    def maxArea(self, height: [int]) -> int:
        leftIndex = 0
        rightIndex = len(height) -1
        currentMax = 0
        while rightIndex - leftIndex > 0:
            leftHeight = height[leftIndex]
            rightHeight = height[rightIndex]
            if rightHeight > leftHeight:
                currentMax =  max(currentMax, (rightIndex-leftIndex)*leftHeight)
                leftIndex += 1
            else:
                currentMax = max(currentMax, (rightIndex - leftIndex)*rightHeight)
                rightIndex -= 1


        return currentMax

if __name__ == '__main__':
    sol = Solution()
    print(sol.maxArea([1,8,6,2,5,4,8,3,7]))
    