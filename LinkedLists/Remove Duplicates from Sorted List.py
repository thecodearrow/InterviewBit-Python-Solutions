#https://www.interviewbit.com/problems/remove-duplicates-from-sorted-list/

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, A):
        headNode=A
        currentNode=A
        while currentNode.next:
            if(currentNode.val==currentNode.next.val):
                currentNode.next=currentNode.next.next
            else:
                currentNode=currentNode.next
        return headNode
            
