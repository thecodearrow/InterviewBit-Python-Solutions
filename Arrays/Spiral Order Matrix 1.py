#Given a matrix of m * n elements (m rows, n columns), return all elements of the matrix in spiral order.

class Solution:
    # @param A : tuple of list of integers
    # @return a list of integers
    
    def moveDown(self,x,y):
        return x+1,y
    
    def moveLeft(self,x,y):
        return x,y-1
    
    def moveUp(self,x,y):
        return x-1,y
    
    def moveRight(self,x,y):
        return x,y+1
        
    def checkFinish(self,count,total):
        if(count==total):
            return True
        return False
    def spiralOrder(self, A):
        rows=len(A)
        cols=len(A[0])
        total=rows*cols
        
        x=0
        y=0
        ans=[]
        visited=set()
        count=0
        while count<=total:
            while(y<cols and (x,y) not in visited):
                
                visited.add((x,y))
                ans.append(A[x][y])
                x,y=self.moveRight(x,y)
                count+=1
                if(self.checkFinish(count,total)):
                    return ans  
            x,y=self.moveLeft(x,y)
            x,y=self.moveDown(x,y)
            while(x<rows and (x,y) not in visited):
                
                visited.add((x,y))
                ans.append(A[x][y])
                x,y=self.moveDown(x,y)
                count+=1
                if(self.checkFinish(count,total)):
                    return ans
            x,y=self.moveUp(x,y)  
            x,y=self.moveLeft(x,y)
            while(y>=0 and (x,y) not in visited):
                
                visited.add((x,y))
                ans.append(A[x][y])
                x,y=self.moveLeft(x,y)
                count+=1
                if(self.checkFinish(count,total)):
                    return ans
            x,y=self.moveRight(x,y)
            x,y=self.moveUp(x,y)
            while(x>=0 and (x,y) not in visited):
                
                visited.add((x,y))
                ans.append(A[x][y])
                x,y=self.moveUp(x,y)
                count+=1
                if(self.checkFinish(count,total)):
                    return ans
            x,y=self.moveDown(x,y)
            x,y=self.moveRight(x,y)
                
            
            
            
        
            
        return ans
    

        
