"""
Given an array of integers A of size N and an integer B. College library has N books,the ith book has A[i] number of pages. You have to allocate books to B number of students so that maximum number of pages alloted to a student is minimum.
A book will be allocated to exactly one student.
Each student has to be allocated at least one book.
Allotment should be in contiguous order, for example: A student cannot be allocated book 1 and book 3, skipping book 2.
Calculate and return that minimum possible number. 
NOTE: Return -1 if a valid assignment is not possible. 
 
"""


class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return an integer
	def canAllocate(self,pages,n,students,max_pages):
	    current_pages=0 #current student is allocated 0 pages
	    current_student=1 #count of students who have their pages assigned completed
	    i=0
	    for p in pages:
	        if(current_pages>max_pages):
	            #current book pages cannot be allotted to any student!
	            return False
	        if(current_pages+p<=max_pages):
	            current_pages+=p #assign the current pages to the current student
	            i+=1
	        else:
	            current_pages=p
	            current_student+=1 #assignment complete, move on to the next student
	            if(current_student>students):
	                #more students are required
	                return False
	    
	    return True
	    
	def books(self, pages, students):
	    n=len(pages)
	    if(students>n):
	        #more students than available books!
	        return -1
	    start=max(pages) #the best case is each student is assigned one page slot... in that case, the best is max(pages)
	    end=sum(pages)
	    min_pages=end
	    while(start<=end):
	        mid=start+(end-start)//2
	        if(self.canAllocate(pages,n,students,mid)):
	            #try to minimise it if possible
	            #print(mid,"possible")
	            min_pages=min(min_pages,mid)
	            end=mid-1
	        else:
	            start=mid+1
	            
	    return min_pages
	        
