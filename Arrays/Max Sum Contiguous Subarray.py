"""
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

"""

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        #Kadane's Algo
        current_sum=A[0]
        max_sum=A[0]
        for i in range(1,len(A)):
            current_sum=max(current_sum,current_sum+A[i])
            if(current_sum>=0):
                current_sum+=ele
            max_sum=max(max_sum,current_sum)
        
        return max_sum
        
