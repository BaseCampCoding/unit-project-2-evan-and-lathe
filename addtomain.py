import classes
import doclear
import sqlite3
import pprint

# # fill in the blank questions
while True:
    how_many_fb = input("How many fill in the blank questions would you like? ")
    try:
        int(how_many_fb)
    except:
        print("Please enter a numerical value")
        continue
    break

all_fb_questions = []
all_fb_answers = []
object_fb_questions = []
for i in range(how_many_fb):
    prompt_fb = input("What would you like the question to say? ")
    # response_fb = input( )
    answer_fb = input("What is the correct answer? ")
    fb_questions = classes.fill_blank(prompt_fb, None, answer_fb)
    all_fb_questions.append([fb_questions.prompt])
    all_fb_answers.append([fb_questions.answer])
    object_fb_questions.append([fb_questions])


# Multiple choice questions
while True:
    how_many_mc = input("How many multiple choice questions would you like? ")
    try:
        int(how_many_mc)
    except:
        print("Please enter a numerical value")
        continue
    break

all_mc_questions = []
all_mc_choices = []
all_mc_answers = []
object_mc_questions = []

for i in range(how_many_mc):
    prompt_mc = input("What would you like the question to say? ")
    # response_mc = input( )
    mc_choices = input("What are the answer choices (Including the correct answer): ")
    answer_mc = input("What is the correct answer: ")
    mc_questions = classes.multiple_choice(prompt_mc, None, mc_choices, answer_mc)
    all_mc_choices.append([mc_questions.choices])
    all_mc_answers.append([mc_questions.answer])
    all_mc_questions.append([mc_questions.prompt])
    object_mc_questions.append(mc_questions)

# # # presenting quiz
print("Here is your quiz. \nAnswer the questions in chronological order ")

for s in all_fb_questions:
    print(*s)


for index, i in enumerate(all_fb_answers):
    fb_user_input = input("\nAnswer:")
    if fb_user_input in i:
        print("That's right")
        print("--------")
    else:
        print("Incorrect")

for s in all_mc_questions:
    print(*s)
    print(" ")
    for c in all_mc_choices:
        print(*c)


for index, q in enumerate(all_mc_answers):

    mc_user_input = input("\nAnswer:")
    if mc_user_input in q:
        print("That's right")
        print("--------")
    else:
        print("Incorrect")
