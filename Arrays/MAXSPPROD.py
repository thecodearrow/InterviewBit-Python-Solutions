"""

You are given an array A containing N integers. The special product of each ith integer in this array is defined as the product of the following:<ul>

LeftSpecialValue: For an index i, it is defined as the index j such that A[j]>A[i] (i>j). If multiple A[j]’s are present in multiple positions, the LeftSpecialValue is the maximum value of j. 

RightSpecialValue: For an index i, it is defined as the index j such that A[j]>A[i] (j>i). If multiple A[j]s are present in multiple positions, the RightSpecialValue is the minimum value of j.

Write a program to find the maximum special product of any integer in the array.

Input: You will receive array of integers as argument to function.

Return: Maximum special product of any integer in the array modulo 1000000007.

Note: If j does not exist, the LeftSpecialValue and RightSpecialValue are considered to be 0.

Constraints 1 <= N <= 10^5 1 <= A[i] <= 10^9

"""

class Solution:
    # @param A : list of integers
    # @return an integer
    
   
        
    def maxSpecialProduct(self, A):
       
        left=[0]*len(A)
        right=[0]*len(A)
       
        stack=[]
        
        for i in range(len(A)):
            while stack and not A[i]<A[stack[-1]]:
                stack.pop()
            left[i]=stack[-1] if stack else 0
            stack.append(i)
        
        stack=[] #reset stack    
        for i in range(len(A)-1,-1,-1):
            while stack and not A[i]<A[stack[-1]]: 
                stack.pop()
            right[i]=stack[-1] if stack else 0
            stack.append(i)
            
        ans=0
      
        for i in range(len(A)):
            ans=max(ans,left[i]*right[i])
        
        return ans%1000000007
        
        
            
        
        
        
            
            
            
        
