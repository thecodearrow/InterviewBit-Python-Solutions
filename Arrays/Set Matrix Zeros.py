#https://www.interviewbit.com/problems/set-matrix-zeros/
class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def setZeroes(self, A):
        n=len(A)
        m=len(A[0])
        first_row_nullify=False
        first_col_nullify=False
        for i in range(n):
            for j in range(m):
                if(A[i][j]==0):
                    if(i==0):
                        first_row_nullify=True
                    if(j==0):
                        first_col_nullify=True
                    
                    A[i][0]=0
                    A[0][j]=0
                    
        
        for i in range(1,n):
            for j in range(1,m):
                if(A[i][0]==0 or A[0][j]==0):
                    A[i][j]=0
                    
        if(first_row_nullify):
            for j in range(m):
                A[0][j]=0
                
        if(first_col_nullify):
            for i in range(n):
                A[i][0]=0
                
        
                    
 
        return A
