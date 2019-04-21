#https://www.interviewbit.com/problems/invert-the-binary-tree/

class Solution:
    # @param A : root node of tree
    # @return the root node in the tree
    def invertTree(self, A):
        if(A==None):
            return
        self.invertTree(A.left)
        self.invertTree(A.right)
        A.left,A.right=A.right,A.left
        return A
