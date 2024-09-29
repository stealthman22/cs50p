emoticon = "v.v"


def main():
    global emoticon
    say("Is anyone there?")
    who = input("Anyone?")
    if "Joe" in who:
        emoticon = ":D"
        say("Yess it's Joey,my favourite person")
        say("Howdy Friend!")
    else:
        say("Oh hi")


# I want to understand why this code runs correctly when i add the else statement, else it just doesn't print any side effects


def say(phrase):
    print(phrase + " " + emoticon)


main()
