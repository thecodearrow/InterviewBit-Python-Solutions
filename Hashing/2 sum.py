#https://www.interviewbit.com/problems/2-sum/

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def twoSum(self, A, target):
        seen_at={}
        ans=[]
        for i,ele in enumerate(A):
            first=A[i]
            second=target-A[i]
            if(second in seen_at):
                if(len(ans)==0):
                    ans=[seen_at[second],i]
                else:
                    if(ans[1]>i):
                        ans=[seen_at[second],i]
                    elif(ans[1]==i):
                        if(ans[0]>seen_at[second]):
                            ans=[seen_at[second],i]
            if(ele not in seen_at):        
                seen_at[ele]=i
                
        if(ans):
            ans[0]+=1
            ans[1]+=1
        return ans
            
        
            
        
