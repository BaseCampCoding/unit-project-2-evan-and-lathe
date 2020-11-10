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

how_many_tf = input("How many True/False questions would you like")

how_many_num = input("How many numerical answer questions would you like?")