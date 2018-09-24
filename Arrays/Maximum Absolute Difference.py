"""

You are given an array of N integers, A1, A2 ,…, AN. Return maximum value of f(i, j) for all 1 ≤ i, j ≤ N.
f(i, j) is defined as |A[i] - A[j]| + |i - j|, where |x| denotes absolute value of x.

"""

class Solution:
   
    def maxArr(self, A):
        array1=[]
        array2=[]
        for i in range(len(A)):
            array1.append(A[i]+(i+1))
            array2.append(A[i]-(i+1))
        
        one=max(array1)-min(array1)
        two=max(array2)-min(array2)
        
        return max(one,two)
