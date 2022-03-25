#You are given a list of N lowercase English letters. For a given integer K,
#you can select any K indices (assume 1-based indexing) with a uniform probability from the list.
#Find the probability that at least one of the K indices selected will contain
#the letter: 'a'.
#Input Format
#The input consists of three lines. The first line contains the integer N,
#denoting the length of the list. The next line consists of N space-separated
#lowercase English letters, denoting the elements of the list.
#The third and the last line of input contains the integer K, denoting the number
#of indices to be selected.
#Output Format
#Output a single line consisting of the probability that at least one of the K indices
#selected contains the letter:'a'.
#Note: The answer must be correct up to 3 decimal places.
#Sample Input
#4 
#a a c d
#2
#Sample Output
#0.8333
#Explanation
#All possible unordered tuples of length 2 comprising of indices from 1 to 4 are:
#(1,2),(1,3),(1,4),(2,3),(2,4),(3,4)
#Out of these 6 combinations,5 of them contain either index 1 or index 2 which
#are the indices that contain the letter 'a'.
#Hence, the answer is 5/6.

from itertools import combinations
n = int(input())

alphabets = list(map(str, input().split(' ')))
alphabets.insert(0,0)
k = int(input())
a_indices = set([i for i in range(0,len(alphabets)) if alphabets[i]=='a'])
k_indices = [i for i in range(1,n+1)]
poss_out = list(combinations(k_indices,k))

fav_out =0

for item in poss_out:
    if len(a_indices.intersection(set(item)))>0:
        fav_out+=1


print(round(fav_out/len(poss_out),4))
