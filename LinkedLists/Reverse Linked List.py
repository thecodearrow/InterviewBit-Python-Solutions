#https://www.interviewbit.com/problems/reverse-linked-list/

class Solution:
    
    def reverseList(self, A):
        current=A
        prev=None
        next=None
        while current!=None:
            next=current.next
            current.next=prev
            prev=current
            current=next
        
        return prev
            
        
        
