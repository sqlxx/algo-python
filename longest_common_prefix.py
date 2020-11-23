class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        
        index:int = 0
        temp = ""
        match:bool = True
        while match:
            for i in range(len(strs)):
                if index == len(strs[i]):
                    match = False
                    break
                    
                if i == 0:
                    temp = strs[0][index]
                else:
                    if strs[i][index] != temp:
                        match = False
                        break

            index += 1
        
        if index == 0:
            return ""
        
        return strs[0][:index-1]