def cal(a,b):
    while True:
        print("ENTER \nFor ADDITION : add \nFor SUBTRACTION  : sub \nFor MULTIPLICATION : multiply \nFor DIVISION : divide ")
        c = input("Want to :").lower()
        if c == "add":
            print(a+b)
            return
        if c == "sub":
            print(a-b)
            return
        if c == "multiply":
            print(a*b)
            return
        if c == "divide":
            print(a/b)
            return
        else:
            print("Please Enter Correct Keyword:")
        
        
a = int(input("First Number :"))
b = int(input("Second Number :"))
cal(a,b)