print('Press 1 for plus')
print('Press 2 for subtract')
print('Press 3 for multiply')
print('Press 4 for divide')

userInput = int(input('Please Enter :'))
firstNumber = int(input('Please Enter First Number :'))
secondNumber = int(input('Please Enter Secound Number :'))

if userInput == 1:
    result = firstNumber+secondNumber
    operator = '+'
elif userInput == 2:
    result = firstNumber-secondNumber
    operator = '-'
elif userInput == 3:
    result = firstNumber*secondNumber
    operator = '*'
elif userInput == 4:
    result = firstNumber/secondNumber
    operator = '/'
else :
    print('You must enter 1 2 3 4')
    result = None

if result is not None:
    print('{} {} {} = {}'.format(firstNumber,operator,secondNumber,result))