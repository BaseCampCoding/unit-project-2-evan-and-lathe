import classes
import doclear
import sqlite3
import json
import sys

con = sqlite3.connect("quizdb.db")
cur = con.cursor()

print("WELCOME TO QUIZZER")


all_tf_questions = []
all_tf_answers = []
all_num_questions = []
all_num_answers = []

while True:
    name = input("What would you like to name your quiz?: ")
    correct_input = input("Your quiz is called " + name + " is this correct?: ")
    if correct_input.upper() == "YES":
        break
    elif correct_input.upper() == "NO":
        continue

doclear.clear()

cur.execute("CREATE TABLE if not exists Quizes(Question TEXT)")
cur.execute(
    'INSERT INTO Quizes VALUES("True/False: The answer is either true or false")'
)
cur.execute('INSERT INTO Quizes VALUES("Numerical: The answer is a number")')
cur.execute(
    'INSERT INTO Quizes VALUES("Fill-In-The-Blank: This answer could be anything")'
)
cur.execute(
    'INSERT INTO Quizes VALUES("Multiple Choice: You choose from a set of answers what it could be")'
)
cur.execute("SELECT * FROM Quizes")
for i in cur.execute("SELECT * FROM Quizes"):
    print(i[0])

template = input("Would you like to use a template?: ")
if template.upper() == "YES":
    choice = input(
        "Type the number of which template you want. \n"
        "1) 10 multiple choice questions \n"
        "2) 5 fill in the blank questions \n"
        "3) 6 True/False questions. \n"
        "Choice:  "
    )
    if choice == "3":
        for i in range(6):
            prompt_tf = input("What would you like the true/false question to say? ")
            while True:
                print("[Please input either True or False for your answer.]")
                answer_tf = input("What is the correct answer? ")
                if answer_tf == "True":
                    break
                if answer_tf == "False":
                    break
            all_tf_questions.append(prompt_tf)
            all_tf_answers.append(answer_tf)

        Fin = input("Would you like to see the quiz? [Y/N] ")

        doclear.clear()
        print("------" + name + "------")
        Fin.upper()
        if Fin == "Y":
            str(all_tf_questions)
        for i in all_tf_questions:
            print(i)

        for e in range(len(all_tf_answers)):
            answer = input("Answer: ")
            if answer == all_tf_answers[e]:
                print("Yes")
            else:
                print("No")
        sys.exit("Stop")
        # tf_questions = classes.true_false(prompt_tf, None, answer_tf)
        all_tf_questions.append(prompt_tf)  # (prompt_Tf used to be tf_questions)
        all_tf_answers.append(answer_tf)

elif template.upper() == "NO":
    pass

# True/False questions
cb = sqlite3.connect("quizzes.db")
cur = cb.cursor()

# cur.execute(
#     """CREATE TABLE if not exists TFquestions(Prompt TEXT, Response TEXT, Answer TEXT) """
# )

how_many_tf = input("How many True/False questions would you like? ")
how_many_num = input("How any Numerical Questions would you like? ")
how_many_tf = int(how_many_tf)
how_many_num = int(how_many_num)

# all_tf_questions = []
# all_tf_answers = []
# all_num_questions = []
# all_num_answers = []
# # fill in the blank questions
while True:
    how_many_fb = input("How many fill in the blank questions would you like? ")
    try:
        int(how_many_fb)
    except:
        print("Please enter a numerical value")
        continue
    break
how_many_fb = int(how_many_fb)

# Multiple choice questions
while True:
    how_many_mc = input("How many multiple choice questions would you like? ")
    try:
        int(how_many_mc)
    except:
        print("Please enter a numerical value")
        continue
    break
how_many_mc = int(how_many_mc)

all_mc_questions = []
all_mc_choices = []
all_mc_answers = []
object_mc_questions = []

all_fb_questions = []
all_fb_answers = []
object_fb_questions = []
for i in range(how_many_fb):
    prompt_fb = input("What would you like the fill in the blank question to say? ")
    # response_fb = input( )
    answer_fb = input("What is the correct answer? ")
    fb_questions = classes.fill_blank(prompt_fb, None, answer_fb)
    all_fb_questions.append([fb_questions.prompt])
    all_fb_answers.append([fb_questions.answer])
    object_fb_questions.append([fb_questions])

all_tf_questions = []
all_tf_answers = []
all_num_questions = []
all_num_answers = []
for i in range(how_many_tf):
    prompt_tf = input("What would you like the true/false question to say? ")
    # response_tf = input( )
    while True:
        print("Please input either True or False for your answer.")
        answer_tf = input("What is the correct answer? ")
        if answer_tf == "True":
            break
        if answer_tf == "False":
            break
    # tf_questions = classes.true_false(prompt_tf, None, answer_tf)
    all_tf_questions.append(prompt_tf)  # (prompt_Tf used to be tf_questions)
    all_tf_answers.append(answer_tf)


for i in range(how_many_num):
    prompt_num = input("What would you like the numerical question to say? ")
    # response_tf = input( )
    while True:
        print("Please input a number for your answer.")
        answer_num = input("What is the correct answer? ")
        if answer_num.isnumeric() == True:
            break
    num_questions = classes.numerical(prompt_num, None, answer_num)
    all_num_questions.append(num_questions)
    all_num_answers.append(answer_num)


for i in range(how_many_mc):
    prompt_mc = input("What would you like multiple choice the question to say? ")
    # response_mc = input( )
    mc_choices = input("What are the answer choices (Including the correct answer): ")
    answer_mc = input("What is the correct answer: ")
    mc_questions = classes.multiple_choice(prompt_mc, None, mc_choices, answer_mc)
    all_mc_choices.append([mc_questions.choices])
    all_mc_answers.append([mc_questions.answer])
    all_mc_questions.append([mc_questions.prompt])
    object_mc_questions.append(mc_questions)


######### Presenting quiz ##########


Fin = input("Would you like to see the quiz? [Y/N] ")
doclear.clear()
print("------" + name + "------")
print("Answer the questions in chronological order ")
print(" ")

Fin.upper()
if Fin == "Y":
    str(all_tf_questions)
for i in all_tf_questions:
    print(i + " True or False?")

# if Fin == "Y":
#     str(all_num_questions)
# for i in all_num_questions:
#     print(i)

for e in range(how_many_tf):
    answer = input("Answer: ")
    if answer == all_tf_answers[e]:
        print("Correct")
        print(" ")
    else:
        print("Incorrect")
        print(" ")


# Presenting fill in the blank questions
for s in all_fb_questions:
    print(*s)

for index, i in enumerate(all_fb_answers):
    fb_user_input = input("\nAnswer:")
    if fb_user_input in i:
        print("That's right")
        print("--------")
    else:
        print("Incorrect")

    if Fin == "Y":
        str(all_num_questions)
    for i in all_num_questions:
        print(i)

for a in range(how_many_num):
    answer = input("Answer: ")
    if answer == all_num_answers[a]:
        print("Yes")
    else:
        print("No")

for i, (question, choice) in enumerate(zip(all_mc_questions, all_mc_choices)):
    print("--------")
    print(*question)
    print(*choice)
    print("--------")
    print(" ")

for index, q in enumerate(all_mc_answers):
    mc_user_input = input("\nAnswer:")
    if mc_user_input in q:
        print("That's right")
        print("--------")
    else:
        print("Incorrect")
