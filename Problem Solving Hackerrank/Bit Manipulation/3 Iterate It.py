#Consider the following pseudocode, run on an array A=[a0,a1,..an-1] of length n:
#
#rep := 0
#while A not empty:
#    B := []
#    for x in A, y in A:
#        if x != y: append absolute_value(x - y) to B
#    A := B
#    rep := rep + 1
#
#Given the values of n and array A, compute and print the final value of rep after the pseudocode above terminates; if the loop will never terminate, print -1 instead.
#
#Input Format
#
#The first line contains a single integer,n , denoting the length of array A.
#The second line contains n space-separated integers describing the respective values of a0,a1,...an-1.
#
#Output Format
#Print the final value of rep after the pseudocode terminates; if the loop will never terminate, print -1 instead.
#
#Sample Input 0
#3
#1 3 4
#
#Sample Output 0
#4
#
#Explanation 0
#After the first loop, A becomes [2,3,2,1,3,1]. After the second loop, the array only contains 1's and 2's. After the third loop, the array only contains 1's. After the fourth loop, the array is empty. Because the value of rep is incremented after each loop,rep=4 at the time the loop terminates. Thus, we print 4 as our answer.

import os
import sys

from math import gcd
from functools import reduce

#
# Complete the iterateIt function below.
#
# Note: didn't find any good pattern, so going for brute force (iterate and count)
#
def iterateIt(arr):
    remove_gcd(arr)
    n = a2b(arr)
    steps=0
    while n>0:
        kp = known_pat(n)
        if kp >= 0 : return steps + kp
        steps +=1
        n = iterate(n)
    return steps

def remove_gcd(arr):
    """Transform [a*i+b, i=i0<i1<i2...] to [i0-k,i1-k,i2-k, ... where k=i0-1]"""
    arr[:] = list(set(arr)) # remove duplicates and sort in place
    arr.sort()
    l = len(arr)
    if l>=2:
        a = reduce(gcd,(arr[i+1]-arr[i] for i in range(l-1)))
        b = arr[0] % a
        k = (arr[0]-b)//a - 1
        for i in range(l): arr[i] = (arr[i]-b)//a - k
    elif len(arr) == 1:
        arr[0]==1
    return

def a2b(arr):
    """Transform array of indices (1-based) to bitvector (0-based)."""
    n=0
    for i in arr: n |= 1<<(i-1)
    return n

def b2a(n):
    """Inverse of a2b(), used for debugging."""
    arr,i = [],1
    while n>0:
        b,n=n&1,n>>1
        if b: arr.append(i)
        i+=1
    return arr
    
def known_pat(n):
    """Check for patterns with known number of steps."""
    l = n.bit_length()
    if l>=3:
        #   [1, ....., n-1, n] => n steps needed
        if n & 1<<l-2 and n & 1: return l
    # this is for Testcase 26: [k,n-k,n] = [k,k+n%k,2k+n%k] + (n//k-2) steps
    if l>30:
        for k in range(2,10): # remember that bitvector is 0-based, not 1-based
            if n & 1<<(k-1) and n & 1<<l-1-k and (n == 1<<l-1|1<<l-1-k|1<<k-1):
                return l//k - 2 + iterateIt([k,k+l%k,2*k+l%k])
    return -1

def iterate(n):
    s=0
    while n>0:
        b,n=n&1,n>>1
        if b: s |=n
    return s
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input())

    a = list(map(int, input().rstrip().split()))

    result = iterateIt(a)

    fptr.write(str(result) + '\n')

    fptr.close()