#https://www.interviewbit.com/problems/list-cycle/

class Solution:
    # @param A : head node of linked list
    # @return the first node in the cycle in the linked list
    def detectCycle(self, A):
        if(A==None):
            return None
        turtle=A
        hare=A
        cycleFound=False
        while hare and hare.next:
            turtle=turtle.next
            hare=hare.next.next
            if(turtle==hare):
                cycleFound=True
                break
            
        turtle=A
        if(not cycleFound):
            return None
            
        
        while turtle!=hare:
            hare=hare.next
            turtle=turtle.next
        
        return turtle
        
            
        
        
