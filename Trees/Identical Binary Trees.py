#https://www.interviewbit.com/problems/identical-binary-trees/

class Solution:
    # @param A : root node of tree
    # @param B : root node of tree
    # @return an integer
    
    def isSameTree(self, A, B):
        if(A is None or B is None):
            if(A is not None or B is not None):
                return 0
            else:
                return 1
        
        left_check=self.isSameTree(A.left,B.left)
        right_check=self.isSameTree(A.right,B.right)
        current_node_check=A.val==B.val
        if(current_node_check and left_check and right_check):
            return 1
        return 0