"""
Jonathan Ishii
Andrew Ramirez
Joshua Logue
Hector Elias

Lab 2
"""

import sqlite3
import csv

def create_db(conn, cur):
    # reads in the CSV file and populates the database based off the CSV(s)
    create_competitors(conn, cur)
    create_events(conn, cur)
    create_awards(conn, cur)

def create_competitors(conn, cur):
    # creates the competitors db

    # user_id (primary key), name, phone_number, sex, age, username, kills, deaths, wins, games_played

    # Clean the database
    cur.execute("""DROP TABLE IF EXISTS Competitors""")

    cur.execute("""CREATE TABLE Competitors(
    user_id INTEGER PRIMARY KEY NOT NULL,
    name TEXT,
    phone_number INTERGER,
    sex TEXT,
    age INTEGER,
    username TEXT,
    kills INTEGER,
    deaths INTEGER,
    wins INTEGER,
    games_played INTEGER
    );""")

    # with open("competitors.csv", 'r', newline='') as f:
    cur.execute("""INSERT INTO Competitors(user_id, name, phone_number, sex, age, username, kills, deaths, wins, games_played)
    VALUES(?,?,?,?,?,?,?,?,?,?)""", (100000, "Jon Ishii", 3104880439, "M", 26, "Godsinred", 123, 456, 78, 90))

    cur.execute("""INSERT INTO Competitors(name, phone_number, sex, age, username, kills, deaths, wins, games_played)
    VALUES(?,?,?,?,?,?,?,?,?)""", ("Andrew Ramirez", 3101234567, "M", 22, "Reptar", 12, 23, 45, 67))

    conn.commit()

def create_events(conn, cur):
    # creates the event db

    # event_id, time, event_name (solo, duo, squad, LTM limited time mode), user_id, team_id, win

    # Clean the database
    cur.execute("""DROP TABLE IF EXISTS Events""")

    # user_id's are the winners for the games
    cur.execute("""CREATE TABLE Events(
    event_id INTEGER PRIMARY KEY NOT NULL,
    time INTEGER,
    event_name TEXT,
    user_id_1 INTEGER,
    user_id_2 INTEGER,
    user_id_3 INTEGER,
    user_id_4 INTEGER
    );""")

    #with open("events.csv", 'r', newline='') as f:
    cur.execute("INSERT INTO Events(event_id, time, event_name, user_id_1, user_id_2, user_id_3, user_id_4) VALUES(?,?,?,?,?,?,?)",
                (500000, 600, "SOLO", 100000, -1, -1, -1))
    cur.execute("INSERT INTO Events(time, event_name, user_id_1, user_id_2, user_id_3, user_id_4) VALUES(?,?,?,?,?,?)",
                (630, "DUO", 100001, 100002, -1, -1))
    cur.execute("INSERT INTO Events(time, event_name, user_id_1, user_id_2, user_id_3, user_id_4) VALUES(?,?,?,?,?,?)",
                (1600, "SQUAD", 100003, 100004, 100005, 100006))

    conn.commit()

def create_awards(conn, cur):
    # creates the awards db

    # (solo_win, duo_win, squad_win) = umbrella , award

    # Clean the database
    cur.execute("""DROP TABLE IF EXISTS Awards""")

    cur.execute("""CREATE TABLE Awards(
    event_name TEXT,
    award TEXT
    );""")

    # with open("awards.csv", 'r', newline='') as f:
    cur.execute("INSERT INTO Awards(event_name, award) VALUES(?,?)", ("SOLO", 100))
    cur.execute("INSERT INTO Awards(event_name, award) VALUES(?,?)", ("DUO", 200))
    cur.execute("INSERT INTO Awards(event_name, award) VALUES(?,?)", ("SQUAD", 400))

    conn.commit()

def create_account(conn, cur):
    name = input("Please enter your name: ")
    phone_number = int(input("Please enter your phone number (i.e. 7149876543):"))
    sex = input("Please enter your sex (M = male, F = female): ").upper()[0]
    age = int(input("Please enter your age: "))
    username = input("Please enter your username: ")

    cur.execute("""INSERT INTO Competitors(name, phone_number, sex, age, username, kills, deaths, wins, games_played)
    VALUES(?,?,?,?,?,?,?,?,?)""", (name, phone_number, sex, age, username, 0, 0, 0, 0))

    conn.commit()

