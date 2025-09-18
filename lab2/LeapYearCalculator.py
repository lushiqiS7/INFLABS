r'''
Task Description:
In this task, you will develop a program to compute all the leap years within a 
specified time period. The user will input a start year and an end year. 
Your task is to determine how many leap years are included in this period and 
print out those leap years. 

The rule for determining leap years is as follows:
	. A year is called a leap year, if the year is perfectly divisible by 4 - except 
       for years which are both divisible by 100 and not divisible by 400. The second 
       part of the rule effects century years. 
       For example; the century years 1600 and 2000 are leap years, 
       but the century years 1700, 1800, and 1900 are not. This means that three times 
       out of every 400 years there are 8 years between leap years.

More information about the leap years rule can be found online. 

Input: Two numbers (one is the start year, and another is the end year)
Output: The number of leap years and all the leap years (Your output should be in one line)
Note: In case of invalid input, print the message "Your input is invalid!".

Running Examples:

C:\INF1002\Lab2\LeapYearCalculator> python LeapYearCalculator.py 1989 2000
The number of Leap Years is 3, the Leap Years are 1992, 1996, 2000
'''

import sys
# write your code here
# you can use sys.argv[1] to get the first input argument.
# sys.argv[2] is the second argument, etc.

def LeapYearCalculator(start, end):
    try:
        start = int(start)
        end = int(end)

        if start > end:
            print("Your input is invalid!")
            return

        leaps = []
        for year in range(start, end + 1):
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                leaps.append(year)

        if leaps:
            leapyears = ', '.join(str(x) for x in leaps)
            print(f'The number of Leap Years is {len(leaps)}, the Leap Years are {leapyears}')
        else:
            print('The number of Leap Years is 0, the Leap Years are')
    except:
        print("Your input is invalid!")

if __name__ == '__main__':
    if len(sys.argv) == 3:
        LeapYearCalculator(sys.argv[1], sys.argv[2])
    else:
        print("Your input is invalid!")
