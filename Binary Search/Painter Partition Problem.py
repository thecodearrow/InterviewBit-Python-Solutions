"""
Given 2 integers A and B and an array of integers C of size N. Element C[i] represents length of ith board.
You have to paint all N boards [C0, C1, C2, C3 … CN-1]. There are A painters available and each of them takes B units of time to paint 1 unit of board.
 Calculate and return minimum time required to paint all boards under the constraints that any painter will only paint contiguous sections of board. NOTE:
1. 2 painters cannot share a board to paint. That is to say, a board cannot be painted partially by one painter, and partially by another.
2. A painter will only paint contiguous boards. Which means a configuration where painter 1 paints board 1 and 3 but not 2 is invalid.

Return the ans % 10000003.

"""
class Solution:
	# @param A : integer
	# @param B : integer
	# @param C : list of integers
	# @return an integer
	
	def canPaint(self,boards,max_time,painters_available):
	    painters_needed=1
	    current_time=0
	    for b in boards:
	        if(b>max_time):
	            #board can't be painted! 
	            return False
	        if(b+current_time<=max_time):
	            current_time+=b
	        else:
	            current_time=b
	            painters_needed+=1
	            if(painters_needed>painters_available):
	                return False
	                
	    return True
	                
	            
	        
	def paint(self, painters_available, cost, boards):
        MOD= 10000003
        start=max(boards)
        end=sum(boards)
        min_time=end
        while start<=end:
            mid=start+(end-start)//2
            if(self.canPaint(boards,mid,painters_available)):
                min_time=min(min_time,mid)
                end=mid-1 #try to minimise it further
            else:
                #try to increase allotted time
                start=mid+1
                
            
        
        ans=(min_time%MOD * cost%MOD)%MOD
        return ans