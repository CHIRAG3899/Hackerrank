#Find the absolute difference between the sum of the squares of the first N natural numbers and the square of the sum.
#Input Format
#First line contains T that denotes the number of test cases. This is followed by T lines, each containing an integer, N.
#Output Format
#Print the required answer for each test case.
#Sample Input 0
#2
#3
#10
#Sample Output 0
#22
#2640

import sys

t=int(input())
while t>0:
    n=int(input())
    j=n*(n+1)*(2*n+1)//6
    m=n*(n+1)//2
    m=m*m
    print(m-j)
    t -=1
