#https://www.interviewbit.com/problems/path-sum/

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def hasPathSum(self, A, B,currentSum=0):
        currentSum+=A.val
        if(A.left is None and A.right is None):
            #Check for a left node
            if(currentSum==B):
                return 1
            return 0
        left_sum=None
        right_sum=None
        if(A.left):
            left_sum=self.hasPathSum(A.left,B,currentSum)
        if(A.right):
            right_sum=self.hasPathSum(A.right,B,currentSum)
        if(left_sum or right_sum):
            return 1
        return 0
