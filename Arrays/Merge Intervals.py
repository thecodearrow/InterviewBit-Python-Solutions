"""
#https://www.interviewbit.com/problems/merge-intervals/

#EXCELLENT TUTORIAL IS HERE >>  https://www.youtube.com/watch?v=WdgAKCnWnwA

Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

"""

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
import functools
from collections import deque
class Solution:
    # @param intervals, a list of Intervals
    # @param new_interval, a Interval
    # @return a list of Interval
    
    def cmp(self,x,y):
        s1=x.start 
        s2=y.start
        e1=x.end
        e2=y.end
        if(s1>s2):
            return 1
        elif(s1==s2):
            if(e1>e2):
                return 1
            else:
                return -1
        else:
            return -1
            
    def insert(self, intervals, new_interval):
        
        intervals.append(new_interval)
        intervals=sorted(intervals,key=functools.cmp_to_key(self.cmp))
        
        stack=deque()
        stack.append(intervals[0])
        for idx in range(1,len(intervals)):
            i=intervals[idx]
            top_start=stack[-1].start
            top_end=stack[-1].end
            if(top_end<i.start): #does not overlap
                stack.append(i)
     
            elif(top_end<i.end): #overlaps
                stack.pop()
                new_I=Interval(top_start,i.end)
                stack.append(new_I)
            
            
        ans=list(stack)
        return ans


 
            
        
        
                
            
        
        
        
