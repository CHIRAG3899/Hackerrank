#Task
#Given an array,na , of size n distinct elements, sort the array in ascending
#order using the Bubble Sort algorithm above. Once sorted, print the following
#3 lines:
#Array is sorted in numSwaps swaps.
#where numSwaps is the number of swaps that took place.
#First Element: firstElement
#where firstElements is the first element in the sorted array.
#Last Element: lastElement
#where lastElement is the last element in the sorted array.
#Hint: To complete this challenge, you will need to add a variable that keeps a
#running tally of all swaps that occur during execution.
#Example
#a=[4,3,1,2]
#original a: 4 3 1 2
#round 1  a: 3 1 2 4 swaps this round: 3
#round 2  a: 1 2 3 4 swaps this round: 2
#round 3  a: 1 2 3 4 swaps this round: 0
#In the first round, the 4 is swapped at each of the 4 comparisons, ending in
#the last position. In the second round, the 3 is swapped at 2 of the 3
#comparisons. Finally, in the third round, no swaps are made so the iterations
#stop. The output is the following:
#Array is sorted in 5 swaps.
#First Element: 1
#Last Element: 4


import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    num = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
                num += 1
    
    print('Array is sorted in {} swaps.'.format(num))
    print('First Element: {}'.format(a[0]))
    print('Last Element: {}'.format(a[n-1]))
