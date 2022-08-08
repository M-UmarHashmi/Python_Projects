n = 18
guess = 0
print("Maximum number of gusses are 9")
while (guess<9):

    # print(guess+1)
    inp = int(input("Enter Your Guess\n"))
    guess = guess+1
    if inp < n:
        print("Increase Your number")
    if inp > n:
        print("Decrease Your number")
    if inp == n:
        print("You've got it right.")
        break
if guess >= 9 :
    print("Game is Over.")

