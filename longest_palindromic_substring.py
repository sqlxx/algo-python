class Solution:
    def isPalindrome(self, s: str) -> bool:
        length = len(s)
        return s[0:int(length/2)] == s[:-int(length/2)-1:-1]
        
    
    def longestPalindrome(self, s: str) -> str:
        length = len(s)

        if length < 2:
            return s
        

        for removeCharCount in range(0, length):
            for startIndex in range(0, removeCharCount + 1):
                strToJudge = s[startIndex:length - removeCharCount + startIndex]
                if self.isPalindrome(strToJudge):
                    return strToJudge


    