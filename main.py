import random

def ranm_generator():
    return random.randint(0,2)

number=int(input('Enter your choice Number: '))
answer=ranm_generator()

if number==answer:
    print('\n\nYour answer is correct. You WIN')
else:
    print('\n\nYou LOSE')
    print(f'\nThe correct answer was {answer}')