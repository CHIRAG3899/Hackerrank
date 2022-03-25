#What is the sum of the digits of the number 2^N  ?
#Input Format
#The first line contains an integer T, i.e., number of test cases.
#Next T lines will contain an integer N.
#Output Format
#Print the values corresponding to each test case.
#Sample Input
#3
#3
#4
#7
#Sample Output
#8
#7
#11
#Explanation
#2^3=8, sum of digits is 8.
#2^4=16, sum of digits is 7.
#2^7=128, sum of digits is 11.

def sumofdigits(s):
    t=0
    for i in s:
        t+=int(i)
    return t
        
for i in range(int(input())):
    n=int(input())
    print(sumofdigits(str(pow(2,n))))
