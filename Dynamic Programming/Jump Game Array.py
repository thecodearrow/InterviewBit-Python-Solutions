#https://www.interviewbit.com/problems/jump-game-array/

class Solution:
    # @param A : list of integers
    # @return an integer
    def canJump(self, A):
        maxReach=0
        steps=1
        n=len(A)
        A=[0]+A
        for i in range(1,n+1):
            if(i==n):
                #reached final step
                return 1
            maxReach=max(A[i]+i,maxReach)
            steps-=1
            if(steps==0):
                steps=maxReach-i
                if(steps<=0):
                    return 0
                

    
