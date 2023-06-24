guess=5
n=18
while(guess):
    
        print("Enter a number :")
        take=input()
        if(take>n):
            print("Guess a smaller number")
            guess=guess-1
        elif(take<n):
            print("Guess a large number")
            guess=guess-1
        else:
            print("You win..")
            break

    
if(guess==0):
    print("You loss")