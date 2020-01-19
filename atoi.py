class Solution:
    def myAtoi(self, str: str) -> int:
        if str == None or len(str) == 0 or str == '-' or str == '+':
            return 0
        s = self.trimSpace(str)
        negative = False
        if s[0] == '-':
            negative = True
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]
        
        if not s[0].isdigit():
            return 0
        
        value = 0
        for i in range(0, len(s)):
            if s[i].isdigit():
                value = value*10 + int(s[i])
            else:
                break

        if negative:
            value = - value 

        intMax = (1 << 31) - 1
        intMin = -intMax -1
        print(intMax)
        print(intMin)
        if value > intMax:
            return intMax
        elif value < intMin:
            return intMin
        else:
            return value


    def trimSpace(self, s: str) -> str:
        for i in range(0, len(s)):
            if (s[i] != ' '):
                break
        
        return s[i:]
    

            

if __name__ == "__main__":
    sol = Solution()
    print("42 = {}".format(sol.myAtoi("42")))
    print("-41 = {}".format(sol.myAtoi("-41")))
    print("4193 = {}".format(sol.myAtoi("4193 with words")))
    print("0 = {}".format(sol.myAtoi("words and 987")))
    print("-2147483648 = {}".format(sol.myAtoi("-91283472332")))
    print("2147483647 = {}".format(sol.myAtoi("2147483648")))
    print("0 = {}".format(sol.myAtoi(None)))




