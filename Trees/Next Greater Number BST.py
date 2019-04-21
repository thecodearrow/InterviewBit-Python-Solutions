#https://www.youtube.com/watch?v=5cPbNCrdotA&feature=player_embedded


class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return the root node in the tree
    
    def findCurrentNode(self,root,ele):
        current=root
        while current.val!=ele:
            if(ele<current.val):
                current=current.left
            else:
                current=current.right
                
        return current
        
    def getSuccessor(self, A, B):
        currentNode=self.findCurrentNode(A,B)
        ans=None
        if(currentNode.right!=None): #if it has a right sub tree
            temp=currentNode.right
            while temp.left!=None:
                temp=temp.left
            return temp
        else:  
            parent=A
            successor=None
            while parent.val!=currentNode.val:
                if(currentNode.val<parent.val):
                    successor=parent
                    parent=parent.left
                else:
                    parent=parent.right
            return successor
                    
                
            
            
            
                
            
        
        
        
                
            
                
                
                
        
