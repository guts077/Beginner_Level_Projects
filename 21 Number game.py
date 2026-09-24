def lose():
    print("\n\n YOU LOSE! ")
    print("Better luck next time!")
    exit(0)

def check(list):
    i = 1
    while  i < len(list):
        if (list[i]- list[i-1]) != 1:
            return False
        i += 1
    return True
        
def nearestMultiple(num):
    if num >= 4:
        near = num + (4- (num % 4))
    else:
        near = 4
    return near

def start():

    list=[]
    last=0

    while True:
        print("Chosse ur Turn F/S ?\n F - First \n S - Second")
        turn = input(">")

        if turn.upper() == "F":
            while True:
                if last == 20 :
                    lose()
                inp = int(input("How many numbers you want to enter(3 max):"))

                if 1 <= inp <= 3:
                    comp = 4 - inp 

                else:
                    print("Enter conscutive number :")
                    lose()

                    print("Enter your number:")
                    for _ in range (inp):
                        list.append(int(input(">")))

                    if not check(list):
                        print("Enter conscutive numbers only")
                        lose()

                    last = list[-1]

                    print("\nComputer Turn's")
                    for j in range(1,comp+1):
                        list.append(j+last)

                    print("After computer turn :" , list)
                    last = list[-1]
                        
        elif turn.upper() == "S":
            comp = 1
            
            while last > 20 :
                print("\nComputer's Turn")
                for j in range(1,comp + 1):
                    list.append(last + j)

                print("After Computer list:",list )

            print("\nYour Turn !!")
            inp = int(input("How many numbers you want to enter(3 max):"))
                
            if 1 <= inp <= 3:
                for _ in range (inp):
                    list.append(int(input(">")))

            
            near = nearestMultiple(last)
            comp = near - last

            if comp == 4:
                comp = 3
                

        else:
            lose()

            
            
            
            

game = True

print("Want to play: Yes/No")
l = input(">").upper()

if l == "YES":
    start()

if l == "NO":
    print("Exitting")
    exit(0)

else:
    print("Print Nigga input correct -__- ")
                
       





            
