import random
playing = True
number = str(random.randint(0,10))

print("There will be a random number between 0 and 9")
print("The game ends when you guess it correctly")

while playing:
    guess = input("Give a good guess ")
    if number == guess:
        print("You won the game")
        print("The number was", number)
        break
    else:
        print("Try again")
