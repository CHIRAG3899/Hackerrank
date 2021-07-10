#Find maximum possible value of abc among all such Pythagorean triplets, If there is no such Pythagorean triplet print -1.
#Input Format
#The first line contains an integer T i.e. number of test cases.
#The next T lines will contain an integer N.
#Output Format
#Print the value corresponding to each test case in separate lines.
#Sample Input 0
#2
#12
#4
#Sample Output 0
#60
#-1
#Explanation 0
#For N=12, we have a triplet {3,4,5}, whose product is 60.
#For N=4, we don't have any pythagorean triple.

import sys

def Find_Pythagorean_Triplet(n):
    if n % 2 == 1:
        return(-1,-1,-1)
    a0 = -1
    b0 = -1
    c0 = -1
    for a in range(int(n//3),0,-1):
        if (n**2 - 2*a*n) % (2*(n-a)) == 0:
            b = (n**2 - 2*a*n)//(2*(n-a))
            if a*b*(n-a-b)>a0*b0*c0:
                a0 = a
                b0 = b
                c0 = n-a-b
    return(a0,b0,c0)


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    a,b,c = Find_Pythagorean_Triplet(n)
    print(a*b*c)
