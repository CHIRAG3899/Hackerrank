#What is the Nth prime number?
#Input Format
#First line contains T that denotes the number of test cases. This is followed by T lines, each containing an integer, N.
#Output Format
#Print the required answer for each test case.
#Sample Input 0
#2
#3
#6
#Sample Output 0
#5
#13
#Explanation 0
#The first 10 prime numbers are {2,3,5,7,11,13,17,19,23,29}
#we can see that 3rd prime number is 5 and 6th prime number is 13

import math as math

t = int(input().strip())
n = []
for _ in range(t):
    n.append(int(input().strip()))

def isPrime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0 :
            return False
    return True
# all first N prime numbers
N = 10000
prime_numbers = []
m =2
while len(prime_numbers) <=N-1:
    if isPrime(m):
        prime_numbers.append(m)
    m += 1
# nth prime number
for i in n:
    print(prime_numbers[i-1])
