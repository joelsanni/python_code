print('python is an high level nprogramming language')
Name = input('please enter your name:')
num1 = int(input('enter tha first number:'))
num2 = int(input('enter the second number:'))
choice =input('pick an operation you will like to perform|(+,-,*,/)')
if choice =='+':
   print(f'{num1} + {num2} = {num1 + num2}')
elif choice == '-':
   print(f'{num1} - {num2} = {num1 - num2}')
elif choice == '*':
   print(f'{num1} x {num2} = {num1 * num2}')
elif choice == '/':
   print(f'{num1} / {num2} = {num1 / num2}')
else:
    print('invalid option')
print('End of program you did a good job')