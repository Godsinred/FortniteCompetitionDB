"""
Jonathan Ishii
Andrew Ramirez
Joshua Logue
Hector Elias

Lab 2
"""

import sqlite3
import csv

def create_db():
    # reads in the CSV file and populates the database based off the CSV(s)
    create_competitor()
    create_event()
    create_awards()
    pass

def create_competitor():
    # creates the competitors db

    # user_id (primary key), name, phone_number, sex, age, username, kills, deaths, wins, games_played
    pass

def create_event():
    # creates the event db

    # event_id, time, event_name (solo, duo, squad, LTM limited time mode), user_id, team_id, win
    pass

def create_awards():
    # creates the awards db

    # (solo_win, duo_win, squad_win) = umbrella , team_id
    pass

def main():

    create_db()

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
            pass
        elif user_input is 2:
            pass
        elif user_input is 3:
            pass
        elif user_input is 4:
            pass
        elif user_input is 5:
            pass
        elif user_input is 6:
            pass
        elif user_input is 7:
            pass
        elif user_input is 8:
            pass
        elif user_input is 9:
            pass
        elif user_input is 10:
            pass
        elif user_input is 11:
            pass
        elif user_input is 12:
            pass
        elif user_input is 13:
            pass
        else:
            print("Invalid Input: Please enter an integer from the options.")



    print("\nThank you for using FortniteCompetitionDB.\nHave a nice day!")

if __name__ == "__main__":
    main()