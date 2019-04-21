#https://www.interviewbit.com/problems/identical-binary-trees/

class Solution:
    # @param A : root node of tree
    # @param B : root node of tree
    # @return an integer
    def isSameTree(self, A, B):
        if(A is None and B is None):
            return 1
        if(A is None or B is None):
            
            return A.val==B==val and 
        return 0
