# x = 1
# y =2
# z= x + y
# print( z)

# Trying David's next point myself
# x =  int( input("What is your first numer? "))
# y=  int(input("What is your second numer? ")) 
# z = x + y 
# print( x + y)

#David's Solution
# x = input("What is your first numer? ")
# y=input("What is your second numer? ")

# z = int(x) + int(y)
# print( z)

#  Let'd do it with floats
# x =  float( input("What is your first numer? "))
# y=  float(input("What is your second numer? ")) 
# z = x + y 
# print( x + y)



# x =  float( input("What is your first numer? "))
# y=  float(input("What is your second numer? ")) 

# z=round(x +y)
# print(f"{z}")

# Let's format the string with commas
# print(f"{z:,}")

# Division and rounding to 2 decimal places
# z=round(x / y, 2)
# Rounding to 2 decimal places  with fstring formatting.
# z = x/y
# print(f"{z:.2f}")
# print(z)



#  New Function

def main():
 x= int(input("What's X?"))
 squared(x)



def squared(square):
 num_squared = square * square
 return num_squared
	
main()

