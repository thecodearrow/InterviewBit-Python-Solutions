#https://www.interviewbit.com/problems/min-jumps-array/

#O(N) solution!  (NOT DP)

#https://www.youtube.com/watch?v=vBdo7wtwlXs Excellent tutorial !

"""

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

"""
class Solution:
    # @param A : list of integers
    # @return an integer
    def jump(self, A):
        n=len(A)
        if(n<=1):
            return 0
        if(A[0]==0):
            return -1
        ladder=A[0]
        stairs=A[0]
        jumps=1
        for i in range(1,n):
            if(i==n-1):
                return jumps
            ladder=max(A[i]+i,ladder)
            stairs-=1
            if(stairs==0):
                jumps+=1
                if(i>=ladder):
                    return -1
                stairs=ladder-i
        
        
        
