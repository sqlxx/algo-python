class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return ""
        keyMap = {"2":["a", "b", "c"], "3":["d", "e", "f"], "4":["g", "h", "i"], "5":["j", "k", "l"], "6":["m", "n", "o"], "7":["p", "q", "r", "s"], "8":["t","u","v"], "9":["w", "x", "y", "z"]}
        if len(digits) >= 2:
            return self.combine(keyMap[digits[0]], self.letterCombinations(digits[1:]))
        else :
            return keyMap[digits[0]]


    def combine(self, chs:[str], strs:[str]):
        result = []
        for v in chs:
            for i in range(len(strs)):
                result.append (v + strs[i])
        
        return result