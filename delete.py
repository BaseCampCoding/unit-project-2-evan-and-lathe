import sqlite3
gb = sqlite3.connect("GBOOK.db")
writer = gb.cursor()
writer.execute(
    """CREATE TABLE if not exists GuestBook(
    name TEXT,
    message TEXT
)"""
)
GUESTBOOK = []
while True:
    action = input(
        """Do you want to:
    - sign
    - view
    - quit
    > """
    )
    if action == "sign":
        name = input("Name: ")
        message = input("Message: ")
        entry = [["name", name], ["message", message]]
        GUESTBOOK.append(entry)
    elif action == "view":
        for entry in GUESTBOOK:
            print(f"{entry}")
    elif action == "quit":
        print("Goodbye!")
        break
writer.execute(""" INSERT INTO GuestBook VALUES (?,?,?), GUESTBOOK""")