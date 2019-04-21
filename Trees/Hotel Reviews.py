#Without Tries 

from collections import defaultdict
class Solution:
    # @param A : string
    # @param B : list of strings
    # @return a list of integers
    def solve(self, A, B):
        good_words=A.split("_")
        good=set()
        order={}
        idx=0
        for s in B:
            order[s]=idx
            idx+=1
            
        for g in good_words:
            good.add(g)
        good_words=good
        words=[]
        for s in B:
            strings=s.split("_")
            count=0
            for string in strings:
                if(string in good_words):
                    count+=1
            words.append((s,count))
        words=sorted(words,key=lambda x:x[1])[::-1]
        ans=[]
        temp=[]
        
        reordering=defaultdict(list)
        for i in range(len(words)):
            w=words[i]
            reordering[w[1]].append(order[w[0]])
            
        keys=sorted(reordering)[::-1]
        for k in keys:
            for i in reordering[k][::-1]:
                ans.append(i)
                
        
        
        return ans
        
