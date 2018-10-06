"""
#https://www.interviewbit.com/problems/longest-substring-without-repeat/

Given a string, 
find the length of the longest substring without repeating characters.

Example:

The longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3.

For "bbbbb" the longest substring is "b", with the length of 1.

"""
class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLongestSubstring(self, A):
        seen=set()
        start=0
        end=0
        ans=0
        while start<len(A) and end<len(A):
            c=A[end]
            if(c not in seen):
                seen.add(c)
                end+=1
                ans=max(ans,end-start)
            else:
                seen.remove(A[start])
                start+=1
        
        
        ans=max(ans,end-start)
        return ans
                
                
                
            
