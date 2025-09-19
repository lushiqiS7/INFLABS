r'''
Task Description:
In this task, you are going to design one program to check the popular characters
in a given string. You need to write one program to calculate the top 5 most 
frequent characters. The following are some hints that may help you design this program. 
	. String has a cool function that you can use to return a copy of the string 
     in which all case-based characters have been lowercased. 
	. To get the top 5 most frequent characters after sorting them, you need to 
     extract all the characters first and figure out one way to calculate the frequency 
     of each character. Then select the top 5 characters. 
	. The output must in the descending order of character frequency. If there are 
     characters with the same frequency, they must be printed in ascending ASCII order.
	. Print out the top 5 characters and their counts in the screen. (Your output should be in one line)

Running Examples:
C:\INF1002\Lab2\CountPopularChars>python CountPopularChars.py sdsERwweYxcxeewHJesddsdskjjkjrFGe21DS2145o9003gDDS
d:7,s:7,e:6,j:4,w:3
'''
import sys

def CountPopularChars(input_str=None):
    if input_str is None:
        if len(sys.argv) == 2:
            input_str = sys.argv[1]
        else:
            input_str = input("Enter a string: ")
    input_str = input_str.lower()
    freq = {}
    for char in input_str:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    sorted_freq = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    top5 = sorted_freq[:5]
    result = ','.join([f'{char}:{count}' for char, count in top5])
    print(result)
    

if __name__ == '__main__':
    CountPopularChars()
