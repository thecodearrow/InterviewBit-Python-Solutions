#https://www.interviewbit.com/problems/greatest-common-divisor/

import math
class Solution:
   
    def gcd(self, A, B):
        if(B%A==0):
            return A
        
        return self.gcd(B%A,A)
            
        
        
