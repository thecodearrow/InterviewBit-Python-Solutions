#https://www.interviewbit.com/problems/inorder-traversal/

#Without Recursion

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def getParent(self,node):
        parent={}
        queue=[node]
        parent[node]=None
        while queue:
            u=queue.pop(0)
            if(u.left):
                queue.append(u.left)
                parent[u.left]=u
                
            if(u.right):
                queue.append(u.right)
                parent[u.right]=u
        return parent
    def inorderTraversal(self, A):
        parent=self.getParent(A)
        currentNode=A
        prevNode=None
        ans=[]
        while currentNode!=None:
            if(prevNode is None or prevNode==parent[currentNode]):
                #Keep exploring left if you can
                if(currentNode.left):
                    nextNode=currentNode.left
                else:
                    ans.append(currentNode.val)
                    if(currentNode.right):
                        nextNode=currentNode.right
                    else:
                        nextNode=parent[currentNode]
            elif(prevNode==currentNode.left):
                ans.append(currentNode.val)
                if(currentNode.right):
                    nextNode=currentNode.right
                else:
                    nextNode=parent[currentNode]
            else:
                nextNode=parent[currentNode]
                
            prevNode=currentNode
            currentNode=nextNode
        return ans
                
                
                    
                
        
        
