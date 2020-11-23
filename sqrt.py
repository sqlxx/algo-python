class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        prev = 1
        for i in range(1, x+1):
            squre = i * i
            if squre == x:
                return i
            elif squre < x:
                prev = i
            else:
                return prev
    

    def mySqrt2(self, x: int) -> int:
        if x == 0:
            return 0

        l, r = 1, 1
        maximum, minimum = 1, x + 1
        
        while maximum < minimum -1 :
            print(l, r, maximum, minimum)
            if r * r == x:
                return r
            elif r * r < x:
                maximum = r
                l = r
                r = min(2*r, (minimum + l) // 2)
            else:
                minimum = r
                r = (l + r) // 2
                
        return maximum