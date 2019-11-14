#https://www.interviewbit.com/problems/evaluate-expression/
class Solution:
    # @param A : list of strings
    # @return an integer
    def evalRPN(self, A):
        stack=[]
        for c in A:
            if(c=="+"):
                op2=int(stack.pop())
                op1=int(stack.pop())
                res=str(op1+op2)
                stack.append(res)
            elif(c=="*"):
                op2=int(stack.pop())
                op1=int(stack.pop())
                res=str(op1*op2)
                stack.append(res)
            elif(c=="/"):
                op2=int(stack.pop())
                op1=int(stack.pop())
                res=str(op1//op2)
                stack.append(res)
            elif(c=="-"):
                op2=int(stack.pop())
                op1=int(stack.pop())
                res=str(op1-op2)
                stack.append(res)
            else:
                stack.append(c)
                
        return stack.pop()
                
                
