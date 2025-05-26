# Cree un programa que le pida tres números al usuario y muestre el mayor.
number_one = int(input('Please add the first number: '))
number_two = int(input('Please add the second number: '))
number_three = int(input('Please add the third number: '))

if number_one >= number_two and number_one >= number_three:
    greatest = number_one
elif number_two >= number_one and number_two >= number_three:
    greatest = number_two
else:
    greatest = number_three
    
print(f'This is the greatest number: {greatest}')