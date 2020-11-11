import sqlite3
from main import all_tf_questions, all_tf_answers
con = sqlite3.connect("database.db")
cur = con.cursor()

# cur.execute('CREATE TABLE Numerical("Questions" TEXT, "Answers" TEXT)')
# cur.execute('CREATE TABLE TrueFalse("Questions" TEXT, "Answers" TEXT)')
cur.execute('INSERT INTO Numerical VALUES(?, ?)', (all_tf_questions, all_tf_answers))
print(cur.fetchall())

