class Solution:
    def getRow(self, rowIndex: int) -> [int]:
        row = [0 for i in range(rowIndex + 1)]
        row[0] = 1

        def getRowInternal(rowIndex):
            row[rowIndex] = 1
            
            for i in range(rowIndex-1, 0, -1):
                row[i] = row[i] + row[i-1]

        for i in range(1, rowIndex + 1):
            getRowInternal(i)

        return row

if __name__ == '__main__':
    sol = Solution()
    print(sol.getRow(3))