#https://www.interviewbit.com/problems/letter-phone/
class Solution:
    # @param A : string
    # @return a list of strings
    def letterCombinations(self, A):
        digits=A
        n=len(digits)
        letters={1:["1"],0:["0"],2:['a','b','c'],3:['d','e','f'],4:['g','h','i'],5:['j','k','l'],6:['m','n','o'],7:['p','q','r','s'],8:['t','u','v'],9:['w','x','y','z']}
        answers=[]
        def printLetters(index,combination):
            if(len(combination)==n):
                answers.append(combination)
                return 
            current_digit=int(digits[index])
            for char in letters[current_digit]:
                printLetters(index+1,combination+char)
        
        printLetters(0,"")
        return sorted(answers)