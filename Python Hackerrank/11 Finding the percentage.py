#The provided code stub will read in a dictionary containing key/value
#pairs of name:[marks] for a list of students. Print the average of the
#marks array for the student name provided, showing 2 places after the decimal.
#Input Format
#The first line contains the integer n, the number of students' records.
#The next n lines contain the names and marks obtained by a student, each
#value separated by a space. The final line contains query_name, the name
#of a student to query.

if __name__ == '__main__':
    
    def readScores(listOfStudents):
        line = list(input().split())
        avScore = sum(map(float, line[1:])) / 3
        name = line[0]
        listOfStudents[name] = avScore


    n = int(input())
    listOfStudents = dict()
    for i in range(n):
        readScores(listOfStudents)
    print('%.2f' % listOfStudents[input()])
