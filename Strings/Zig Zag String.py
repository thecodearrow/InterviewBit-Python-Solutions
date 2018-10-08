

"""

#https://www.interviewbit.com/problems/zigzag-string/

"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)


P.......A........H.......N
..A..P....L....S....I...I....G
....Y.........I........R

"""
class Solution:

    def convert(self, A, B):
        matrix=[]
        if(B==1):
            return A
        for i in range(B):
            matrix.append([]) #B rows
        
        count=0
        down=False
        for c in A:
            matrix[count].append(c)
            if(count==0):
                down=True
            if(count==B-1):
                down=False
            
            if(down):
                count+=1
            else:
                count-=1
            
        ans=""
        for i in range(B):
            for c in matrix[i]:
                ans+=c
        
        return ans
            
            
