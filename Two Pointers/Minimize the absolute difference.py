#https://www.interviewbit.com/problems/minimize-the-absolute-difference/

class Solution:

    def solve(self, A, B, C):
        p1=0
        p2=0
        p3=0
        answer=float("inf")
        if(len(A)==0 or len(B)==0 or len(C)==0):
            return None
            
        while p1<len(A) and p2<len(B) and p3<len(C):
            a,b,c=A[p1],B[p2],C[p3]
            diff=max(a,b,c)-min(a,b,c)
            answer=min(answer,diff)
            #The array which contributes the min number is moved forward
            if(a<=b and a<=c):
                p1+=1
            elif(b<=a and b<=c):
                p2+=1
            else:
                p3+=1
                
        return answer
        
