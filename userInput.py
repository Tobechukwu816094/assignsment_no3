"""
program that requires username input,
three numbers that requires to sum,
      divide and multiply first and second of each.
"""
username = input('username:')
  # store inputs numbers
num1 = float(input("enter first number:"))
num2 =float( input("enter second number:"))
num3 = float(input("enter third number:"))
  # Add two numbers
sum = num1 + num2
division = num1 / num2
multiplication =  num1 * num2

 #display the sum , quotient, product.
print('the sum of {0} and {1} is {2}'.format(num1,num2,sum))
print('the division of {0} and {1} is {2}'.format(num1,num2,division))
print('the multiplication of {0} and {1} is {2}'.format(num1,num2,multiplication))












