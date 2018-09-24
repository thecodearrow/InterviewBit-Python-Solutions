"""
For Given Number N find if its COLORFUL number or not

A number can be broken into different contiguous sub-subsequence parts. 
Suppose, a number 3245 can be broken into parts like 3 2 4 5 32 24 45 324 245. 
And this number is a COLORFUL number, since product of every digit of a contiguous subsequence is different

"""

class Solution:
 
    def colorful(self, A):
        n=str(A)
        number=[]
        for c in n:
            number.append(int(c))
        
        seen=set()
       
        for i in range(len(n)):
            product=number[i]
            if(product in seen):
                return 0
            seen.add(product)
            
            for j in range(i+1,len(n)):
                product*=number[j]
                if(product in seen):
                    return 0
                seen.add(product)
        
        return 1
            
        
