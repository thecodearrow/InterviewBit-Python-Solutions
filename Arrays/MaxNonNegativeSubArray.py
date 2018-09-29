"""
Find out the maximum sub-array of non negative numbers from an array.
The sub-array should be continuous. That is, a sub-array created by choosing the second and fourth element and skipping the third element is invalid.

Maximum sub-array is defined in terms of the sum of the elements in the sub-array. Sub-array A is greater than sub-array B if sum(A) > sum(B).

NOTE: If there is a tie, then compare with segment's length and return segment which has maximum length
NOTE 2: If there is still a tie, then return the segment with minimum starting index
"""


import functools
class Solution:
    
    def cmp(self,x,y):
        s1=x[0]
        s2=y[0]
        l1=x[1]
        l2=y[1]
        start1=x[2]
        start2=y[2]
        if(s1>s2):
            return 1
        elif(s1==s2):
            if(l1>=l2):
                return 1
            elif(l1==l2):
                if(start1<=start2):
                    return 1
                else:
                    return -1
            
            else:
                return -1
        else:
            return -1
                
            
            
    def maxset(self, A):
        A.append(-1) #signifying the end
        arrays=[]
        start=0
        end=0
        for ele in A:
            if(ele>=0):
                end+=1
            else:
                if(start!=end):
                    arrays.append([start,end])
                start=end+1
                end=start
        if(len(arrays)==0):
            return [] #all negative numbers
        
        final_array=[] #[sum,length,start_index]
        for temp in arrays:
            a=A[temp[0]:temp[1]]
            store=[sum(a),len(a),temp[0],temp[1]]
            final_array.append(store)
        
        final_array=sorted(final_array,key=functools.cmp_to_key(self.cmp))[::-1]
        s=final_array[0][2]
        e=final_array[0][3]
        return A[s:e]
        
        
        
    