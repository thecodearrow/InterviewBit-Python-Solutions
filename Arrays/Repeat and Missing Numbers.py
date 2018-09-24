"""
Repeat and Missing Number Array

You are given a read only array of n integers from 1 to n.

Each integer appears exactly once except A which appears twice and B which is missing.

Return A and B.

"""

#uses extra memory
class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        visited=set()
        numbers=set()
        for i in range(1,len(A)+1):
            numbers.add(i)
        for ele in A:
            if(ele in visited):
                repeat=ele
            visited.add(ele)
        
        missing=numbers.difference(visited)
        missing=list(missing)[0]
        return [repeat,missing]
                
        

#without using extra memory

"""
Sum(Actual) = Sum(1...N) + A - B

    Sum(Actual) - Sum(1...N) = A - B. 

    Sum(Actual Squares) = Sum(1^2 ... N^2) + A^2 - B^2

    Sum(Actual Squares) - Sum(1^2 ... N^2) = (A - B)(A + B) 

    = (Sum(Actual) - Sum(1...N)) ( A + B). 

"""

