"""
Given a read only array of n + 1 integers between 1 and n, find one number that repeats in linear time using less than O(n) space and traversing the stream sequentially O(1) times.


"""



#https://www.youtube.com/watch?v=lf2w3C82jYA
#https://www.interviewbit.com/problems/find-duplicate-in-array/


class Solution:
    def repeatedNumber(self, A):
        #Involves cheeky encoding
        A=list(A)
        for ele in A:
            number=ele
            if(ele<0):
                number=-ele #has been flipped already!
            if(A[number]<0):
                #has already been flipped
                #Duplicate present
                return number
            else:
                A[number]=-1*A[number] #Flip it to mark that the number has been seen
        
        return -1