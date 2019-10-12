#https://www.interviewbit.com/problems/subset/

class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def subsets(self, A):
        A=sorted(A)
        answer=[]
        n=len(A)
        def makeSubsets(index,currentSet):
            if(index==n):
                answer.append(currentSet)
            else:
                makeSubsets(index+1,currentSet)
                makeSubsets(index+1,currentSet+[A[index]])
            
        makeSubsets(0,[])
        return sorted(answer)