def update_account(conn, cur):
    num = int(input("Please enter the phone number for the account that you would like to edit: "))
    print("What would you like to update?")
    print("1. name")
    print("2. phone number")
    print("3. sex")
    print("4. age")
    print("5. username")

    choice = int(input("Choice: "))

    if choice is 1:
        name = input("Please enter your name: ")
        cmd = "UPDATE Competitors SET name = \'" + name + "\' WHERE phone_number = " + str(num)
        cur.execute(cmd)
    elif choice is 2:
        phone_number = input("Please enter your new phone number (i.e. 7149876543):")
        cmd = "UPDATE Competitors SET phone_number = " + phone_number  + " WHERE phone_number = " + str(num)
        cur.execute(cmd)
    elif choice is 3:
        sex = input("Please enter your sex (M = male, F = female): ").upper()[0]
        cmd = "UPDATE Competitors SET sex = \'" + sex  + "\' WHERE phone_number = " + str(num)
        cur.execute(cmd)
    elif choice is 4:
        age = input("Please enter your age: ")
        cmd = "UPDATE Competitors SET age = " + age + " WHERE phone_number = " + str(num)
        cur.execute(cmd)
    elif choice is 5:
        username = input("Please enter your username: ")
        cmd = "UPDATE Competitors SET username = \'" + username  + "\' WHERE phone_number = " + str(num)
        cur.execute(cmd)
    else:
        print("Invalid choice.")

    conn.commit()

def delete_account(conn, cur):
    print("Please enter the information for the account that you would like to delete.")
    name  = input("name: ")
    phone_number  = input("phone number: ")

    cmd = "DELETE FROM Competitors WHERE (name = \'" + name + "\' AND phone_number = " + phone_number + ")"
    cur.execute(cmd)

    conn.commit()

def create_event(conn, cur):
    print("1. Solo")
    print("2. Duo")
    print("3. Squad")
    event = int(input("Enter a number for the event type you would like to host? "))

    if event is 1:
        event = "Solo"
    elif event is 2:
        event = "Duo"
    elif event is 3:
        event = "Squad"
    else:
        print("Invalid choice.")
        return

    time = int(input("What time would you like to create the event? "))

    cmd = "INSERT INTO Events(time, event_name, user_id_1, user_id_2, user_id_3, user_id_4) VALUES(?,?,?,?,?,?)"
    cur.execute(cmd, (time, event, -1, -1, -1, -1))

    conn.commit()


def show_all_competitors(conn, cur):
    cur.execute("SELECT * FROM Competitors")
    comp = cur.fetchall()

    print("\nShowing all competitors.")
    print("{:15s}{:15s}{:15s}{:15s}{:15s}{:15s}{:15s}{:15s}{:15s}{:15s}".format("user_id", "name", "phone_number", "sex",
                                                                              "age", "username", "kills", "deaths",
                                                                              "wins", "games_played"))
    for c in comp:
        print("{:<15d}{:15s}{:<15d}{:15s}{:<15d}{:15s}{:<15d}{:<15d}{:<15d}{:<15d}".format(c[0], c[1], c[2], c[3], c[4],
                                                                                    c[5], c[6], c[7], c[8], c[9]))

def show_all_male_competitors(conn, cur):
    cur.execute("""SELECT * FROM Competitors
    WHERE sex = 'M'""")
    comp = cur.fetchall()

    print("\nShowing all male competitors.")
    print("{:15s}{:15s}{:15s}{:15s}{:15s}{:15s}{:15s}{:15s}{:15s}{:15s}".format("user_id", "name", "phone_number", "sex",
                                                                              "age", "username", "kills", "deaths",
                                                                              "wins", "games_played"))
    for c in comp:
        print("{:<15d}{:15s}{:<15d}{:15s}{:<15d}{:15s}{:<15d}{:<15d}{:<15d}{:<15d}".format(c[0], c[1], c[2], c[3], c[4],
                                                                                    c[5], c[6], c[7], c[8], c[9]))

