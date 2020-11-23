class Solution:
    def addBinary(self, a: str, b: str) -> str:
        s = ''
        lena = len(a)
        lenb = len(b)
        limit = max(lena, lenb) + 2
        
        toAdd = 0
        for i in range(-1, -limit, -1):
            va = int(a[i]) if lena >= -i else 0
            vb = int(b[i]) if lenb >= -i else 0
            sumValue = va + vb + toAdd
            if sumValue == 3:
                s = '1' + s
                toAdd = 1
            elif sumValue == 2:
                s = '0' + s
                toAdd = 1
            elif sumValue == 1:
                s = '1' + s
                toAdd = 0
            elif sumValue == 0 and i != -limit+1:
                s = '0' + s
                toAdd = 0
            
        return s
        
        