"""
https://www.interviewbit.com/problems/count-and-say/

The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

Given an integer n, generate the nth sequence.

"""

class Solution:
    # @param A : integer
    # @return a strings
    def countAndSay(self, A):
        array=["1"]
       
        for index in range(A-1):
            store=""
            prev=array[-1]
            count=1
            for i in range(1,len(prev)):
                if(prev[i-1]==prev[i]):
                    count+=1
                else:
                    store+=str(count)+prev[i-1]
                    count=1
            store+=str(count)+prev[-1]
            array.append(store)
        return array[A-1]
                    
                    
                
                
                
                
        
