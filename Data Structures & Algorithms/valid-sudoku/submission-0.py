from collections import defaultdict
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # checking row wise
        i = 0
        while i<9:  
            validation=defaultdict(int)         
            for j in range(len(board[0])):
                if((board[i][j]).isnumeric()):
                    validation[int(board[i][j])]+=1
            if any(x>1 for x in validation.values()):
                return False
            print(validation,"adding 1")
            i+=1

        # check column 
        j = 0
        while j<9:  
            validation=defaultdict(int)         
            for i in range(len(board[0])):
                if((board[i][j]).isnumeric()):
                    validation[int(board[i][j])]+=1
            if any(x>1 for x in validation.values()):
                return False
            print(validation,"adding 2")
            j+=1

        for box_row in range(0, 9, 3):        # 0, 3, 6
            for box_col in range(0, 9, 3):    # 0, 3, 6
                validation = defaultdict(int)
                for i in range(3):
                    for j in range(3):
                        cell = board[box_row + i][box_col + j]
                        if cell.isnumeric():
                            validation[int(cell)] += 1
                if any(x > 1 for x in validation.values()):
                    return False
        
        return True

                

        
        
            