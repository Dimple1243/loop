i=5
while 1<=i:
    guess=int(input("enter the number"))
    if guess==10:
        print("correct")
    elif guess!=10:
        print("your guess is too less from the guess number")  
    else:
        print("your guess is too high")  
        break
    i-=1  
    print("you have only" ,i, "chance")













