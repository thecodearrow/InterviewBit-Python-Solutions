#https://www.interviewbit.com/problems/rotate-matrix/

#Alternate Solution based on observation

#If you take the transpose of the original matrix and then swap the 
#first column with the last, second with last second, and so on,
#you get the 90 degrees rotated matrix.

class Solution:
    def getNewPosition(self,i,j,n):
        return n-j-1,i
        
    def rotateUsingTranspose(self,A):
        n=len(A)
        #Take Transpose of Matrx
        for i in range(n):
            for j in range(i+1,n):
                A[i][j],A[j][i]=A[j][i],A[i][j]
                
        limit=n//2
        
        #Start swapping columns now
        for i in range(n):
            for j in range(limit):
                A[i][j],A[i][n-j-1]=A[i][n-j-1],A[i][j]
        
        return A
                
                
    def rotate(self, A):
        n=len(A)
        limit_rows=n//2
        limit_cols=n//2
        if(n%2!=0):
            limit_cols+=1
        for i in range(limit_rows):
            for j in range(limit_cols):
                current_i,current_j=i,j
                next_i,next_j=self.getNewPosition(i,j,n)
                starting_value=A[i][j]
                while (next_i,next_j)!=(i,j):
                    A[current_i][current_j]=A[next_i][next_j]
                    current_i,current_j=next_i,next_j
                    next_i,next_j=self.getNewPosition(current_i,current_j,n)
                    
                A[current_i][current_j]=starting_value
        return A
                    
                
                    
