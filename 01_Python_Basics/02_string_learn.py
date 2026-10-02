name =input('Enter ur name:')
print('Hey'+ name ) 
''' 
Here when we use + to concatenate text and variable since they would make a single argument  it will not add space 
automatically a space would not be added and hence
 we need to add manually a space in the text 
'''
print('Hey',name)
'''
Here when we use , as separator it tells the interpreter that more than one argument is being passed 
passed
and as the syntax of print function says that the sepaator of arguments by default is a single space
Hence in the output we get a space added automatically
'''
print('Hey')
print(name)
'''
Here we will get output in 2 lines since 2 print functions called 
Also in the print function syntax we have the end temp variable given the value of \n which tells it to move to next line
syntax of print function is print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
'''
print('Hey',end='')
print(name)
'''
here we have used the end temp variable to change the default value of \n to '' which tells it not to move to next line
and hence the output will be in a single line
'''
print("'Hey'")
print("\"Hey\"") # we add \ before the " to tell the interpreter that it is not the end of the string and it is a part of the string
'''
above shows the use of escape sequence to print the single quote and double quote in the output
'''
#use of f strings i.e. formatted string literals
print(f"hey, {name}")
'''
Here we have used f strings to print the variable name in the output
f strings are used to format the string and it is a new feature in python 3.
'''


#string methods
name  = input('Enter ur name:')
name = name.strip() #removes the leading and trailing spaces from the string
name = name.upper() #converts the string to uppercase

print(f"hey, {name}")
# above we were calling methods separately but we can also concatenate them in single line and 
# in python operation will be performed from left to right and hence we can write the above code as below
name  = input('Enter ur name:').strip().upper()
print(f"hey, {name}")
#here first the input will be taken then the leading and trailing spaces will be removed and then the string will be converted to uppercase
first=name.split(",") # here we are using split method to split the string into two parts and assign them to first and last variables
print(f"hey {first}")
print(type(first))  # class is list
one,two= name.split(",") # here we are using split method to split the string into two parts and assign them to one and two variables
print(one, two, type(one)) #class is str
