class Solution:
    def myPow2(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        result = x
        pow = abs(n)
        for _ in range(pow):
            result *= x

        
        if n < 0:
            result = 1/result
        
        return result
    

    def myPow(self, x: float, n: int) -> float:
        memo = {}

        def dp(x, n):

            if n == 1:
                return x

            key = str(x) + "," + str(n)
            if key in memo:
                result = memo[key]
            else:
                if n % 2 == 0:
                    result = dp(x, n/2) * dp(x, n/2)
                else:
                    result = x*dp(x, n//2)* dp(x, n//2)    

                memo[key] = result

            return result
        

        if n == 0:
            return 1

        if n < 0:
            return 1/dp(x, abs(n))
        else:
            return dp(x, n)
            
