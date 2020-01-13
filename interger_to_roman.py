class Solution:
    def inttoroman(self, num: int) -> str:
        result = ""
        if num >= 1000 :
            countM = int(num/1000)
            num = num %1000
            result += "M"*countM
        
        if num >= 900:
            result += "CM"
            num -= 900
        
        if num >= 500:
            result += "D"
            num -= 500
        if num >= 400:
            result += "CD"
            num -= 400
        if num >= 100:
            countC = int(num/100)
            num = num%100
            result += "C"*countC
        if num >=90:
            result += "XC"
            num -= 90
        if num >= 50:
            result += "L"
            num -= 50
        if num >= 40:
            result += "XL"
            num -= 40
        if num >= 10:
            countX = int(num / 10)
            result += "X"*countX
            num = num % 10
        if num >= 9:
            result += "IX"
            num -= 9
        if num >= 5:
            result += "V"
            num -= 5
        if num >= 4:
            result += "IV"
            num -= 4
        if num >0:
            result += "I"*num
        return result

    def romanToInt(self, s: str) -> int:
        result:int = 0
        dit = {"M":1000, "CM":900, "D":500, "CD":400, "C":100, "XC":90, "L":50, "XL":40, "X":10, "IX":9, "V":5, "IV":4, "I":1}

        for key in dit:
            while (len(s) >= 1 and s[0] == key) or (len(s) >= 2 and s[0:2] == key):
                result += dit[key]
                s = s[len(key):]

        return result
if __name__ == "__main__":
    sol = Solution()
    print(sol.inttoroman(1994))

    print(sol.romanToInt(sol.inttoroman(1994)))

