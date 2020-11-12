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

cur.execute('CREATE TABLE if not exists Quizes(Question TEXT)') 
cur.execute('INSERT INTO Quizes VALUES("True/False: The answer is either true or false")')
cur.execute('INSERT INTO Quizes VALUES("Numerical: The answer is a number")')
cur.execute('INSERT INTO Quizes VALUES("Fill-In-The-Blank: This answer could be anything")')
cur.execute('INSERT INTO Quizes VALUES("Multiple Choice: You choose from a set of answers what it could be")')
cur.execute("SELECT * FROM Quizes")
for i in cur.execute("SELECT * FROM Quizes"):
    print(i[0])

template = input("Would you like to use a template?: ")
if template.upper() == "YES":
    choice = input("Type the number of which template you want. \n"
        "1) 10 multiple choice questions \n"
        "2) 5 fill in the blank questions \n"
        "3) 6 True/False questions. \n"
        "Choice:  ")
    if choice == "3":
        for i in range(6):
            prompt_tf = input("What would you like the true/false question to say? ")
            while True: 
                print("Please input either True or False for your answer.")
                answer_tf = input("What is the correct answer? ")
                if answer_tf == "True":
                    break
                if answer_tf == "False":
                    break
            all_tf_questions.append(prompt_tf) 
            all_tf_answers.append(answer_tf)

        Fin = input("Would you like to see the quiz? [Y/N] ")
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

elif template.upper() == "NO":
    pass

# True/False questions
cb = sqlite3.connect("quizzes.db")
cur = cb.cursor()

cur.execute(
    """CREATE TABLE if not exists TFquestions(Prompt TEXT, Response TEXT, Answer TEXT) """
)

how_many_tf = input("How many True/False questions would you like? ")
how_many_num = input("How any Numerical Questions would you like? ")
how_many_tf = int(how_many_tf)
how_many_num = int(how_many_num)

# all_tf_questions = []
# all_tf_answers = []
# all_num_questions = []
# all_num_answers = []

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
    all_tf_questions.append(prompt_tf) #(prompt_Tf used to be tf_questions)
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

# Presenting quiz
Fin = input("Would you like to see the quiz? [Y/N] ")
print("------" + name + "------")
Fin.upper()
if Fin == "Y":
    str(all_tf_questions)
for i in all_tf_questions:
    print(i)

if Fin == "Y":
   str(all_num_questions)
for i in all_num_questions:
    print(i)

for e in range(how_many_tf):
    answer = input("Answer: ")
    if answer == all_tf_answers[e]: 
        print("Yes")
    else:
        print("No")


for a in range(how_many_num):
    answer = input("Answer: ")
    if answer == all_num_answers[a]: 
        print("Yes")
    else:
        print("No")


# cur.execute('CREATE TABLE Numerical("Questions" TEXT, "Answers" TEXT)')
# cur.execute('CREATE TABLE TrueFalse("Questions" TEXT, "Answers" TEXT)')
# strquestions = json.dumps(all_tf_questions)
# stranswers = json.dumps(all_tf_answers)

# cur.execute('INSERT INTO Numerical VALUES(?, ?)', (strquestions, stranswers))
# cur.execute('SELECT Questions, Answers FROM Numerical')
# print(cur.fetchall())
# con.commit()




# how_many_num = input("How many numerical answer questions would you like?")

# how_many_multiple = input("How many multiple choice questions would you like?")

# how_many_fib = input("How many fill in the blank questions would you like?")
