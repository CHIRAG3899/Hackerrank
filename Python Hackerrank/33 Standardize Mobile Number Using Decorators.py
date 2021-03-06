#Let's dive into decorators! You are given N mobile numbers. Sort them in ascending
#order then print them in the standard format shown below:
#+91 xxxxx xxxxx
#The given mobile numbers may have +91, 91 or 0 written before the actual 10 digit
#number. Alternatively, there may not be any prefix at all.
#Input Format
#The first line of input contains an integer N, the number of mobile phone numbers.
#N lines follow each containing a mobile number.
#Output Format
#Print N mobile numbers on separate lines in the required format.
#Sample Input
#3
#07895462130
#919875641230
#9195969878
#Sample Output
#+91 78954 62130
#+91 91959 69878
#+91 98756 41230

def wrapper(f):
    def fun(l):
        new_list=[]
        for i in l:
            new_list.append(' '.join(("+91",i[len(i)-10:len(i)-5],i[len(i)-5:len(i)])))
        f(new_list)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 


