"""
Given a read only array of n + 1 integers between 1 and n, find one number that repeats in linear time using less than O(n) space and traversing the stream sequentially O(1) times.


#Assuming only one integer repeats more than once! 

"""

class Solution:

    def repeatedNumber(self, A):
        s = sum(A)
        n = len(A)
        missing = s - (n*(n-1))/2
        return missing