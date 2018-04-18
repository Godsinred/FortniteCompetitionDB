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
    """ reads in the CSV file and populates the database based off the CSV(s). """
    create_competitors(conn, cur)
    create_events(conn, cur)
    create_awards(conn, cur)

def create_competitors(conn, cur):
    """ creates the competitors db. """

    cmd = """SELECT count(*) FROM sqlite_master WHERE type='table' AND name='Competitors'"""
    cur.execute(cmd)
    exists = cur.fetchall()

    # user_id (primary key), name, phone_number, sex, age, username, kills, deaths, wins, games_played

    cur.execute("""CREATE TABLE IF NOT EXISTS Competitors(
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

    
    for e in exists:
        if e[0] == 0:
            with open("competitors.csv", 'r', newline='') as f:
                read = csv.DictReader(f)
                for e in read:
                    cur.execute("""INSERT INTO Competitors(user_id, name, phone_number, sex, age, username, kills, deaths, wins, games_played)
                    VALUES(?,?,?,?,?,?,?,?,?,?)""", (e['ID'],e['Name'],e['Phone'],e['Sex'],e['Age'],e['Username'],e['Kills'],e['Deaths'],e['Wins'],e['Games']))

    conn.commit()

def create_events(conn, cur):
    """ creates the event db. """

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

    with open("events.csv", 'r', newline='') as f:
        read = csv.DictReader(f)
        for e in read:
            cur.execute("INSERT INTO Events(event_id, time, event_name, user_id_1, user_id_2, user_id_3, user_id_4) VALUES(?,?,?,?,?,?,?)",
            (e['ID'],e['time'],e['name'],e['user_1'],e['user_2'],e['user_3'],e['user_4']))

    conn.commit()

def create_awards(conn, cur):
    """ creates the awards db. """

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
    """ Function to create a competitor's account. """
    name = input("Please enter your name: ")
    phone_number = int(input("Please enter your phone number (i.e. 7149876543):"))
    sex = input("Please enter your sex (M = male, F = female): ").upper()[0]
    age = int(input("Please enter your age: "))
    username = input("Please enter your username: ")

    cur.execute("""INSERT INTO Competitors(name, phone_number, sex, age, username, kills, deaths, wins, games_played)
    VALUES(?,?,?,?,?,?,?,?,?)""", (name, phone_number, sex, age, username, 0, 0, 0, 0))

    conn.commit()

def update_account(conn, cur):
    """ Function to edit an existing competitor's account. """
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
    """ Function to delete a competitor's account. """
    print("Please enter the information for the account that you would like to delete.")
    name  = input("name: ")
    phone_number  = input("phone number: ")

    cmd = "DELETE FROM Competitors WHERE (name = \'" + name + "\' AND phone_number = " + phone_number + ")"
    cur.execute(cmd)

    conn.commit()

def create_event(conn, cur):
    """ Function to create an event. """
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
    """ Function to display all the competitors. """
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
    """ Function to display all the male competitors. """
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
    """ Function to display all the female competitors. """
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
    """ Function to display all events. """
    cur.execute("SELECT * FROM Events")
    all_events = cur.fetchall()

    print("\nShowing all events.")
    print("{:15s}{:15s}{:15s}{:15s}{:15s}{:15s}{:15s}".format("event_id", "time", "event_name", "user_id_1", "user_id_2", "user_id_3", "user_id_4"))

    for e in all_events:
        print("{:<15d}{:<15d}{:15s}{:<15d}{:<15d}{:<15d}{:<15d}".format(e[0], e[1], e[2], e[3],
                                                                  e[4], e[5], e[6]))

def find_user(conn, cur):
    """ Function to search for a competitor using a particular field name. """

    print("Find user from a category below: ")
    print("1. username")
    print("2. user id")
    print("3. name")
    print("4. phone number")
    choice  = int(input("Choice: "))

    category = ""
    detail = ""
    if choice is 1:
        category = "username"
    elif choice is 2:
        category = "user_id"
    elif choice is 3:
        category = "name"
    elif choice is 4:
        category = "phone_number"
    else:
        print("Invalid input.")
        return

    player_info = input("Enter players {}: ".format(category.replace("_", " ")))

    cmd_list = "SELECT * FROM Competitors WHERE " + category + " = \'" + player_info + "\'"
    cur.execute(cmd_list)
    user = cur.fetchall()

    print("{:15s}{:15s}{:15s}{:15s}{:15s}{:15s}{:15s}{:15s}{:15s}{:15s}".format("user_id", "name", "phone_number", "sex",
                                                                              "age", "username", "kills", "deaths",
                                                                              "wins", "games_played"))

    for c in user:
        print("{:<15d}{:15s}{:<15d}{:15s}{:<15d}{:15s}{:<15d}{:<15d}{:<15d}{:<15d}".format(c[0], c[1], c[2], c[3], c[4],
                                                                                    c[5], c[6], c[7], c[8], c[9]))

def save_to_csv(cur):
    """ Function to save data to a csv file. """
    with open('competitors.csv', 'r', newline='') as f:
        read = csv.DictReader(f)
        header = read.fieldnames

    with open('competitors.csv', 'w', newline='') as f:
        write = csv.writer(f)
        write.writerow(header)
        cur.execute("""SELECT * FROM Competitors""")
        comps = cur.fetchall()
        for c in comps:
            write.writerow([c[0], c[1], c[2], c[3], c[4], c[5], c[6], c[7], c[8], c[9]])

    with open('events.csv', 'r', newline='') as f:
        read = csv.DictReader(f)
        header = read.fieldnames

    with open('events.csv', 'w', newline='') as f:
        write = csv.writer(f)
        write.writerow(header)
        cur.execute("""SELECT * FROM Events""")
        events = cur.fetchall()
        for c in events:
            write.writerow([c[0], c[1], c[2], c[3], c[4], c[5], c[6]]) 

def show_all_events_with_competitors(conn, cur):
    """ function to display all the events with competitors. """
    cur.execute("""SELECT * FROM Events WHERE user_id_1 != -1""")
    events = cur.fetchall()
    print("{:15s}{:15s}{:15s}{:15s}{:15s}{:15s}{:15s}".format("event_id", "time", "event_name", "user_id_1", "user_id_2", "user_id_3", "user_id_4"))

    for e in events:
        print("{:<15d}{:<15d}{:15s}{:<15d}{:<15d}{:<15d}{:<15d}".format(e[0], e[1], e[2], e[3],
                                                                  e[4], e[5], e[6]))

def enter_event(conn, cur):
    """ Function to enter into an event. """
#<<<<<<< HEAD
#=======
    uID = int(input("Please enter your user ID: "))
    eID = int(input("Please enter the ID of the event you would like to sign up for: "))
    cmd = """ SELECT * FROM Events WHERE event_id=? """
    cur.execute(cmd, (eID,))
    e = cur.fetchall()
    counter = 4
    index = 0
    open = True
    for event in e:
        print("This event is designated as '" + event[2] + "'.")
        for i in range(6,2,-1):
            if event[i] != 0:
                counter -= 1
            else:
                break
        print("There are " + str(counter) + " open spots.")
        set_string = "user_id_" + str(counter)
        if counter > 0:
            loc = 3 + counter
            cmd = """ """
            cur.execute('UPDATE Events SET {user}=? WHERE event_id=?'.\
                format(user = set_string), (uID, eID))
            conn.commit()
            print("Thank you for entering this events, please be availble at " + str(event[1]) + ".")
        else:
            print("Sorry, this event is full")            

#>>>>>>> 1f7b0c1ea1e3b991b76ddfa73e7874a7fe62e358

def change_event(conn, cur):
    """ Function to change an event you're register for. """
    show_all_events(conn, cur)
    print()
    print("Change an event:")
    name = input("What is the event name: ").upper()
    time = int(input("What is the time of the event you want to change: "))

    print("What would you like to change: ")
    print("1. Event name")
    print("2. Time")
    print("3. Event name & Time")
    choice = int(input("Please make a selection: "))

    if (choice == 1):
        uname = input("What is the new event name: ").upper()
        cur.execute("UPDATE Events set event_name = ? where event_name = ? and time = ?", (uname, name, time,))
        print("Successfully updated the event name.")
    elif (choice == 2):
        utime = int(input("Enter the new time: "))
        cur.execute("UPDATE Events set time = ? where event_name = ? and time = ?", (utime, name, time,))
        print("Successfully updated the event time.")
    elif (choice == 3):
        uname = input("What is the new event name: ").upper()
        utime = int(input("Enter the new time: "))
        cur.execute("UPDATE Events set event_name = ?, time = ? where event_name = ? and time = ?", (uname, utime, name, time,))
        print("Successfully updated the event name and time.")
    else:
        print("An error occured. Please try again.")
        return #Exit function with no action.

    conn.commit()

def remove_from_event(conn, cur):
    """ Function to remove a competitor from a register event. """
    print("Use one of the options below to look up the user ID to unsubscribe: ")
    print("1. username")
    print("2. user id")
    print("3. name")
    print("4. phone number")
    choice  = int(input("Choice: "))

    if (choice == 1):
        username = input("Username: ")
        cmd = "SELECT user_id FROM Competitors WHERE  username = ?"
        cur.execute(cmd, (username,))
    elif (choice == 2):
        id = int(input("User ID: "))
        cmd = "SELECT user_id FROM Competitors WHERE user_id = ?"
        cur.execute(cmd, (id,))
    elif (choice == 3):
        name = input("Name: ")
        cmd = "SELECT username FROM Competitors WHERE name = ?"
        cur.execute(cmd, (name,))
    elif (choice == 4):
        phone = int(input("Phone Number: "))
        cmd = "SELECT user_id FROM Competitors WHERE phone_number = ?"
        cur.execute(cmd, (phone,))
    else:
        print("Invalid input.")
        return #Exit function with no action.

    info = cur.fetchall()

    show_all_events(conn, cur)
    print()
    print("Unsubscribe from event:")
    event = input("What is the event name: ").upper()
    time = int(input("What is the time of the event you want to unsubscribe from: "))

    cmd = "SELECT * FROM Events where event_name = ? and time = ?"
    cur.execute(cmd, (event, time,))

    events = cur.fetchall()

    index = 0
    for tup in events:
        items = list(tup)
        results = list(info[index])
        while (index < len(items)):
            if items[index] == results[0]:
                items[index] = -1
                break
            index += 1

        items.pop(0)
        cmd = """
            UPDATE Events SET time = ?, event_name = ?, user_id_1 = ?, user_id_2 = ?, user_id_3 = ?, user_id_4 = ?
        """
        cur.execute(cmd, items)

def show_all_winners(conn, cur):
    """ Function to display all winners from all events. """


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
        print("12. Show all events with competitors.")
        print("13. Show winners of all events.")
        print("14. Look up user.")
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
            enter_event(conn, cur)
        elif user_input is 6:
            change_event(conn, cur)
        elif user_input is 7:
            remove_from_event(conn, cur)
        elif user_input is 8:
            show_all_competitors(conn, cur)
        elif user_input is 9:
            show_all_male_competitors(conn, cur)
        elif user_input is 10:
            show_all_female_competitors(conn, cur)
        elif user_input is 11:
            show_all_events(conn, cur)
        elif user_input is 12:
            show_all_events_with_competitors(conn, cur)
        elif user_input is 13:
            show_all_winners(conn, cur)
        elif user_input is 14:
            find_user(conn, cur)
        else:
            print("Invalid Input: Please enter an integer from the options.")



    save_to_csv(cur)

    print("\nThank you for using FortniteCompetitionDB.\nHave a nice day!")

if __name__ == "__main__":
    main()
