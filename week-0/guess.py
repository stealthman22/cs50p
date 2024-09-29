# guess = 10
# print(guess)


def main():
    guess = get_guess()
    if guess == 50:
        print("That is Correct!")
    else:
        print("Incorrect!")
    # print(f"Your guess is {int(guess)}")
    # print(guess)


def get_guess():
    guess = int(input("What's my favorite number? "))
    return guess


main()
