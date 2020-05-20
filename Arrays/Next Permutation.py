#https://stackoverflow.com/questions/1622532/algorithm-to-find-next-greater-permutation-of-a-given-string

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def nextPermutation(self, A):
        n=len(A)
        sort_index=n-1
        for i in range(n-2,-1,-1):
            if(A[i]<A[i+1]):
                #Find j such that j>i and A[j]>A[i]
                
                min_j=i+1
                min_ele=A[i+1]
                for j in range(i+1,n):
                    if(A[j]>A[i]):
                        min_ele=A[j]
                        min_j=j
                
                #Swap A[j],A[i]
                A[i],A[min_j]=A[min_j],A[i]
                break
            else:
                sort_index-=1
        
        #start reversing!
        start=sort_index
        end=n-1
        while start<end:
            A[start],A[end]=A[end],A[start]
            start+=1
            end-=1
            
        return A
            