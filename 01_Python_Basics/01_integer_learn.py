x=input("whats x: ")
y=input("whats y: ")
print(x+y) # here we are adding the two integers and hence the output will be the sum of the two integers
#if x=1,y=2 then the output will be 3 since the input function takes the input as string and we are converting it to integer using int() function and hence the + operator will add the two integers
#use of type conversion here now we will convert the input to integer using int() function and then add the two integers
x=int(input("whats x: "))
y=int(input("whats y: "))
print(x+y) # here we are adding the two integers and hence the output will be the sum of the two integers   

#float
x=float(input("whats x: "))
y=float(input("whats y: "))
print(x+y) # here we are adding the two floats and hence the output will be the sum of the two floats

#now if we want the output to be rounded off
z=round(x+y) # here we are rounding off the sum of the two floats and hence the output will be the rounded off value of the sum of the two floats
#but if we want the output to be rounded off to 2 decimal places then we can use the round() function with 2 as the second argument
z=round(x+y,2) # here we are rounding off the sum of the two floats to 2 decimal places and hence the output will be the rounded off value of the sum of the two floats to 2 decimal places 

#now if I want to add a comma separator in the output when inputs are bigger number then we would use the format() function and use the comma separator in the format string
x=float(input("whats x: "))   
y=float(input("whats y: "))
z=round(x+y)
print(f"{z:,}") # here we are adding a comma separator in the output when inputs are bigger number
x=float(input("whats x: "))   
y=float(input("whats y: "))
z=x/y
print(f"{z:,.2f}") # here we are adding a comma separator in the output when inputs are bigger number and also rounding off to 2 decimal places,
                    #it works similar to round(z,2)

