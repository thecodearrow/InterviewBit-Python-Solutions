#https://www.interviewbit.com/problems/longest-common-prefix/

class Solution:
    # @param A : list of strings
    # @return a strings
    def longestCommonPrefix(self, A):
        ans=""
        limit=len(min(A))
        for i in range(0,limit):
            current=A[0][i]
            for string in A:
                if(string[i]!=current):
                    return ans
            ans+=current
        
        return ans
            
        
