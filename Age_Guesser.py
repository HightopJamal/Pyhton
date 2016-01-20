print("Let's play a game!")

Question = input("Do you want to play?(Y/N):")
if Question == ("Y"):
    print("Let's Play!!")
    def mathgame():
        print("Using math, I will guess your age!")
        input("Press Enter to continue:")

        shoesize = eval(input("What's Your Shoe size? ""Round to the nearest whole number:"))
        guessdraft1 = (shoesize * 5) + 50
        guessdraft2 = guessdraft1 * 20 + 1016
        brthyr = eval(input("What year were you born in?: "))
        divide = ((guessdraft2 - brthyr)%100 )
        answer = ("You are {0:0} Years old").format(divide)
        print(answer)
    mathgame()

else:
    print("I did'nt wanna play with you anyways")












