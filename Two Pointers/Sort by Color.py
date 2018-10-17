"""

https://www.interviewbit.com/problems/sort-by-color/


Swap the 0s to the start of the array maintaining a pointer,
and 2s to the end of the array. 1s will automatically be in their right position. 

"""
from collections import defaultdict
class Solution:

    def sortColors(self, A):
        #two pointer approacH!
        start=0
        end=len(A)-1
        idx=0
        while idx<=end:
            if(A[idx]==0):
                A[start],A[idx]=A[idx],A[start]
                start+=1
                idx+=1
            elif(A[idx]==2):
                A[end],A[idx]=A[idx],A[end]
                end-=1
            else:
                idx+=1
                
            
        
        return A
            
        
        
        
        
