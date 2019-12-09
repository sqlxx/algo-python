class Solution:
    def generateParenthesis(self, n: int) -> [str]:
        if n == 0:
            return [""]
        result = []
        
        for i in range(n):
            print(n, ", ", n-i -1)
            for left in self.generateParenthesis(i):
                for right in self.generateParenthesis(n - i - 1):
                    result.append('({}){}'.format(left, right))

        return result

    def generateParenthesis2(self, n: int) -> [str]:
        result = []
        def backtrack(s:str, left:int, right:int):
            if len(s) == 2*n:
                result.append(s)
            else:
                if left < n:
                    backtrack(s + "(", left + 1, right)
                
                if left > right:
                    backtrack(s + ")", left, right + 1)
        
        backtrack("", 0, 0)
    
        return result

if __name__ == "__main__":
    sol = Solution()
    print(sol.generateParenthesis2(3))
    print(sol.generateParenthesis(3))