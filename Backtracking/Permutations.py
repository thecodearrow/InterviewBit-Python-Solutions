#https://www.interviewbit.com/problems/permutations/

class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def permute(self, A):
        answer=[]
        n=len(A)
        
        def printPermutations(currentIndex):
            if(currentIndex==n):
                answer.append(A[:])
            
            else:
                for i in range(currentIndex,n):
                    A[i],A[currentIndex]=A[currentIndex],A[i]
                    printPermutations(currentIndex+1)
                    A[i],A[currentIndex]=A[currentIndex],A[i]
                    
        
        printPermutations(0)
        return answer
                    
                
