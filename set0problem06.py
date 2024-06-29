## Author: Thomas Mitchell
## Date: 06/28/2024
## Assignment: MIT 6006 2020 Problem Set 0 Problem 0-6

## Write Python Function count_long_subarrays(A) which accepts Python Tuple A=(a0,a1,...,an-1) of n>0
## positive integers, and returns the number of longest increasing subarrays of A.

## Variables:
# longestIncStrk - stores the streaks (whether 1 or 1000)
# incstrk - counts the streak over iterations
# for loop - generates value up until the index of the second last
# if/else - for each value, it checks whether less than next, if so, it adds one to the strk,
# if not, the streak ends and it is appended to the streak list.

def count_long_subarrays(A):
    longestIncStrk=[]
    incstrk=1
    lenArray=len(A)
    if lenArray == 1:
        return 1
    else:
        for elem in range(lenArray-1):
            if A[elem]<A[elem+1]:
                incstrk+=1
            else:
                longestIncStrk.append(incstrk)
                incstrk=1
        longestIncStrk.append(incstrk)
    return longestIncStrk.count(max(longestIncStrk))




    


           

