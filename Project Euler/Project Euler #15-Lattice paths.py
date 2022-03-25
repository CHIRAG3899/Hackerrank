#How many such routes are there through a N X M grid? As number of ways can be very large, print it modulo(10^9 + 7) .
#Input Format
#The first line contains an integer T , i.e., number of test cases.
##Next T lines will contain integers N and M.
#Output Format
#Print the values corresponding to each test case.
#Sample Input
#2
#2 2
#3 2
#Sample Output
#6
#10

p = int(1e9+7) # NOTE: the conversion is important

def exp_mod(a, n):
    if n == 0:
        return 1
    temp = exp_mod(a, n // 2)
    if n % 2 == 0:
        return (temp * temp) % p
    return (temp * temp * a) % p

maxm = 500
maxn = 500

factor = [1]
inv_factor = [1]

def init():
    for i in range(1, maxm+maxn+1): # NOTE: the range is this
        factor.append((factor[i-1] * i) % p)
        inv_factor.append((inv_factor[i-1] * exp_mod(i, p-2)) % p)

init()
T = int(input())
for t in range(T):    
    n, m = map(int, input().split())    
    print((factor[n+m] * inv_factor[n] * inv_factor[m]) % p)
