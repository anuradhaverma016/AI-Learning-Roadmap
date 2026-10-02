def main():
    name= input("whats your name:")
    hello(name)

def hello(to="world"):   #world is the default value of the parameter 'to'
    print("Hello,", to )

main()
'''
 in the above code, we have defined a function called main() that prompts the user for their name and then calls the hello() function with that name as an argument.
 The hello() function takes an optional parameter 'to' which defaults to "world" if no argument is provided in hello()
 It then prints a greeting message using the provided name or the default value.
 Finally, we call the main() function to execute the program.
 '''

#scope

def main():
    name= input("whats your name:")
    hello() 

def hello():
    print("Hello" , name)
      #this will give an error because 'name' is not defined in this scope