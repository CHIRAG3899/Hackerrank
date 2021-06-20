#Task
#A prime is a natural number greater than 1 that has no positive divisors other
#than  and itself. Given a number, , determine and print whether it is Prime or
#Not Prime.
#Input Format
#The first line contains an integer,T , the number of test cases.
#Each of the T subsequent lines contains an integer,n , to be tested for primality.
#Output Format
#For each test case, print whether n is Prime or Not Prime on a new line.
#Sample Input
#3
#12
#5
#7
#Sample Output
#Not prime
#Prime
#Prime

import math
for _ in range(int(input())):
    num = int(input())
    if num > 1:
        for i in range(2,math.floor(math.sqrt(num))+1):
            if (num % i) == 0:
                print('Not prime')
                break
        else:
            print('Prime')
    else:
        print('Not prime')
