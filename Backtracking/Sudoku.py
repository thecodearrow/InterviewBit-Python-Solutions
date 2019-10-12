#https://www.interviewbit.com/problems/sudoku/

class Solution:
    # @param A : list of list of chars
    # @return nothing
    
    def isValid(self,sudoku,row,col,value):
        #Check if value is present in col
        for i in range(9):
            if(sudoku[i][col]==value):
                return False
        #Check if value is present in row
        for i in range(9):
            if(sudoku[row][i]==value):
                return False
           
        #Check if value is present in box
        x=(row//3)*3
        y=(col//3)*3
        for i in range(x,x+3):
            for j in range(y,y+3):
                if(sudoku[i][j]==value):
                    return False
        return True
        
        
    def solveSudoku(self, A):
        def sudokuSolver(row,col):
            if(row==9):
                #Reached the end
                return True
            if(col==9):
                return sudokuSolver(row+1,0)
            if(row<=8 and col<=8):  
                if(A[row][col]=="."):
                    for number in range(1,10):
                        if(self.isValid(A,row,col,str(number))):
                            A[row][col]=str(number)
                            if(sudokuSolver(row,col+1)):
                                return True
                            A[row][col]="."
                    return False
                else:
                    return sudokuSolver(row,col+1)
                            
                            
                    
        sudokuSolver(0,0)
                            
        
