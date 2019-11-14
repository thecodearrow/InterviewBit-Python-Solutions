
#https://www.interviewbit.com/problems/noble-integer/

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        found=False
        A=sorted(A)
        rem_count=len(A)-1
        for i,p in enumerate(A):
            if(i<len(A)-1):
                if(A[i]!=A[i+1]):
                    if(p==rem_count):
                        found=True
                        break
                    
            else:
                if(p==rem_count):
                    found=True
            rem_count-=1
            
        if(found):
            return 1
        return -1
            
                
