print("WELCOME TO QUIZZER")


def funct1():
    while True: 
        name = input("What would you like to name your quiz?: ")
        correct_input = input("Your quiz is called " + name + " is this correct?: ")
        if correct_input.upper() == "Y":
            print("ok")
            break
        elif correct_input.upper() == "N":
            funct1()
funct1()
print("How are you?")