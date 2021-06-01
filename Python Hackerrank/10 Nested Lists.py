#Given the names and grades for each student in a class of N students,
#store them in a nested list and print the name(s) of any student(s) having
#the second lowest grade.

#Note: If there are multiple students with the second lowest grade,
#order their names alphabetically and print each name on a new line.

if __name__ == '__main__':
    s = []
    scorel = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        s.append([name, score])
        scorel.append(score)
        #find the second lowest score
    sl = sorted(set(scorel))[1]
    nl = [x[0] for x in s if x[1]==sl]
    print('\n'.join(i for i in sorted(nl)))
