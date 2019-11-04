#https://www.interviewbit.com/problems/best-time-to-buy-and-sell-stocks-i/
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        if(len(A)<=1):
            return 0
        maxProfit=0
        minStockOption=A[0]
        for i in range(1,len(A)):
            currentProfit=A[i]-minStockOption
            maxProfit=max(maxProfit,currentProfit)
            minStockOption=min(minStockOption,A[i])
        return maxProfit
