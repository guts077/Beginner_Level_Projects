import random 
print("Rock = R \nPaper = P \nSicssors = S")

list = ["R","P","S"]

P1 = random.choice(list)

user = input("PICK:").upper()

if user not in list:
    print("Invaild Pick")
else:
    print(f"computer pick", P1)

    if user == "S" and P1 == "P" or user == "R" and P1 == "S" or user == "P" and P1 == "R":
        print("You win")
    else:
        print("Computer Wins")