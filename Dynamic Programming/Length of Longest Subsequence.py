#Longest Bitonic Subsequence 
#Length of Longest Subsequence

#https://www.interviewbit.com/problems/length-of-longest-subsequence/

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def longestSubsequenceLength(self, A):
        n=len(A)
        increasing=[1]*n # LIS till i
        decreasing=[1]*n # LDS starting from i
    
        for i in range(1,n):
            for j in range(i):
                if(A[j]<A[i]):
                    increasing[i]=max(increasing[i],increasing[j]+1)
        
        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                if(A[j]<A[i]):
                    decreasing[i]=max(decreasing[i],decreasing[j]+1)
        
        ans=0
        
        for i in range(n):
            ans=max(increasing[i]+decreasing[i]-1,ans)
        
        return ans 
                
        
        
