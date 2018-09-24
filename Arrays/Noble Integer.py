"""
Given an integer array, find if an integer p exists in the array such that the number of integers greater than p in the array equals to p
If such an integer is found return 1 else return -1.

"""

from collections import defaultdict
class Solution:
  
    def solve(self, A):
        found=False
        A=sorted(A)[::-1]
        count=0
        freq=defaultdict(lambda:0)
        new_A=[]
        for i in range(len(A)):
            if(freq[A[i]]==0):
                new_A.append(A[i])
            freq[A[i]]+=1
            
            
        for i in range(len(new_A)):
            p=new_A[i]
            count+=freq[p]
            if(count-freq[p]==p):
                found=True
                
                    
        
        if(found):
            return 1
        else:
            return -1
