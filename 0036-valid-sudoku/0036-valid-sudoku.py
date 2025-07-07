class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        invalid = False

        for i in range(0, len(board), 3):
            for j in range(0, len(board[0]), 3):
                subgrid = [row[j:j+3] for row in board[i:i+3]]
                if self.three_by_three_duplicate_check(subgrid):
                    return False
        
        
        for j in range(0, len(board[0])):
            seen = []
            for i in range(0, len(board)):
                val = board[i][j]
                if val == ".":
                    continue

                if val not in seen:
                    seen.append(val)
                else:
                    print(val)
                    print("returning here2")
                    return False
        
        for i in range(0, len(board)):
            seen = []
            for j in range(0, len(board[0])):
                val = board[i][j]
                if val == ".":
                    continue
                    
                if val not in seen:
                    seen.append(val)
                else:
                    print("returning here2323")
                    return False
        
        return True
    
    def three_by_three_duplicate_check(self, threeDArray):
        
        seen = []
        
        for i in range(len(threeDArray)):
            for j in range(len(threeDArray[0])):
                val = threeDArray[i][j]
                if val == ".":
                    continue
                if val not in seen:
                    seen.append(val)
                else:
                    return True

        print(threeDArray)        
        return False
