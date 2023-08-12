"""
If/else statements and inputs
input() will print out whatever you put between the parentheses, then wait for the user to give an answer.
if statements will check if the statement after if is true. If it is, the indented lines of code after will all run.
otherwise, the code will skip those lines and continue after the indented lines stop. If an else statement immediately
follows, the indented lines after else will only run if the if statement was false.

Based on the example below, write your own quiz question for the user to answer.
"""

correct_answer = '5'
answer = input('What is 2+3? ')
if answer == correct_answer:
    print('Wahoo you win!')
else:
    print('Try again!')
