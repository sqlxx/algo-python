class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            result = int(str(x)[::-1])
        else:
            result = int("-" + str(-x)[::-1])
        limit = 1 << 31
        if result > limit -1 or result < -limit:
            return 0
        return result
        

if __name__ == "__main__":
    s = Solution()
    print(s.reverse(123456789))
    print(s.reverse(123))
    print (1 << 31)
