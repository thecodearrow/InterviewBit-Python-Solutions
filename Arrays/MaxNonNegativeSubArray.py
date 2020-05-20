
#https://www.interviewbit.com/problems/max-non-negative-subarray/

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        global_max_sum=0
        global_max_length=0
        current_max_sum=0
        current_max_length=0
        curr_i=0
        curr_j=0
        ans_i=None
        ans_j=None
        for i,ele in enumerate(A):
            if(ele>=0):
                current_max_length+=1
                current_max_sum+=ele
                curr_j+=1
            if(current_max_sum>global_max_sum or (current_max_sum==global_max_sum and current_max_length>global_max_length)):
                ans_i,ans_j=curr_i,curr_j
                global_max_sum=current_max_sum
                global_max_length=current_max_length
            if(ele<0):
                current_max_sum=0
                current_max_length=0
                curr_i=i+1
                curr_j=i+1
                
        if(ans_i is None):
            return []
            
        return A[ans_i:ans_j]
                
            
            

    