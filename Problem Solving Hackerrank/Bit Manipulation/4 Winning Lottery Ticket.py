#The SuperBowl Lottery is about to commence, and there are several lottery tickets being sold, and each ticket is identified with a ticket ID. In one of the many winning scenarios in the Superbowl lottery, a winning pair of tickets is:
#Concatenation of the two ticket IDs in the pair, in any order, contains each digit from 0 to 9 at least once.
#For example, if there are 2 distinct tickets with ticket ID 129300455 and 56789,(129300455,56789) is a winning pair.
#NOTE: The ticket IDs can be concantenated in any order. Digits in the ticket ID can occur in any order.
#Your task is to find the number of winning pairs of distinct tickets, such that concatenation of their ticket IDs (in any order) makes for a winning scenario. Complete the function winningLotteryTicket which takes a string array of ticket IDs as input, and return the number of winning pairs.
#
#Input Format
#The first line contains n denoting the total number of lottery tickets in the super bowl.
#Each of the next n lines contains a string, where string on a ith line denotes the ticket id of the  ticket.
#
#Output Format
#Print the number of pairs in a new line.
#
#Sample Input 0
#5
#129300455 
#5559948277
#012334556 
#56789
#123456879
#
#Sample Output 0
#5

n = int(input())
p = [input().strip() for _ in range(n)]

fullMask = 2**10-1
cntMask = [0 for _ in range(fullMask+1)]

for s in p:
    mask = 0
    for c in s:
        mask |= 1 << (ord(c) - ord('0'))
    cntMask[mask] += 1

res = 0
for i in range(fullMask+1):
    for j in range(i+1, fullMask+1):
        if i | j == fullMask:
            res += cntMask[i] * cntMask[j]

res += cntMask[fullMask] * (cntMask[fullMask]-1) / 2
print(int(res))