#  Nesting conditional statement
def main():
    difficulty = input("Difficult or Casual? ")
    players = input("Multiplayer or Single-Player? ")

    if difficulty == "Difficut":
        if players == "Multiplayer":
            recommend("Poker")
        elif players == "Single-Player":
            recommend("Klondike")
        else:
            print("Enter a valid set of players")
    elif difficulty == "Casual":
        if players == "Multiplayer":
            recommend("Hearts")
        else:
            recommend("Clock")
    else:
        print("Enter a valid   difficulty")


def recommend(game):
    print("You might like", game)
#next step

main()
#  Resuming 