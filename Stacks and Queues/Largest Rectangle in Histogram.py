#https://www.interviewbit.com/problems/largest-rectangle-in-histogram/
class Solution:
    # @param A : list of integers
    # @return an integer
    
    def popAndComputeArea(self,currentHeight,idx,maxArea,stack,A):
        while(stack and A[stack[-1]]>currentHeight):
                poppedElementIdx=stack.pop()
                if(stack):
                    contributedArea=A[poppedElementIdx]*(idx-stack[-1]-1)
                else:
                    contributedArea=A[poppedElementIdx]*idx
                maxArea=max(contributedArea,maxArea)
        return maxArea,stack
        
    def largestRectangleArea(self, A):
        n=len(A)
        if(n==0):
            return 0
        if(n==1):
            return A[0]
        stack=[0]
        idx=1
        maxArea=0
        while idx<n:
            currentHeight=A[idx]
            topElementHeight=A[stack[-1]]
            if(not stack or topElementHeight<=currentHeight):
                stack.append(idx)
            else:
                maxArea,stack=self.popAndComputeArea(currentHeight,idx,maxArea,stack,A)
                stack.append(idx)
        
            idx+=1
            
        #Pop the remaining elements in stack!
        maxArea,stack=self.popAndComputeArea(0,idx,maxArea,stack,A) #
        return maxArea