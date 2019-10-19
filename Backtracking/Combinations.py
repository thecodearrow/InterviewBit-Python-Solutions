#https://www.interviewbit.com/problems/combinations/

class Solution:
    # @param A : integer
    # @param B : integer
    # @return a list of list of integers
    def combine(self, A, B):
        n=A
        k=B
        a=[i for i in range(1,n+1)]
        answers=[]
        def combinations(index,currentSet):
            if(len(currentSet)==k):
                answers.append(currentSet[:])
                return
            if(index>=n):
                return
            combinations(index+1,currentSet+[a[index]])
            combinations(index+1,currentSet)
            
        combinations(0,[])
        return answers
