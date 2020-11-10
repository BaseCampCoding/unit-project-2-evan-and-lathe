import classes
import doclear

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

#True/False questions
how_many_tf = input("How many True/False questions would you like?")
prompt_tf = input("What would you like the question to be?")
#response_tf = input( )
answer_tf = input("What is the correct answer?")

tf_questions = true_false(prompt_tf, input(), answer_tf)



how_many_num = input("How many numerical answer questions would you like?")






