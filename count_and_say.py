class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        
        prevResult = self.countAndSay(n-1)
        count = 0
        current = ''
        result = ''
        for i in prevResult:
            if count == 0:
                current = i
                count += 1
            elif current == i:
                count += 1
            else:
                result += (str(count) + current)
                current = i
                count = 1

        result += (str(count) + current)

        return result

if __name__ == '__main__':
    sol = Solution()
    print(sol.countAndSay(1))
    print(sol.countAndSay(2))
    print(sol.countAndSay(4))