#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get
#3,5,6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below N.
#Input Format
#First line contains T that denotes the number of test cases. This is followed by
#T lines, each containing an integer,N .
#Output Format
#For each test case, print an integer that denotes the sum of all the multiples of 3 or 5 below N.
#Sample Input 0
#2
#10
#100
#Sample Output 0
#23
#2318
#Explanation 0
#For N=10, if we list all the natural numbers below  that are multiples of 3 or
#5, we get 3,5,6 and 9. The sum of these multiples is 23.
#Similarly for N=100, we get 2318.

t=int(input())
def ar(x):
    return x*(x+1);
for i in range(t):
    n =int(input())
    n -=1;
    a=int(n/3);
    b=int(n/5);
    c=int(n/15);
    print(int(int(3*ar(a) + 5*ar(b) - 15*ar(c))>>1));

