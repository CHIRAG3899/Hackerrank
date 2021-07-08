#Find the greatest product of K consecutive digits in the N digit number.
#Input Format
#First line contains T that denotes the number of test cases.
#First line of each test case will contain two integers N & K.
#Second line of each test case will contain a N digit integer.
#Output Format
#Print the required answer for each test case.
#Sample Input 0
#2
#10 5
#3675356291
#10 5
#2709360626
#Sample Output 0
#3150
#0
#Explanation 0
#For 3675356291 and selecting K=5 consequetive digits, we have 36753,67356,53562,75356,35629 and 56291. Where 6 X 7 X 5 X 3 X 5 gives maximum product as 3150
#For 2709360626,0  lies in all selection of 5 consequetive digits hence maximum product remains 0

def largest_prod_in_a_series(l, k): # n is a string
    res = 0
    starting_slice = 0
    end_slice = k
    s = ''
    while end_slice <= len(l):
        s = l[starting_slice:end_slice]
        starting_slice += 1
        end_slice += 1
        if '0' in s:
            continue
        num = int(s)
        prod = 1
        while num > 0:
            r = num % 10 #taking out last digit
            num = num // 10 #taking out all digits except the last one
            prod = prod * r
        if res < prod:
            res = prod
    return res


t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ') # k consecutive digits, in a n digit number.
    n,k = [int(n),int(k)] # converted into integers
    number = input().strip() # the number to perform operations with 
    print(largest_prod_in_a_series(number, k))
