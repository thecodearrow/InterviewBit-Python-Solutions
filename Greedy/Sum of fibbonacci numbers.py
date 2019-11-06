#Very similar to the min no. of coins reqd. to make a given change
#Also greedy strategy works
#https://www.interviewbit.com/problems/sum-of-fibonacci-numbers/
import bisect
class Solution:
    # @param A : integer
    # @return an integer
    def generateFibSeries(self,n):
        series=[1,1]
        fib_number=1
        i=2
        while fib_number<=n:
            fib_number=series[i-1]+series[i-2]
            series.append(fib_number)
            i+=1
            
        return series
            
    def giveNumberLessThanOrEqualsN(self,a,n):
        idx=bisect.bisect_left(a,n)
        numLess=a[idx]
        if(numLess>n):
            numLess=a[idx-1]
        return numLess    
            
    def fibsum(self, A):
        fib_numbers=self.generateFibSeries(A)
        number=A
        count=0
        while number:
            count+=1
            numLess=self.giveNumberLessThanOrEqualsN(fib_numbers,number)
            number-=numLess
            
        
                    
        return count
