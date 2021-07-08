#A palindromic number reads the same both ways. The smallest 6 digit palindrome made from the product of two 3-digit numbers is 101101=143 X 707.
#Find the largest palindrome made from the product of two 3-digit numbers which is less than N.
#Input Format
#First line contains T that denotes the number of test cases. This is followed by T lines, each containing an integer, N.
#Output Format
#Print the required answer for each test case in a new line.
#Sample Input 0
#2
#101110
#800000
#Sample Output 0
#101101
#793397
#Explanation 0
#101101 is product of 143 and 707.
#793397 is product of 869 and 913.

def isPalin(num):
    num_st = str(num)
    return True if num_st == num_st[::-1] else False

ls = set(i*j for i in range(100,1000) for j in range(100,1000) if isPalin(i*j))

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    m = max(i for i in ls if i<n)
    print(m)
