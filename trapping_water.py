class Solution:
    def trap(self, height: [int]) -> int:
        if len(height) <= 1:
            return 0
        
        result = 0

        left = 0
        right = len(height) - 1

        maxLeft = height[left]
        maxRight = height[right]
        while left < right:
            if height[left] < height[right]:
                if height[left] > maxLeft:
                     maxLeft = height[left]
                else:
                    result +=  maxLeft - height[left]
                left += 1
            else:
                if height[right] > maxRight:
                    maxRight = height[right]
                else:
                    result += maxRight - height[right]
                right -= 1
        
        return result

    def trap2(self, height:[int]) -> int:
        if len(height) <= 1:
            return 0 

        maxLeft = {0: height[0]}
        maxRight ={len(height)-1: height[-1]}
        for i in range(1, len(height)):
            maxLeft[i] = max(maxLeft[i-1], height[i])
        
        for j in range(len(height) - 2 , 0, -1):
            maxRight[j] = max(maxRight[j + 1], height[j])
        

        res = 0
        for i in range(1, len(height) - 1):
            res += min(maxLeft[i], maxRight[i]) - height[i]

        return res