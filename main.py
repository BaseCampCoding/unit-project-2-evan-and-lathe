import classes
import doclear
import sqlite3

print("WELCOME TO QUIZZER")


while True:
    name = input("What would you like to name your quiz?: ")
    correct_input = input("Your quiz is called " + name + " is this correct?: ")
    if correct_input.upper() == "YES":
        break
    elif correct_input.upper() == "NO":
        continue

# True/False questions
cb = sqlite3.connect("quizzes.db")
cur = cb.cursor()

cur.execute(
    """CREATE TABLE if not exists TFquestions(Prompt TEXT, Response TEXT, Answer TEXT) """
)

how_many_tf = input("How many True/False questions would you like? ")
how_many_tf = int(how_many_tf)
all_tf_questions = []
all_tf_answers = []
for i in range(how_many_tf):
    prompt_tf = input("What would you like the question to say? ")
    # response_tf = input( )
    answer_tf = input("What is the correct answer? ")
    tf_questions = classes.true_false(prompt_tf, None, answer_tf)
    all_tf_questions.append(tf_questions)
    all_tf_answers.append(answer_tf)


# Presenting quiz
Fin = input("Would you like to see the quiz? [Y/N] ")
Fin.upper()
if Fin == "Y":
    str(all_tf_questions)
for i in all_tf_questions:
    print(i)

for e in range(how_many_tf):
    answer = input("Answer: ")
    f = 0
    is_correct = answer == all_tf_answers[e]

    while f < how_many_tf:
        if answer == all_tf_answers[f]:
            print("Yes")
            f += 1
        else:
            print("No")
            f += 1

        


# how_many_num = input("How many numerical answer questions would you like?")

# how_many_multiple = input("How many multiple choice questions would you like?")

# how_many_fib = input("How many fill in the blank questions would you like?")
