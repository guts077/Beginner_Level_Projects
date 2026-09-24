import random

words = ["ironman","thor","captainamerica","spiderman"]

word = random.choice(words)

gl =[]
wg = 0
max_g = 5

print("WELCOME TO HANGMAN !!")

while wg < max_g:
    show = ""
    for letter in word :
        if letter in gl:
            show += letter + ""
        else:
            show += "_"

    print("\n Word :",show)

    if "_" not in show:
        print("Congratulation You Won !!")
        break

    guess = input("Guess a Letter :").lower()

    if len(guess) != 1 or not guess.isalpha() :
        print("Must be one letter and alphabet")
        continue

    if guess in gl:
        print("You already guess that letter")
        continue
    gl.append(guess)

    if guess in word:
       print("correct letter")

    else:
        print("wrong guess")
        wg += 1

else:
    print("GAME OVER")    
