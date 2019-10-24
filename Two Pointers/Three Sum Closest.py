#https://www.interviewbit.com/problems/3-sum/
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def threeSumClosest(self, A, B):
        a=sorted(A)
        target_sum=B
        diff=float("inf")
        answer=None
        n=len(A)
        for i in range(n):
            first=a[i]
            l=i+1
            r=n-1
            while l<r:
                second=a[l]
                third=a[r]
                current_sum=first+second+third
                if(abs(current_sum-target_sum)<diff):
                    diff=abs(current_sum-target_sum)
                    answer=current_sum
                if(current_sum==target_sum):
                    return current_sum
                elif(current_sum<target_sum):
                    l+=1
                else:
                    r-=1
                    
        return answer
        
