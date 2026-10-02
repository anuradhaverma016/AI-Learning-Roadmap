def main():
    x= int(input("Whats x?"))
    print("square of x is: " , square(x))

#if we keep it like this it errors out saying square is not defined.
#so what we are going to do is we will create a function named square which returns the square of any number passed

def square(number) :
    return number * number
or
    return number ** 2
or
    return pow(number, 2)

#we can use either of the above three methods to return the square of a number. Now we can call the main function to execute the program.

main()  