def show_all_female_competitors(conn, cur):
    cur.execute("""SELECT * FROM Competitors
    WHERE sex = 'F'""")
    comp = cur.fetchall()

    print("\nShowing all female competitors.")
    print("{:15s}{:15s}{:15s}{:15s}{:15s}{:15s}{:15s}{:15s}{:15s}{:15s}".format("user_id", "name", "phone_number", "sex",
                                                                              "age", "username", "kills", "deaths",
                                                                              "wins", "games_played"))
    for c in comp:
        print("{:<15d}{:15s}{:<15d}{:15s}{:<15d}{:15s}{:<15d}{:<15d}{:<15d}{:<15d}".format(c[0], c[1], c[2], c[3], c[4],
                                                                                    c[5], c[6], c[7], c[8], c[9]))

def show_all_events(conn, cur):
    cur.execute("SELECT * FROM Events")
    all_events = cur.fetchall()

    print("\nShowing all events.")
    print("{:15s}{:15s}{:15s}{:15s}{:15s}{:15s}{:15s}".format("event_id", "time", "event_name", "user_id_1", "user_id_2", "user_id_3", "user_id_4"))

    for e in all_events:
        print("{:<15d}{:<15d}{:15s}{:<15d}{:<15d}{:<15d}{:<15d}".format(e[0], e[1], e[2], e[3],
                                                                  e[4], e[5], e[6]))

def main():

    conn = sqlite3.connect("fortnite.sqlite")
    cur = conn.cursor()

    create_db(conn, cur)

    # allow the user to enter, modify, and delete records

    # contain at least one many-to-many relationship with a corresponding junction table

    # dynamically generate at least one graph of your database.
    # You might graph the number of awards each person earned, the times of the finishers, the average times, etc

    # you must be able to display (at least)
    # – All competitors alphabetically
    # – Competitors and their bib numbers (or whatever number they have) – All male competitors
    # – All female competitors
    # – All events, listed by starting time
    # – All of the competitors of each event
    # – The top winners of each event

    # You should allow the user to look up (at least)
    # – A person’s id given their name, event, and age
    # – A person’s information given their id number
    # – A person’s overall time (or whatever you’re tracking to determine winners) given their name or id (if matching by name, it’s OK if multiple people are returned)
    # – A person’s award(s) given their id number

    print("Welcome to FortniteCompetitionDB!")
    print("--------------------------------------------------------")
    print("This is a program for all users to create/edit accounts ")
    print("and events as well as displaying vital information.")
    print("--------------------------------------------------------")

    done = False
    while not done:
        print("\nPlease enter in a number from the options below.\n")
        print("1. Create account")
        print("2. Edit account.")
        print("3. Delete account.")
        print("4. Create an event.")
        print("5. Enter in an event.")
        print("6. Change event you are registered in.")
        print("7. Remove yourself from an event.")
        print("8. Show all competitors.")
        print("9. Show all male competitors.")
        print("10. Show all female competitors.")
        print("11. Show all events.")
        print("11. Show all events with competitors.")
        print("12. Show winners of all events.")
        print("13. Look up user.")
        print("\nEnter -1 to quit.")

        user_input = int(input("Choice: "))

        if user_input < 0:
            done = True
        elif user_input is 1:
            create_account(conn, cur)
        elif user_input is 2:
            update_account(conn, cur)
        elif user_input is 3:
            delete_account(conn, cur)
        elif user_input is 4:
            create_event(conn, cur)
        elif user_input is 5:
            pass
        elif user_input is 6:
            pass
        elif user_input is 7:
            pass
        elif user_input is 8:
            show_all_competitors(conn, cur)
        elif user_input is 9:
            show_all_male_competitors(conn, cur)
        elif user_input is 10:
            show_all_female_competitors(conn, cur)
        elif user_input is 11:
            show_all_events(conn, cur)
        elif user_input is 12:
            pass
        elif user_input is 13:
            pass
        else:
            print("Invalid Input: Please enter an integer from the options.")



    print("\nThank you for using FortniteCompetitionDB.\nHave a nice day!")

if __name__ == "__main__":
    main()