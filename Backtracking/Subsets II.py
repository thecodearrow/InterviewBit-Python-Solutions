#https://www.interviewbit.com/problems/subsets-ii/

class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def subsetsWithDup(self, A):
        A=sorted(A)
        answer=[]
        n=len(A)
        def findAllSubsets(idx,currentSet):
            if(idx==n):
                answer.append(currentSet)
            else:
                findAllSubsets(idx+1,currentSet)
                findAllSubsets(idx+1,currentSet+[A[idx]])
        findAllSubsets(0,[])
        answer=set([tuple(x) for x in answer])
        return sorted(answer)
            
