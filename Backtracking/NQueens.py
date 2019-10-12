#https://www.interviewbit.com/problems/nqueens/

class Solution:
    # @param A : integer
    # @return a list of list of strings
    def isSafe(self,row,col,n,board):
        #Checking column for a Queen
        #Row is already taken care of since we are only placing one Queen in one row
        for r in range(n):
            if(board[r][col]=="Q"):
                return False
                
        #Check for upper left diagonal
        i=row
        j=col
        while i>=0 and j>=0:
            if(board[i][j]=='Q'):
                return False
            i-=1
            j-=1
        
        
        #Check for upper right diagonal
        i=row
        j=col
        while i>=0 and j<n:
            if(board[i][j]=='Q'):
                return False
            i-=1
            j+=1
            
        return True
    
    def convertToString(self,board):
        new_board=[]
        for row in board:
            s=""
            for r in row:
                s+=r
            new_board.append(s)
        return new_board
    def solveNQueens(self, A):
        board=[["." for i in range(A)]for j in range(A)]
        def solve(board,row,n,ans):
            if(row==n):
                ans.append(self.convertToString(board))
                return ans
            for c in range(n):
                if(self.isSafe(row,c,n,board)):
                    board[row][c]='Q'
                    solve(board,row+1,n,ans)
                    board[row][c]='.'
            
            return ans
            
        ans=[]
        ans=solve(board,0,A,ans)
        return ans

