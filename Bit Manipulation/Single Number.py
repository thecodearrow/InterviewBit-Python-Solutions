#https://www.interviewbit.com/problems/single-number/

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        xor_value=0
        for ele in A:
            xor_value^=ele
        return xor_value
            
        
        
