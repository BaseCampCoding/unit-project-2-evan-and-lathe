print("WELCOME TO QUIZZER")



while True:
    name = input("What would you like to name your quiz?: ")
    correct_input = input("Your quiz is called " + name + " is this correct?: ")
    if correct_input.upper() == "YES":
        print("ok")
        break
    elif correct_input.upper() == "NO":
        continue
            
print("How are you?")

how_many_tf = input("How many True/False questions would you like")

how_many_num = input("How many numerical answer questions would you like?")

how_many_multiple = input("How many multiple choice questions would you like?")

how_many_fib = input("How many fill in the blank questions would you like?")