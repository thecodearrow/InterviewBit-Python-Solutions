"""

https://www.interviewbit.com/problems/intersection-of-linked-lists/

Write a program to find the node at which the intersection of two singly linked lists begins.

https://www.youtube.com/watch?v=gE0GopCq378&feature=player_embedded


"""



class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    
    def length(self,l):
        length=0
        while l!=None:
            length+=1
            l=l.next
        return length
    def getIntersectionNode(self, A, B):
        m=self.length(A)
        n=self.length(B)
        d=n-m
        if(m>n):
            #swap A,B
            A,B=B,A
            d=m-n
        
        #cover d steps
        for i in range(d):
            B=B.next 
            
        
        while A!=None and B!=None:
            if(A==B):
                return A
            A=A.next
            B=B.next
        
        return None
            
            
            
            
        
        
        
        
            
