class Solution:
    def reverseBits(self, n: int) -> int:
        next = n 
        result = 0
        i = 32
        while next > 0:
            reminder = next % 2
            print (next, reminder)
            result = (result * 2) | reminder
            next = next // 2
            i -= 1
        result = result << i


        return result