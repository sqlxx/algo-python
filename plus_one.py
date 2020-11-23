class Solution:
    def plusOne(self, digits: [int]) -> [int]:
        length = len(digits)
        toAdd = 1
        for i in range(length-1, -1, -1):

                
            digits[i] += 1
            if digits[i] > 9:
                toAdd = 1
                digits[i] = digits[i] - 10
            else:
                toAdd = 0
                break
        
        if toAdd > 0:
            return [toAdd] + digits
            
        return digits