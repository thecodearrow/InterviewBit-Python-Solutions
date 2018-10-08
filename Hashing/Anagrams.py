

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
        
        
        
