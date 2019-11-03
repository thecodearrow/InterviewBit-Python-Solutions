#https://www.interviewbit.com/problems/kth-smallest-element-in-tree/

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def inorder(self,root,k):
        count=0
        stack=[root]
        visited={}
        #Iterative Inorder Traversal
        while stack:
            currentNode=stack[-1]
            if(currentNode.val not in visited):
                visited[currentNode.val]=0
            if(visited[currentNode.val]==0):
                if(currentNode.left):
                    stack.append(currentNode.left)
            elif(visited[currentNode.val]==1):
                count+=1
                if(count==k):
                    return currentNode.val
            elif(visited[currentNode.val]==2):
                if(currentNode.right):
                    stack.append(currentNode.right)
            
            else:
                stack.pop()
            visited[currentNode.val]+=1
        
    def kthsmallest(self, A, B):
        return self.inorder(A,B)

        
