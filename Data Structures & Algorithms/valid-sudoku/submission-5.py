from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # need to check for row, column and otherwise
        row = defaultdict(int)

        def validsubgrid(start_num,col):
            xxx = defaultdict(int)
            for i in range(start_num,start_num+3):
                for j in range(col,col+3):
                    if (board[i][j] in xxx and board[i][j].isnumeric()):
                        return False
                    else:
                        xxx[board[i][j]]=1
            return True

        ## ehcking for rows
        for i in range(len(board)):
            row = defaultdict(int)
            for j in range(len(board[0])):
                if (board[i][j] in row and board[i][j].isnumeric()):
                    return False
                else:
                    row[board[i][j]]=1

        # checking for columns
        for j in range(len(board[0])):
            column = defaultdict(int)
            for i in range(len(board)):
                if (board[i][j] in column and board[i][j].isnumeric()):
                    print("column fail")
                    return False
                else:
                    column[board[i][j]]=1

        for r in [0,3,6]:
            for c in [0,3,6]:
                answer = validsubgrid(r,c)
                if (not answer):
                    return False
        return True    

        


                
        