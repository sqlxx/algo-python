class Solution:
    def longestValidParentheses2(self, s: str) -> int:
        ''' brute force'''

        length = 0
        stack = 0
        nextpoint = 0
        rightpareCount = 0

        for i in range(len(s)):
            if s[i] == '(':
                stack += 1
            if s[i] == ')':
                if stack > 0:
                    stack -= 1
                    # print("In right parenthese ", stack)
                    rightpareCount += 1
                    if stack == 0:
                        length += (2*rightpareCount)
                        rightpareCount = 0
                    # print("length is ", length)
                else:
                    nextpoint = i
                    break
        
        length2 = 0
        for j in range(nextpoint + 1, len(s)):
            if s[j] == '(':
                length2 = self.longestValidParentheses(s[j:])
                break
        # print(length, ",", length2)
        return max(length, length2)

    def longestValidParentheses(self, s: str) -> int:
        ''' dynamic programming '''
        dp = []
        for i in range(len(s)):
            dp.append(0)
        length = 0
        for i in range(1, len(s)):
            if s[i] == ')' and s[i-1] == '(':
                if i > 2:
                    dp[i] = dp[i-2] + 2
                else:
                    dp[i] = 2
            
            if s[i] == ')' and s[i-1] == ')':
                if i - dp[i-1] -1 >=0 and s[i - dp[i-1] -1] == '(' and dp[i-1] != 0:
                    dp[i] = dp[i-1] + 2 + dp[i - dp[i-1] -2]
            
            if dp[i] > length:
                length = dp[i]
            # print(dp)
        
        return length
    
        


if __name__ == '__main__':
    sol = Solution()
    print(sol.longestValidParentheses("(()))())("))
    # print(sol.longestValidParentheses("))(())"))
    # print(sol.longestValidParentheses("()(())"))
    # print(sol.longestValidParentheses("()(()"))
    # print(sol.longestValidParentheses("(()"))
    # print(sol.longestValidParentheses(")()()))"))

