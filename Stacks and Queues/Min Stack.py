#https://www.interviewbit.com/problems/min-stack/
class MinStack:
    # @param x, an integer
    def __init__(self):
        self.mainStack=[]
        self.minimums=[]
        
    def updateMinimums(self,number):
        n=len(self.minimums)
        if(n==0):
            current_min=number
        else:
            current_min=min(self.minimums[n-1],number)
        self.minimums.append(current_min)
            
    def push(self, x):
        self.mainStack.append(x)
        self.updateMinimums(x)

    # @return nothing
    def pop(self):
        if(len(self.mainStack)>0):
            self.mainStack.pop()
            self.minimums.pop()
            
    # @return an integer
    def top(self):
        n=len(self.mainStack)
        if(n>0):
            return self.mainStack[n-1]
        else:
            return -1


    # @return an integer
    def getMin(self):
        n=len(self.mainStack)
        if(n>0):
            return self.minimums[n-1]
        else:
            return -1

