Python 3.12.5 (v3.12.5:ff3bc82f7c9, Aug  7 2024, 05:32:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
name = input("What is your name")
What is your nameJakub
print("Your name is: " +name)
Your name is: Jakub
print("Your name is: "name)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print("your name is: ",name)
your name is:  Jakub

age = input("Enter your age: ")
Enter your age: rover
age = int(age)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    age = int(age)
ValueError: invalid literal for int() with base 10: 'rover'
age = input("Enter your age: ")
Enter your age: 31
age = int(age)
age
31
age = int(input("Enter your age: "))
Enter your age: bike
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    age = int(input("Enter your age: "))
ValueError: invalid literal for int() with base 10: 'bike'
age = int(input("Enter your age: "))
Enter your age: 31
age = int(input("Enter your age: ")) print("Your age is: ", age)
SyntaxError: invalid syntax
age = int(input("Enter your age: ")), print("Your age is: ", age)
Enter your age: 31
Your age is:  31
>>> age = int(input("Enter your age: ")), print("Your age is: ", age)
Enter your age: bike
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    age = int(input("Enter your age: ")), print("Your age is: ", age)
ValueError: invalid literal for int() with base 10: 'bike'
>>> age = int(input("Enter your age: ")), print("Your age is: ", age)
Enter your age: 31
Your age is:  (31, None)
>>> age = int(input("Enter your age: ")), print("Your age is: ", age)
Enter your age: 33
Your age is:  (31, None)
>>> 
>>> 
>>> print( "Jakub" + "Python")
JakubPython
>>> 
>>> print(4* "Jakub")
JakubJakubJakubJakub
>>> print(4* "Jakub ")
Jakub Jakub Jakub Jakub 
>>> 
>>> name = (input("What is your name? "), age = int(input("What is your age? "))
...         
SyntaxError: '(' was never closed
>>> name = input("What is your name? "), age = int(input("What is your age? "))
...         
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
>>> crear
...         
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    crear
NameError: name 'crear' is not defined. Did you mean: 'repr'?
>>> repr
...         
<built-in function repr>
>>> name = input("What is your name? "), age = int(input("What is your age? "))
...         
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
>>> name == input("What is your name? "), age = int(input("What is your age? "))
...         
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
>>> name == input("What is your name? "), age == int(input("What is your age? "))
...         
What is your name? Jakub
What is your age? 31
(True, False)
>>> 
>>> 
>>> 
>>> 
>>> 
