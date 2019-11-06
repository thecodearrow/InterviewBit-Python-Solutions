#https://www.interviewbit.com/problems/number-of-1-bits/

class Solution:
    def numSetBits(self, A):
        ans=0
        while A:
            ans+=1
            A-=(A&(-A))
            #A=(A&(A-1))
        return ans
