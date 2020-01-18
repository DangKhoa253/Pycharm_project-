#let on game 
import random as rd 

#pick number:
def begin():
    x=int(input("Let pick random number: "))
    if x in range(1,301):
        print(x)
        return x 
    else:
        print("Select another number, the accepted number in range 1,300: ")
        return begin()
# Play game 

def result():
        y=rd.randrange(1,301)
        return y 
def setup(): 
    num=result()
    print("The result is: ",num)
    i=0  
    while i < 5:
        x=begin()
        if x == num:
            print("Congrats, the result is:", num, "at ", i + 1, "time(s)" )
            input1 = input("Do you want to play again? (Yes/No) ")
            if input1 == "Yes":
                return setup()
            else:
                print(" Thanks for joining our game")
                return  
        else:
            print("Huh, You're wrong", i + 1  ,"time(s).", "Let pick another number")
            i +=1
            continue
    if i+1 >= 5:
        print(" You lose this game, do you wanna play one more times? Yes/No")
        input2= input()
        if input2 == "Yes":
            return setup()
        else:
            print("Thanks for joining our game")

        

setup()
            
            

