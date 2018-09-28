"""

Given an array of integers, sort the array into a wave like array and return it, 
In other words, arrange the elements into a sequence such that a1 >= a2 <= a3 >= a4 <= a5.....
"""
class Solution:

    def wave(self, A):
        A=sorted(A)
        #Sort array and swap adjacent elements. Voila! Wave form :D
        for i in range(0,len(A)-1,2):
            A[i],A[i+1]=A[i+1],A[i]
        
        return A
            
