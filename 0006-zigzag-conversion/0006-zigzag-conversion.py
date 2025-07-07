import math
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
            
        rows = numRows
        cols = int(math.ceil(len(s))) 
        array_2d = [[None for _ in range(cols)] for _ in range(rows)]

        row, col = 0, 0
        down = True

        for ch in s:
            array_2d[row][col] = ch
            if down:
                if row == numRows - 1:
                    down = False
                    row -= 1
                    col += 1
                else:
                    row += 1
            else:
                if row == 0:
                    down = True
                    row += 1
                else:
                    row -= 1
                    col += 1

        output = ""
        for i in range(len(array_2d)):
            for j in range(len(array_2d[0])):
                if array_2d[i][j] != None:
                    output += array_2d[i][j]
        return output