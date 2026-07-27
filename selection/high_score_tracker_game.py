# start an intentional infinte loop using while True:
# inside the loop, ask the user to enter a game score next to the flashing cursor
# if they type the word "stop" (clean it up with .strip().lower()), print "Game session ended!" and use break statement to shut down the loop
# otherwise, cast their input into an int, check if the score is greater than 100, and print either "wow!"That's a new high score!" or "Good try, keep playing!" based on the value.


while True:
    score_input = input("Enter your game score (or type 'stop' to end): ").strip().lower()

    if score_input == "stop":
        print("Game session ended!")
        break

    try:
        score = int(score_input)
        if score > 100:
            print("Wow! That's a new high score!")
        else:
            print("Good try, keep playing!")
    except ValueError:
        print("Please enter a valid number or 'stop' to end the session.")