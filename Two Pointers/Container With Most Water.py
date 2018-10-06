#https://www.interviewbit.com/problems/container-with-most-water/

class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArea(self, A):
        start=0
        end=len(A)-1
        current=0
        ans=0
        while start<=end:
            current=(end-start)*min(A[start],A[end])
            ans=max(current,ans)
            if(A[start]>=A[end]):
                end-=1
            else:
                start+=1
            
            
            
        return ans
