class Solution:
    def generate(self, numRows: int) -> [[int]]:
        result = []

        def generateRow(rowNum):
            row = [1]
            itemCount = rowNum + 1
            if itemCount == 1:
                return row
            else:
                for i in range(1, itemCount-1):
                    row.append(result[rowNum-1][i-1] + result[rowNum-1][i])
            
            row.append(1)
            return row

        for i in range(numRows):
            result.append(generateRow(i))
            
        return result
    

if __name__ == '__main__':
    sol = Solution()
    print(sol.generate(10))