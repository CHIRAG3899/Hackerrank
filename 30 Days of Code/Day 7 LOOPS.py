#Task
#Given a string,S , of length N that is indexed from 0 to N-1 ,
#print its even-indexed and odd-indexed characters as 2 space-separated
#strings on a single line .
#Note: 0 is considered to be an even index.
#Sample Input
#2
#Hacker
#Rank
#Sample Output
#Hce akr
#Rn ak

n = int(input())  # number of strings
for _ in range(n):
    string = input()
    print(string[::2], string[1::2])
