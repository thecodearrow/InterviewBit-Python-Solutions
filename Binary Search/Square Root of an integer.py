#https://www.interviewbit.com/problems/square-root-of-integer/
class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        if(A==0 or A==1):
            return A
        n=A
        low=1
        high=n
        while low<=high:
            mid=(low+high)//2
            if(mid*mid==n):
                return mid
            elif(mid*mid<n):
                low=mid+1
            else:
                high=mid-1
                
        return high #or low-1

