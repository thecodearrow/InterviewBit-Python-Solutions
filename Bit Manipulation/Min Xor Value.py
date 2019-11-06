#https://www.interviewbit.com/problems/min-xor-value/

class Solution:
    # @param A : list of integers
    # @return an integer
    def findMinXor(self, A):
        A=sorted(A)
        min_xor=float("inf")
        for i in range(1,len(A)):
            current_xor=A[i]^A[i-1]
            if(current_xor<min_xor):
                min_xor=current_xor
                
        return min_xor
