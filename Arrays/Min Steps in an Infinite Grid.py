"""
You are in an infinite 2D grid where you can move in any of the 8 directions :

 (x,y) to 
    (x+1, y), 
    (x - 1, y), 
    (x, y+1), 
    (x, y-1), 
    (x-1, y-1), 
    (x+1,y+1), 
    (x-1,y+1), 
    (x+1,y-1) 

You are given a sequence of points and the order in which you need to cover the points. 
Give the minimum number of steps in which you can achieve it. You start from the first point.

"""

import math
class Solution:

    
    def distance(self,a,b):
        x1=a[0]
        x2=b[0]
        y1=a[1]
        y2=b[1]
        one=abs(x1-x2)
        two=abs(y1-y2)
        return max(one,two)
        
       
    def coverPoints(self, A, B):
        n=len(A)
        if(n<2):
            return 0
        ans=0
        for i in range(n-1):
            first=[A[i],B[i]]
            second=[A[i+1],B[i+1]]
            d=self.distance(first,second)
            ans+=d
        return ans
       
       
       
            
            
            
        
