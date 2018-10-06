
"""
#https://www.interviewbit.com/problems/length-of-last-word/

Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

"""
class Solution:
   
    def lengthOfLastWord(self, A):
        l=0
        A=A[::-1]
        index=-1
        for c in A:
            index+=1
            if(c!=" "): #first non space character
                break
        
        if(index==-1):
            return 0
        else:
            for i in range(index,len(A)):
                if(A[i]!=" "):
                    l+=1
                else:
                    break
            return l
                    
                
