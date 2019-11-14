#https://www.interviewbit.com/problems/rain-water-trapped/
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def trap(self, A):
        left_max=[A[i] for i in range(len(A))]
        right_max=[A[i] for i in range(len(A))]
        for i in range(1,len(A)):
            left_max[i]=max(left_max[i-1],A[i])
            
        for i in range(len(A)-2,-1,-1):
            right_max[i]=max(right_max[i+1],A[i])
        ans=0
        for i in range(len(A)):
            water_height=min(left_max[i],right_max[i])
            ans+=(water_height-A[i])
            
        return ans
