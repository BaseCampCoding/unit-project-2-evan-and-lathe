import classes
import doclear
import sqlite3
# fill in the blank questions
how_many_fb = input("How many fill in the blank questions would you like? ")
how_many_fb = int(how_many_fb)
all_fb_questions = []
all_fb_answers = []
for i in range(how_many_fb):
    prompt_fb = input("What would you like the question to say? ")
    # response_fb = input( )
    answer_fb = input("What is the correct answer? ")
    fb_questions = classes.fill_blank(prompt_fb, None, answer_fb)
    all_fb_questions.append(fb_questions.prompt)
    all_fb_answers.append(fb_questions.answer)

# presenting quiz
print("Here is your quiz")

for question in all_fb_questions:
    fb_user_question = input(fb_questions.prompt + "\n")
    if fb_user_question == fb_questions.answer:
        print ("That's right")
    else:
        print("no") 