# Proposal for Lathe and Evan's Quiz Creator

## Project Description and Motivation:
We will be writing a Quiz Creator; a program that does the grunt work of making a quiz for a user. The user will be asked what they want to name their quiz, what kind of questions they want to have (with the choices being multiple choice, True/False, numerical answer, and fill in the blank) or choose a premade template. This program will give the user a simple Q and A format to fill out what kind of quiz they want to create.

## Prior art
The first instance of this kind of thing that comes to mind is Google Forms. When filling out a blank form, It has a similar format to what's been described. There is a blank space for the form's title, for the question's title, and the question's description. On the side of the form, there is options for changing the format of the question, adding various content in it, and deleting the question. This idea has been executed in many ways, such as Formsite, which creates forms that emphasize security features, and Formstack, which gives features for highly regulated industries.

## Core User Workflows
The main features in our program will consist of the user writing over and deleting data. The user will be given a greeting and the option of either naming their quiz or choosing one of the premade templates or a previously made quiz by the user. If the user names their quiz, they will be asked how many of each type of question they want to have (multiple choice, True/False, numerical answer, and fill in the blank). After the mentioned prompts, the user will be presented the form for review. The form is then saved to a database as a template for them to choose.

## Tuesday - Thursday Daily Goals

### Tuesday
By the end of Tuesday, we want to establish the question type classes. Each type of question is going to take various type of formatting in class for later reference, and if this is accomplished early on, this will make the rest of the week much easier. We should also be able to accomplish most of the "creation" process by making use of these classes.

### Wednesday
Lathe will be writing code for editing content within the questions, Evan will work on returning the form for the user to review and making various templates from the established classes. 

### Thursday
This day will be reserved for finalizing save functions to datatbases and testing for bugs. Lathe will be making sure the databases written with sqlite are functioning properly and Evan will be writing input loops for each step of the program and checking for factors we may not have seen.

## How we will utilize the content
Evan and myself will be making much use of databases, classes, and file transfers for the majority of this project. Throughout the process of writing, we will have to use a little of everything we have learned thus far.