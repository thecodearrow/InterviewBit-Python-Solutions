#Without Tries 
#https://www.interviewbit.com/problems/hotel-reviews/

class Solution:
    # @param A : string
    # @param B : list of strings
    # @return a list of integers
    
    def solve(self, A, B):
        keys=A.split("_")
        keywords=set()
        for k in keys:
            keywords.add(k)
        
        good_reviews=[]
        for i,word in enumerate(B):
            score=0
            for w in word.split("_"):
                if(w in keywords):
                    score+=1
            good_reviews.append([i,score])
            
        good_reviews=sorted(good_reviews,key=lambda x:x[1],reverse=True)
        
        review_order=[]
        for idx,score in good_reviews:
            review_order.append(idx)
            
        return review_order

#Using Trie

class Trie:
    def __init__(self):
        self.letters={}
    
    def addString(self,string):
        letters=self.letters
        for c in string:
            if(c not in letters):
                letters[c]={}
            letters=letters[c]
        
        letters["*"]=True #Marks the end of a word
    
    def containsString(self,string):
        letters=self.letters
        for c in string:
            if(c not in letters):
                return False
            letters=letters[c]
        
        if("*" in letters):
            #end of string
            return True
        return False
                
        

class Solution:
    # @param A : string
    # @param B : list of strings
    # @return a list of integers
    
    def solve(self, A, B):
        keywords=A.split("_")
        t=Trie()
        for s in keywords:
            t.addString(s)
        
        good_reviews=[]
        for i,word in enumerate(B):
            score=0
            for w in word.split("_"):
                if(t.containsString(w)):
                    score+=1
            good_reviews.append([i,score])
            
        good_reviews=sorted(good_reviews,key=lambda x:x[1],reverse=True)
        
        review_order=[]
        for idx,score in good_reviews:
            review_order.append(idx)
            
        return review_order
