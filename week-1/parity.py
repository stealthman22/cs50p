# x = int(input("What's x? "))

# if x % 2 == 0:
#     print("Even")
# else:
#     print("odd")


# My stuff
# if x % 2 == 0 and x > 0:
#     print("That's an even number")
# elif x % 2 != 0 and x > 0:
#     print("That's an odd number")
# elif x == 0 or type(x) == float:
#     print("Well that's  neither an even nor odd")
# else:
#     print("I do not understand your input")


def main():
    x = int(input("What's X? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")


def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


main()
