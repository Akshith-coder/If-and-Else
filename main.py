''''
If and else is used when you want to execute a code only if a certain condition is satisfied.

This is basically decision making in python

When the condition for if is false, the program ends or it moves on to the else statement. 

An if statement does not require to be paired with an else statement. You can have only one else statement paired with a if statement

The elif is short for else if. It allows us to check for multiple expressions.

If the condition for if is False, it checks the condition of the next elif block and so on. You can use as many elif statements as you want in your if and else statement. 
'''
a = 200
b = 200
if b >= a:
	print("b is greater than or equal to a")
elif a == b:
	print("a is equal to b")