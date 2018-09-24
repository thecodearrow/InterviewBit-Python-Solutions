"""
Given a non-negative number represented as an array of digits,

add 1 to the number ( increment the number represented by the digits ).

The digits are stored such that the most significant digit is at the head of the list.

Example:

If the vector has [1, 2, 3]

the returned vector should be [1, 2, 4]

as 123 + 1 = 124.

"""

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        number=0
        actual=[]
        seen=False
        for ele in A:
            if(ele!=0):
                seen=True
            if(seen):
                actual.append(ele)
        l=len(actual)
        actual=actual[::-1]
        ans=[]
        carry=1
        for d in actual:
            store=(d+carry)%10
            if(d+carry<10):
                carry=0
            ans.append(store)
        
        if(carry==1):
            ans.append(carry)
        ans=ans[::-1]
        return ans
        
        
        
