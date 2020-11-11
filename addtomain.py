import classes
import doclear
import sqlite3

# # fill in the blank questions
# how_many_fb = input("How many fill in the blank questions would you like? ")
# how_many_fb = int(how_many_fb)
# all_fb_questions = []
# all_fb_answers = []
# for i in range(how_many_fb):
#     prompt_fb = input("What would you like the question to say? ")
#     # response_fb = input( )
#     answer_fb = input("What is the correct answer? ")
#     fb_questions = classes.fill_blank(prompt_fb, None, answer_fb)
#     all_fb_questions.append(fb_questions.prompt)
#     all_fb_answers.append(fb_questions.answer)

# # presenting quiz
# print("Here is your quiz. \nAnswer the questions in chronological order ")

# for i in all_fb_answers:
#     print(all_fb_questions)
#     fb_user_input = input("\nAnswer:")
#     if fb_user_input == i:
#         print("That's right")
#         print("--------")
#     else:
#         print("Incorrect")

# Multiple choice questions

how_many_mc = input("How many fill in the blank questions would you like? ")
how_many_mc = int(how_many_mc)
all_mc_questions = []
all_mc_answers = []
for i in range(how_many_mc):
    prompt_mc = input("What would you like the question to say? ")
    # response_mc = input( )
    choices_mc = input("What are the answer choices ")
    answer_mc = input("What is the correct answer")
    mc_questions = classes.multiple_choice(prompt_mc, None, choices_mc, answer_mc)
    all_mc_questions.append(mc_questions.prompt)
    all_mc_answers.append(mc_questions.answer)