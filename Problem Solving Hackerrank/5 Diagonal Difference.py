#Given a square matrix,
#calculate the absolute difference between the sums of its diagonals.
#diagonalDifference takes the following parameter:

#int arr[n][m]: an array of integers
#Return

#int: the absolute diagonal difference

import math
import os
import random
import re
import sys


def diagonalDifference(arr):
    s1 = 0
    s2 = 0
    for i in range(len(arr)):
        s1 += arr[i][i]
        s2 += arr[i][len(arr)-i-1]
    s = s1-s2
    return abs(s)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
