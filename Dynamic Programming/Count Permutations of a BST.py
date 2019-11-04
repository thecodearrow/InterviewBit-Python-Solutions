#https://www.interviewbit.com/problems/count-permutations-of-bst

#TLE
class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    
    def ncr(self,n, r):
        fact={}
        fact[0]=1 
        for i in range(1,51):
            fact[i]=fact[i-1]*i
        if(r>n):
            return 0
        return fact[n] // fact[n-r] // fact[r]
    def countBSTs(self,n,h,memo):
        if(n<=1):
            if(h==0):
                return 1
            return 0
        if(h>=n):
            return 0
        if(h<0):
            return 0
        if(memo[n][h]):
            return memo[n][h]
        bsts_count=0
        for i in range(1,n+1):
            root_i_count=0
            root_i_count+=(self.countBSTs(i-1,h-1,memo)*self.countBSTs(n-i,h-1,memo))
            for hi in range(0,h-1):
                root_i_count+=(self.countBSTs(i-1,h-1,memo)*self.countBSTs(n-i,hi,memo))
                root_i_count+=(self.countBSTs(i-1,hi,memo)*self.countBSTs(n-i,h-1,memo))
            
            
            bsts_count+=root_i_count*self.ncr(n-1,i-1)
            
        memo[n][h]=bsts_count
        return memo[n][h]
        
    def cntPermBST(self, A, B):
        n=A
        h=B
        memo=[[None for i in range(h+1)]for i in range(n+1)]
        ans=self.countBSTs(n,h,memo)
        modulo=10**9+7
        return ans%modulo
        
