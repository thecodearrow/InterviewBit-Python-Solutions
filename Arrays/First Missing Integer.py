#https://www.interviewbit.com/problems/first-missing-integer/

#Given an unsorted integer array, find the first missing positive integer.

#our algorithm should run in O(n) time and use constant space.

#Solution without using a hash map

class Solution:
 
    def firstMissingPositive(self, A):

        if(max(A)<1):
            return 1
        
        new_A=[0]*(len(A)+1)

        for ele in A:
            if(ele>=1 and ele<=len(A)):
                new_A[ele-1]=10**9+7 #checked PRESENT!


        for i in range(len(new_A)):
            if(new_A[i]!=(10**9+7)):
                return(i+1)



#Solution using a hashmap



class Solution:
 
    def firstMissingPositive(self, A):
        seen={}
        if(max(A)<1):
            return 1
        for ele in A:
            seen[ele]=True

        for i in range(1,len(A)+2): 
            if(i not in seen):
                return i 





                


        


       
       