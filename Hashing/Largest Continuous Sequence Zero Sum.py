#https://www.interviewbit.com/problems/largest-continuous-sequence-zero-sum/

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def lszero(self, A):
        sum_seen_at={0:-1}
        current_sum=0
        start_index=None
        end_index=None
        max_length=0
        for i in range(len(A)):
            current_sum+=A[i]
            if(current_sum in sum_seen_at):
                current_length=i-sum_seen_at[current_sum]
                if(current_length>max_length):
                    max_length=current_length
                    start_index=sum_seen_at[current_sum]+1
                    end_index=i
            else:
                sum_seen_at[current_sum]=i
                
        if(start_index is None):
            return []
        ans=[]
        for i in range(start_index,end_index+1):
            ans.append(A[i])
        return ans
            
