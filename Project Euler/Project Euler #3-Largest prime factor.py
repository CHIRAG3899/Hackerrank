#The prime factors of 13195 are 5,7,13 and 29.
#What is the largest prime factor of a given number N?
#Input Format
#First line contains T, the number of test cases. This is followed by T lines each containing an integer N.
#Output Format
#For each test case, display the largest prime factor of N.
#Sample Input 0
#2
#10
#17
#Sample Output 0
#5
#17
#Explanation 0
#Prime factors of 10 are {2,5}, largest is 5.
#Prime factor of 17 is 17 itself, hence largest is 17.


import math
n = int(input())
def isPrime(a):
    val = True
    for i in range(2,int(math.sqrt(a))+1):
        if a%i==0:
            val = False
    return val
max = 1
for _ in range(n):
    a = int(input())
    for i in range(1,int(math.sqrt(a))+1):
        if a%i == 0:
          if isPrime(a//i) and a//i>max:
              max = a//i
              break
          elif isPrime(i):
            max = i        
    print(max)
