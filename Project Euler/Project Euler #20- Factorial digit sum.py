#Find the sum of the digits in the number N! 
#
#Input Format
#
#The first line contains an integer  T, i.e., number of test cases.
#Next T lines will contain an integer N.
#
#Output Format
#
#Print the values corresponding to each test case.
#
#Sample Input
#
#2
#3
#6
#Sample Output
#
#6
#9
#Explanation
#
#3! is 6, sum of digit is 6.
#6! is 720, sum of digits is 9.

def f(n):
    if n==0: return 1
    return n*f(n-1)
for _ in range(int(input())): print(sum(int(i) for i in str(f(int(input())))))