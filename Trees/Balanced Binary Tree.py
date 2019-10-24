#https://www.interviewbit.com/problems/balanced-binary-tree/

class Solution:
    # @param A : root node of tree
    # @return an integer
    def checkBalanced(self,A):
        if(A==None):
            return 0
        if(A.left==None and A.right==None):
            return 1
        leftDepth=self.checkBalanced(A.left)
        if(leftDepth==float("inf")):
            #If left subtree is not balanced, there's no point going right
            return float("inf")
        rightDepth=self.checkBalanced(A.right)
        diff=abs(leftDepth-rightDepth)
        if(diff>=2):
            maxDepth=float("inf")
        else:
            maxDepth=max(leftDepth,rightDepth)+1
        return maxDepth
    def isBalanced(self, A):
        maxDepth=self.checkBalanced(A)
        if(maxDepth==float("inf")):
            return 0
        return 1
