import random

quessesTaken = 0

print('Hello! What is your name?')

myName = input()
number = random.randint(1,20)
print('Well ' + myName + ' I quess a number from 1 to 20')
for quessesTaken in range(6):
    print('Try to quess')
    quess = input()
    quess = int(quess)

    if quess < number:
        print('Number too small')

    if quess > number:
        print('Your number too big')

    if quess == number:
        break

if quess==number:
    quessesTaken = str(quessesTaken + 1)
    print('Well done'+ myName + 'your quess' + quessesTaken + 'try')

if quess != number:
    number = str(number)
    print('You loose,i quess'+ number + '.')