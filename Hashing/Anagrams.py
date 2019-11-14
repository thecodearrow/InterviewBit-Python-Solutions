

#https://www.interviewbit.com/problems/anagrams/

"""
Given an array of strings, return all groups of strings that are anagrams. 
Represent a group by a list of integers representing the index in the original list. 
Look at the sample case for clarification.

"""
from collections import defaultdict
class Solution:
   
    def anagrams(self, A):
        words=[]
        for w in A:
            w="".join(sorted(w))
            words.append(w)
        
        ans=[]
        
        d=defaultdict(list)
        index=1
        for w in words:
            d[w].append(index)
            index+=1
        
        for k in d:
            ans.append(d[k])
        
        return sorted(ans)
        
        
class Solution:
    # @param A : tuple of strings
    # @return a list of list of integers
    def anagrams(self, A):
        seen_at={}
        ans=[]
        group_index=0
        for i,word in enumerate(A):
            sorted_word="".join(sorted(word))
            if(sorted_word in seen_at):
                ans[seen_at[sorted_word]].append(i+1)
            else:
                ans.append([i+1])
                seen_at[sorted_word]=group_index
                group_index+=1
                
        return ans
