#Given an array A of integers and another non negative integer k, find if there exists 2 indices i and j such that A[i] - A[j] = k, i != j.

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, A, B):
        check={}
        j=0
        for ele in A:
            check[ele]=j
            j+=1
            
        i=-1    
        for ele in A:
            i+=1
            diff=ele-B
            if(diff in check):
                j=check[diff]
                if(i!=j):
                
                    return 1
        return 0