#https://www.interviewbit.com/problems/remove-duplicates-from-sorted-array/
class Solution:
    def removeDuplicates(self, A):
        n=len(A)
        count=1
        for i in range(n-1):
            if(A[i]!=A[i+1]):
                A[count]=A[i+1]
                count+=1
            
        return count
            
