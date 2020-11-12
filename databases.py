import sqlite3
con = sqlite3.connect("database.db")
cur = con.cursor()


cur.execute('CREATE TABLE if not exists Quizzes(Question TEXT)') 
cur.execute('INSERT INTO Quizzes VALUES("True/False: This is a true/false question")')
cur.execute('INSERT INTO Quizzes VALUES("Numerical: This is a numerical question")')
con.commit()
# cur.execute("SELECT * FROM Quizzes")
print(cur.fetchall())

