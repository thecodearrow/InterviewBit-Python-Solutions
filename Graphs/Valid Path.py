#Valid Path

#https://www.interviewbit.com/problems/valid-path/

from collections import defaultdict

class Graph:
    def __init__(self):
        self.neighbours=defaultdict(list)
    
    def add(self,u,v):
        self.neighbours[u].append(v)
        self.neighbours[v].append(u)
    
    
    def BFS(self,dest):
        s=(0,0)
        visited=defaultdict(lambda:False)
        visited[s]=True
        queue=[s]
        while queue:
            u=queue.pop(0)
            
            for v in self.neighbours[u]:
                if(not visited[v]):
                    queue.append(v)
                    visited[v]=True
        
        if(visited[dest]):
            return True
        
        return False
        
        

class Solution:

    
    def incircle(self, D, E, F, point):
        x=point[0]
        y=point[1]
        for z in range(len(E)):
            if ((E[z] - x) ** 2 + (F[z] - y) ** 2) ** 0.5 <= D:
                return True
        return False

    def solve(self, x, y, n, r, cx, cy):
        circle_points=set()
        #each circle will have 5 points including center to be blocked!
        for i in range(n):
            p1=cx[i]
            p2=cy[i]
            circle_points.add((p1,p2)) 
            for w in range(1,r+1):
                circle_points.add((p1+w,p2))
                circle_points.add((p1-w,p2))
                circle_points.add((p1,p2+w))
                circle_points.add((p1,p2-w))
            
            
        rectangle=set()
        
        for i in range(x+1):
            for j in range(y+1):
                rectangle.add((i,j))
                
        g=Graph()
        
        
        
        for i in range(x+1):
            for j in range(y+1):
                source=(i,j)
                one=(i+1,j)
                two=(i,j+1)
                three=(i+1,j+1)
                four=(i-1,j-1)
                five=(i-1,j+1)
                six=(i+1,j-1)
                seven=(i-1,j)
                eight=(i,j-1)
                if(not self.incircle(r,cx,cy,source)):
                    if(one in rectangle and not self.incircle(r,cx,cy,one)):
                        g.add(source,one)
                    if(two in rectangle and not self.incircle(r,cx,cy,two)):
                        g.add(source,two)
                    if(three in rectangle and not self.incircle(r,cx,cy,three)):
                        g.add(source,three)
                    if(four in rectangle and not self.incircle(r,cx,cy,four)):
                        g.add(source,four)
                    if(five in rectangle and not self.incircle(r,cx,cy,five)):
                        g.add(source,five)
                    if(six in rectangle and not self.incircle(r,cx,cy,six)):
                        g.add(source,six)
                    if(seven in rectangle and not self.incircle(r,cx,cy,seven)):
                        g.add(source,seven)
                    if(eight in rectangle and not self.incircle(r,cx,cy,eight)):
                        g.add(source,eight)
               
                
               
                
                
        
            
        if(g.BFS((x,y))):
            return "YES"
        else:
            return "NO"
            
        
        
            
            
        
