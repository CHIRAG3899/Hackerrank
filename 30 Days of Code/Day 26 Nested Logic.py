#Task
#Your local library needs your help! Given the expected and actual return dates
#for a library book, create a program that calculates the fine (if any). The
#fee structure is as follows:
#If the book is returned on or before the expected return date, no fine will be
#charged (i.e.:fine =0 .
#If the book is returned after the expected return day but still within the same
#calendar month and year as the expected return date,fine= 15 Hackos X (the number
#of days late).
#If the book is returned after the expected return month but still within the
#same calendar year as the expected return date, the fine= 500 Hackos X (the number
#of months late).
#If the book is returned after the calendar year in which it was expected, there
#is a fixed fine of 10000 hackos.
#Example
#d1,m1,y1=12312014 returned date
#d2,m2,y2=112015 due date
#The book is returned on time, so no fine is applied.
#d1,m1,y1=112015 returned date
#d2,m2,y2=12312014 due date
#The book is returned in the following year, so the fine is a fixed 10000.
#Input Format
#The first line contains 3 space-separated integers denoting the respective day,
#,month and year on which the book was actually returned.
#The second line contains 3 space-separated integers denoting the respective day,
#month, and year on which the book was expected to be returned (due date).
#Output Format
#Print a single integer denoting the library fine for the book received as input.
#Sample Input
#STDIN       Function
#-----       --------
#9 6 2015    day = 9, month = 6, year = 2015 (date returned)
#6 6 2015    day = 6, month = 6, year = 2015 (date due)
#Sample Output
#45

d, m, y = map(int, list(input().split(' ')))
de, me, ye = map(int, list(input().split(' ')))

fine = 0

if y > ye:
    fine = 10000
elif y == ye:
    if m > me:
        fine = 500 * (m - me)
    elif m == me:
        if d > de:
            fine = 15 * (d - de)  
            
print(fine)
                                                                                        
