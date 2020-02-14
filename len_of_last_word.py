class Solution:
    def lengthOfLastWord2(self, s: str) -> int:
        result = 0
        hasSpace = False
        for c in s:
            if c != ' ':
                if hasSpace:
                    result = 1
                    hasSpace = False
                else:
                    result += 1
            else:
                hasSpace = True
        
        return result
    
    def lengthOfLastWord(self, s: str) -> int:
        result = 0
        for i in range(len(s), -1, -1):
            if s[i] == ' ':
                if result > 0:
                    return result
                else:
                    continue
            else:
                result += 1
        
        return result