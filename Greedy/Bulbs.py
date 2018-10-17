
"""
https://www.interviewbit.com/problems/bulbs/

N light bulbs are connected by a wire. Each bulb has a switch associated with it, 
however due to faulty wiring, a switch also changes the state of all the bulbs to the 
right of current bulb. Given an initial state of all bulbs, find the minimum number of 
switches you have to press to turn on all the bulbs. You can press the same switch 
multiple times.


"""
class Solution:
  
    def bulbs(self, A):
        current=0
        count=0
        for b in A:
            bulb=b-current
            if(bulb==0):
                current=1-current
                count+=1
                
        return count
