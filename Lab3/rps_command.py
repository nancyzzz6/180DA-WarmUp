# reference https://www.reddit.com/r/Python/comments/o7j60z/ive_made_a_rock_paper_scissor_game_as_a_beginner/

import random
a = 'scissor'
b = 'rock'
c = 'paper'
print('welcome to the [ rock paper scissor ] game')
print('_____________________________________________________________________________')
print('Choose one of the option:\n* rock\n* paper\n* scissor')
print('_____________________________________________________________________________')
print('Enter exit if you want to stop playing this game')
answer = ''
while answer != 'exit':
    answer = input('enter your choice:\n')
    list = ['rock', 'paper', 'scissor']
    bot_answer = random.choice(list)
    print(f'your answer is {answer.upper()} and bot is ({bot_answer.upper()})')
    if answer==b and bot_answer=='paper':
        print('please try again')
    elif answer==a and bot_answer=='paper':
        print('you won')
    elif answer == c and bot_answer == 'paper':
        print('draw')
    elif answer == b and bot_answer == 'rock':
        print('draw')
    elif answer == a and bot_answer == 'rock':
        print('please try again')
    elif answer == c and bot_answer == 'rock':
        print('you won')
    elif answer == b and bot_answer == 'scissor':
        print('you won')
    elif answer == a and bot_answer == 'scissor':
        print('draw')
    elif answer == c and bot_answer == 'scissor':
        print('please try again')
    else:
        print('please enter the correct word')
    print('..............................................................................')