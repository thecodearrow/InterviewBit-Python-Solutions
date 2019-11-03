#https://www.youtube.com/watch?v=GnliEfQo114

#https://www.youtube.com/watch?v=13m9ZCB8gjw

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution1:
    # @param A : root node of tree
    # @param B : integer
    # @param C : integer
    # @return an integer
    def contains(self,root,val):
        if(root is None):
            return False
        if(root.val==val):
            return True
        return self.contains(root.left,val) or self.contains(root.right,val)
    
    def findLCA(self,A,B,C):
        if(A is None):
            return None
        if(A.val==B or A.val==C):
            return A.val
        left_return=self.findLCA(A.left,B,C)
        right_return=self.findLCA(A.right,B,C)
        if(left_return and right_return):
            return A.val
        if(left_return):
            return left_return
        if(right_return):
            return right_return
        return None
    def lca(self, A, B, C):
        if(not self.contains(A,B) or not self.contains(A,C)):
            return -1
        lca=self.findLCA(A,B,C)
        if(lca):
            return lca
        return -1


class Solution2:
    # @param A : root node of tree
    # @param B : integer
    # @param C : integer
    # @return an integer
    
    
    
    def findNode(self,start,value):
        if(start==None):
            return None
        if(start.val==value):
            return [value]
        leftPath=self.findNode(start.left,value)
        if(leftPath!=None):
            leftPath.append(start.val)
            return leftPath
        rightPath=self.findNode(start.right,value)
        if(rightPath!=None):
            rightPath.append(start.val)
            return rightPath
        return None
        
    def lca(self, root, val1, val2):
        path1=self.findNode(root,val1)
        path2=self.findNode(root,val2)
        print(path1,path2)
        if(not path1 or not path2):
            return -1
        limit=len(path1)
        if(len(path2)<limit):
            limit=len(path2)
        ans=root.val
        for i in range(limit):
            if(path1[i]!=path2[i]):
                return ans
            ans=path1[i]
            
        return ans
        
