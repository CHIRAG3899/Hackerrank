#Find the sum of all the primes not greater than given N.
#Input Format
#The first line contains an integer T i.e. number of the test cases.
#The next T lines will contains an integer N.
#Output Format
#Print the value corresponding to each test case in separate line.
#Sample Input 0
#2
#5
#10
#Sample Output 0
#10
#17
#Explanation 0
#For N=5, we have primes as (2,3,5} and the sum is 10.
#For N=10, we have primes as (2,3,5,7} and the sum is 17.

import sys
# read test cases
t = int(input())
max_n = 0
n = []
#saves all test cases in n
for _t in range(t):
    n.append(int(input()))
    if n[-1] > max_n:
        max_n = n[-1]
#create sieve for prime numbers
sieve = list(range(max_n+1))
#put sum of all primes until now
value = 0
#calculate sieve
for i in range(2,len(sieve)):
    #if is prime (anything bigger than zero for current index is a prime)
    if sieve[i] > 0:
        #add to the sum of all primes
        value += sieve[i]
        for j in range(i+sieve[i],len(sieve),sieve[i]):
            #flag as not prime
            sieve[j] = -1
    #after using memory space, put current sum of all primes for easier post access
    sieve[i] = value
#give back all answers, that are saved in sieve
for answer in n:
    print(sieve[answer])
