#https://www.interviewbit.com/problems/longest-increasing-subsequence/

class Solution:

    def lis(self, A):
        n=len(A)
        length=[1]*n
        for i in range(1,n):
            for j in range(i):
                if(A[j]<A[i]):
                    length[i]=max(length[i],length[j]+1)
                    
        
        return max(length)
            
        