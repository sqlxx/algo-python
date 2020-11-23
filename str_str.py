class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        
        firstIndex = -1
        for i in range(len(haystack)):
            if len(haystack) - i < len(needle):
                break
                
            if haystack[i] == needle[0]:
                matched = True
                for j in range(1, len(needle)):
                    if haystack[i + j] == needle[j]:
                        continue
                    else:
                        matched = False
                        continue
        
                if matched == True:
                    firstIndex = i
                    break
        return firstIndex