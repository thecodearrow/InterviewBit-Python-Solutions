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




#Is Safe can be optimised to O(1)

class Solution:
    # @param A : integer
    # @return a list of list of strings
    def solveNQueens(self, n):
        board=[["." for i in range(n)]for j in range(n)]
        result=[]
        def isSafe(i,j,rows,cols,diag1,diag2):
            if(i not in rows):
                if(j not in cols):
                    if((i+j) not in diag1):
                        if((i-j) not in diag2):
                            return True
            return False
        def markPosition(i,j,rows,cols,diag1,diag2,board):
            board[i][j]='Q'
            rows.add(i)
            cols.add(j)
            diag1.add(i+j)
            diag2.add((i-j))
            return rows,cols,diag1,diag2,board
        
        def unMarkPosition(i,j,rows,cols,diag1,diag2,board):
            board[i][j]='.'
            rows.remove(i)
            cols.remove(j)
            diag1.remove(i+j)
            diag2.remove((i-j))
            return rows,cols,diag1,diag2,board
            
        def NQueens(i,board,rows,cols,diag1,diag2):
            if(i==n):
                #print(board)
                solved_board=[]
                for row in board:
                    rowString="".join(row)
                    solved_board.append(rowString)
                result.append(solved_board)
                return
            r=i
            for c in range(n):
                if(isSafe(r,c,rows,cols,diag1,diag2)):
                    rows,cols,diag1,diag2,board=markPosition(r,c,rows,cols,diag1,diag2,board)
                    NQueens(i+1,board,rows,cols,diag1,diag2)
                    rows,cols,diag1,diag2,board=unMarkPosition(r,c,rows,cols,diag1,diag2,board)
                
            
        
        
        NQueens(0,board,set(),set(),set(),set())
        return result
