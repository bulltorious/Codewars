# https://www.codewars.com/kata/529bf0e9bdf7657179000008
def valid_solution(board):
    #print(board)
    start = {1,2,3,4,5,6,7,8,9}
    
    # verify all rows
    for row_ctr in range(0,9):
        start = {1,2,3,4,5,6,7,8,9}
        for element in board[row_ctr]:
            #print(element)
            if element in start:
                start.remove(element)
            else:
                return False
    

    # verify all columns
    
    for col_ctr in range(0,9):
        start = {1,2,3,4,5,6,7,8,9}
        for row_ctr in range(0,9):
            element = board[row_ctr][col_ctr]
            if element in start:
                start.remove(element)
            else:
                return False            
            
        
    
    # verify all 3x3 blocks
    r_start = 0
    c_start = 0

    while(r_start < 9):
        while(c_start < 9):
            start = {1,2,3,4,5,6,7,8,9}
            for c in range(c_start, c_start+3):
                for r in range(r_start, r_start+3):
                    element = board[r][c]
                    if element in start:
                        start.remove(element)
                    else:
                        return False
            c_start+=3
        r_start+=3
        
    return True

print(valid_solution([
  [5, 3, 4, 6, 7, 8, 9, 1, 2],
  [6, 7, 2, 1, 9, 5, 3, 4, 8],
  [1, 9, 8, 3, 4, 2, 5, 6, 7],
  [8, 5, 9, 7, 6, 1, 4, 2, 3],
  [4, 2, 6, 8, 5, 3, 7, 9, 1],
  [7, 1, 3, 9, 2, 4, 8, 5, 6],
  [9, 6, 1, 5, 3, 7, 2, 8, 4],
  [2, 8, 7, 4, 1, 9, 6, 3, 5],
  [3, 4, 5, 2, 8, 6, 1, 7, 9]
])) #should be True