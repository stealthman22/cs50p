# print("What's your name? ")
# Ask user for their name
# name = input("What's your name? ")
# Say hello to user
# The + sign here is called concatenation
# print("Hello " +  name)

# Another way
# When you pass multiple arguments into print,
# It automatically creates a space.
# print("Hello,", name)

# print("Hello, ", end="")
# print(name)


# let's play with sep
# print("Hello, ", name,  sep="\n")


# print("How are you 'human'?")

# Escape Character
# print("How are you \"human\"?")

# format string (fstring)
# print(f"Hello, {name}")

# Formatting Strings how we want
# Remove whitespace from strings and reassigning name.
# name = name.strip()


# Capitalize users names
# name = name.capitalize()

# Capitalize all first characters
# name= name.title()
# print(f"Hello, {name}")

# Capitalize all first characters and remove whitespaces
# name = name.capitalize().title()


# We can make it even tighter  and cuter
# name = input("What's your age? ").strip().title()


# Split user's name into first name and last name
# Try to remember js's equivalent of this.
# first, last= name.split(" ")
# print(f"Hello, {first}")


# Creating our own hello funtion
# mine
# def hello():
#  name = input("What's your name?  ").strip().title()
#  print(f"Hello {name}")


# David solutuon
# def hello(to="world"):
# To is a parameter here
# print("hello, ", to)

# name is the argumetn of the function and it is copied into to
# hello()
# name = input("What's your name?  ").title().strip()
# hello(name)


def main():
    hello()
    name = input("What's your name? ")
    hello(name)


def hello(to="world"):
    print("hello, ", to)


main()


"""
This can also be used 
for multiline comments
"""

# New line
