#https://www.interviewbit.com/problems/assign-mice-to-holes/
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def mice(self, A, B):
        ans=0
        positions=sorted(A)
        holes=sorted(B)
        for i in range(len(A)):
            currentDist=abs(positions[i]-holes[i])
            ans=max(ans,currentDist)
                
        return ans
