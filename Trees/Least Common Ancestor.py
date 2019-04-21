#https://www.youtube.com/watch?v=GnliEfQo114

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
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
        
