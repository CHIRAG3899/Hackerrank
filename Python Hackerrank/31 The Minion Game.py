#Kevin and Stuart want to play the 'The Minion Game'.
#Game Rules
#Both players are given the same string, S.
#Both players have to make substrings using the letters of the string S.
#Stuart has to make words starting with consonants.
#Kevin has to make words starting with vowels.
#The game ends when both players have made all possible substrings.
#Scoring
#A player gets +1 point for each occurrence of the substring in the string S.
#For Example:
#String S = BANANA
#Kevin's vowel beginning word = ANA
#Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.
#Your task is to determine the winner of the game and their score.
#Function Description
#Complete the minion_game in the editor below.
#minion_game has the following parameters:
#string string: the string to analyze
#Prints
#string: the winner's name and score, separated by a space on one line, or Draw if there is no winner
#Input Format
#A single line of input containing the string S.
#Note: The string S will contain only uppercase letters:[A-Z] .
#Sample Input
#BANANA
#Sample Output
#Stuart 12

def minion_game(string):
    s=string
    tot1=0
    tot2=0
    l=len(s)
    for i in range(l):
        if s[i] == "A" or s[i] == "E" or s[i] == "I" or s[i] == "O" or s[i] == "U":
            tot1 += l - i
        else:
            tot2 += l - i
    if tot1>tot2:
        print("Kevin",tot1)
    elif tot2==tot1:
        print("Draw")
    else:
        print("Stuart",tot2)

if __name__ == '__main__':
    s = input()
    minion_game(s)
