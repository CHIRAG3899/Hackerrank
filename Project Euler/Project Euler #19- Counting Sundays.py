#You are given the following information, but you may prefer to do some research for yourself.
#
#1 Jan 1900 was a Monday.
#Thirty days has September,
#April, June and November.
#All the rest have thirty-one,
#Saving February alone,
#Which has twenty-eight, rain or shine.
#And on leap years, twenty-nine.
#
#A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
#
#How many Sundays fell on the first of the month between two dates(both inclusive)?
#
#Input Format
#The first line contains an integer T, i.e., number of test cases.
#Each testcase will contain two lines
#Y1 M1 D1 on first line denoting starting date.
#Y2 M2 D2 on second line denoting ending date.
#
#Output Format
#
#Print the values corresponding to each test case.
#
#Sample Input
#
#2
#1900 1 1
#1910 1 1
#2000 1 1
#2020 1 1
#Sample Output
#
#18
#35
#Explanation
#
#For testcase 1, we have the following sundays :-
#1 April 1900
#1 July 1900
#1 September 1901
#1 December 1901
#1 June 1902
#1 February 1903
#1 March 1903
#1 November 1903
#1 May 1904
#1 January 1905
#1 October 1905
#1 April 1906
#1 July 1906
#1 September 1907 
#1 December 1907
#1 March 1908
#1 November 1908
#1 August 1909

def confirm_dates(start, end):
    dates = [start, end]
    if date_error(start, end):
        new_dates = exchange(start, end)
        dates = [new_dates[0], new_dates[1]]
    return dates


def date_error(start, end):
    if start[0] > end[0]:
        return True
    elif start[0] == end[0]:
        if start[1] > end[1]:
            return True
        elif start[1] == end[1]:
            if start[2] > end[2]:
                return True
    return False


def exchange(start, end):
    dates = [end, start]
    return dates


def is_sunday(year, month, day):
    if month < 3:
        month += 12
        year -= 1
    dv = year // 100
    y = year % 100
    d = (y + (y // 4) + (dv // 4) - (2 * dv) + ((26 * (month + 1)) // 10) + day - 1) % 7
    return d == 0


for _ in range(int(input())):
    start_date = list(map(int, input().split()))
    end_date = list(map(int, input().split()))
    dates = confirm_dates(start_date, end_date)
    start_date = dates[0]
    end_date = dates[1]
    
    count = 0
    while True:
        if start_date[2] == 1:
            if is_sunday(start_date[0], start_date[1], start_date[2]):
                count += 1
        
        start_date[2] = 1
        start_date[1] += 1
        if start_date[1] > 12:
            start_date[1] = 1
            start_date[0] += 1
            
        if date_error(start_date, end_date):
            break
    
    print(count)