import sys
import datetime
import time

from colors import bcolors

from random import random
from random import seed

from datetime import date

# declaring global variables -------------------------------------------------------------------------------
name = ["username"] * 28
phone_number = [000000000] 
travel_date = "dd mm yyyy"
travel_time = "00:00"

today_date = datetime.datetime.now()  # getting today's date and formatting it

from datetime import datetime
today_time = datetime.now().strftime("%H:%M")  # getting today's time and formatting it

total_number_of_seats = 0
terminator = 0
current_user_number = 0
current_location = "unknown"
destination = "unknown"
cost = 0.0

# declaring variables to print the seating pattern ---------------------------------------------------------
occupied_seats = [True, False,                             # row 1
                  False, True,                             # row 2
                  True, True, False, True,                 # row 3
                  True, False, False, False,               # row 4
                  False, False, True, True,                # row 5
                  True, True, True, False, False, False,   # row 6
                  False, True, True, True, True, False,    # row 7
                  True, False, False, False, False, True,  # row 8
                  True, True, False, False, False, False,  # row 9
                  False, False, False, True, True, True,   # row 10
                  True, True, True, True, True, True]      # row 11
all_seats = ["1A", "1F", "2A", "2F", "3A", "3B", "3E", "3F", "4A", "4B", "4E", "4F", "5A", "5B", "5E", "5F",
             "6A", "6B", "6C", "6D", "6E", "6F", "7A", "7B", "7C", "7D", "7E", "7F", "8A", "8B", "8C", "8D", "8E", "8F",
             "9A", "9B", "9C", "9D", "9E", "9F", "10A", "10B", "10C", "10D", "10E", "10F",
             "11A", "11B", "11C", "11D", "11E", "11F"]

# declaring global variables to accept the seat from the user --------------------------------------------
number_of_seats_booked = 0
users_seat = ["nothing here"] * 28
all_seats_index = 0


# displaying the welcome pattern at the beginning
def display_welcome():
    # displaying welcome
    print(" *       *   * * * *   *         * * *    * * * *    *     *   * * * * ")
    print(" *       *   *         *        *        *       *   * * * *   *       ")
    print(" *   *   *   * * * *   *       *        *         *  *  *  *   * * * * ")
    print(" * *   * *   *         *        *        *       *   *     *   *       ")
    print(" *       *   * * * *   * * * *   * * *    * * * *    *     *   * * * * ")
    print(f"{bcolors.BOLD}{bcolors.HEADER}{bcolors.UNDERLINE}Welcome to https://github.com/Anjna25/Airplane_Seating_Reservation-System , "
          f"We would like to take some information:{bcolors.ENDC}{bcolors.ENDC}{bcolors.ENDC}")


def constant_details():
    global total_number_of_seats
    global terminator
    global current_location
    global destination
    global travel_date
    global today_date
    global travel_time
    global today_time

    # accepting the total number of seats the user wants to book --------------------------------------------
    total_number_of_seats = input("Total number of reservations: ")

    available_number_of_seats = 0

    for i in range(0, len(occupied_seats)):  # finding the available number of seats
        if occupied_seats[i]:
            available_number_of_seats += 1

    while True:
        if int(total_number_of_seats) == 0:
            total_number_of_seats = input(f"{bcolors.WARNING}ZERO? Please enter the proper value: {bcolors.ENDC}")
        elif 0 >= int(total_number_of_seats):
            total_number_of_seats = input(f"{bcolors.WARNING}You have entered a negative value... Please enter the "
                                          f"number of reservations as a positive value: {bcolors.ENDC}")
        elif int(total_number_of_seats) >= available_number_of_seats:
            total_number_of_seats = input(f"{bcolors.WARNING}We don't have that many seats available... "
                                          f"Please enter a lower value: {bcolors.ENDC}")
        else:
            break

    # declaring the value of terminator
    terminator = int(total_number_of_seats)
    terminator = terminator - 1

    while True:
        dt, mt, yt = [int(x) for x in input("Enter Travel Date (dd/mm/yyyy): ").split('/')]
        travel_date = date(yt, mt, dt)

        if int(yt) >= (3 + int(today_date.year)):
            print(f"{bcolors.WARNING}You are travelling {int(yt) - int(today_date.year)} years from now"
                  f" We don't have tickets for that time...{bcolors.ENDC}")

        travelling_today = False
        travelling_in_the_past = False
        travelling_in_the_future = False

        if int(dt) == int(today_date.day) and int(mt) == int(today_date.month) and int(yt) == int(today_date.year):
            travelling_today = True
        elif int(yt) > int(today_date.year):
            travelling_in_the_future = True
        elif int(yt) == int(today_date.year) and int(mt) > int(today_date.month):
            travelling_in_the_future = True
        elif int(yt) == int(today_date.year) and int(mt) >= int(today_date.month) and int(dt) > int(today_date.day):
            travelling_in_the_future = True
        else:
            travelling_in_the_past = True

        if travelling_today:
            travel_time = input("Since you are travelling today, please enter timings (HH:MM): ")
            while True:
                if today_time > travel_time:
                    travel_time = input(f"{bcolors.WARNING}Looks like that time has already passed."
                                        f" Please enter proper time: {bcolors.ENDC}")
                else:
                    break
            break
        elif travelling_in_the_future:
            flag1 = False
            flag2 = False
            travel_time = input("Please enter time of travel (hh:mm): ")
            while True:
                if int(travel_time[0:2]) > 23:
                    travel_time = input(f"{bcolors.FAIL}INVALID TIMINGS{bcolors.ENDC} "
                                        f"Please enter the correct timings: ")
                    flag1 = True
                if int(travel_time[3:5]) > 59:
                    travel_time = input(f"{bcolors.FAIL}INVALID MINUTES{bcolors.ENDC} "
                                        f"Please enter the correct timings: ")
                    flag2 = True
                if flag1 or flag2:
                    flag1 = False
                    flag2 = False
                    continue
                else:
                    break
            break
        elif travelling_in_the_past:
            print(f"{str(travel_date)} {bcolors.FAIL} Has already passed{bcolors.ENDC}")

    # accepting the current location ------------------------------------------------------------------
    current_location = input("From: ")

    # accepting the destination -----------------------------------------------------------------------
    destination = input("To: ")

    # converting current_location and destination into upper case
    current_location = current_location.capitalize()
    destination = destination.capitalize()


def display_aeroplane_seat():
    # global variables
    global occupied_seats
    global all_seats

    # displaying Business Class
    print("              " + f"{bcolors.BOLD}First Class{bcolors.ENDC}" + "              ")

    for i in range(0, 4):
        # displaying 1A and 2A with colour code
        if occupied_seats[i] and (i == 0 or i == 2):
            print("▢ " + f"{bcolors.WARNING}{all_seats[i]}{bcolors.ENDC}" + "                             ", end="")
        elif not occupied_seats[i] and (i == 0 or i == 2):
            print("▢ " + f"{bcolors.OKGREEN}{all_seats[i]}{bcolors.ENDC}" + "                             ", end="")

        # displaying 1F and 2F with colour code
        if occupied_seats[i] and (i == 1 or i == 3):
            print(f"{bcolors.WARNING}{all_seats[i]}{bcolors.ENDC}" + " ▢", end="\n")
        elif not occupied_seats[i] and (i == 1 or i == 3):
            print(f"{bcolors.OKGREEN}{all_seats[i]}{bcolors.ENDC}" + " ▢", end="\n")

    # displaying First Class
    print("             " + f"{bcolors.BOLD}Business Class{bcolors.ENDC}" + "           ")

    for i in range(4, 16):
        # displaying 3A, 4A and 5A with colour code
        if occupied_seats[i] and (i == 4 or i == 8 or i == 12):
            print("▢ " + f"{bcolors.WARNING}{all_seats[i]}{bcolors.ENDC}", end="   ")
        elif not occupied_seats[i] and (i == 4 or i == 8 or i == 12):
            print("▢ " + f"{bcolors.OKGREEN}{all_seats[i]}{bcolors.ENDC}", end="   ")

        # displaying 3B, 4B and 5B with colour coding
        if occupied_seats[i] and (i == 5 or i == 9 or i == 13):
            print(f"{bcolors.WARNING}{all_seats[i]}{bcolors.ENDC}", end="                   ")
        elif not occupied_seats[i] and (i == 5 or i == 9 or i == 13):
            print(f"{bcolors.OKGREEN}{all_seats[i]}{bcolors.ENDC}", end="                   ")

        # displaying 3E, 4E and 5E with colour coding
        if occupied_seats[i] and (i == 6 or i == 10 or i == 14):
            print(f"{bcolors.WARNING}{all_seats[i]}{bcolors.ENDC}", end="   ")
        elif not occupied_seats[i] and (i == 6 or i == 10 or i == 14):
            print(f"{bcolors.OKGREEN}{all_seats[i]}{bcolors.ENDC}", end="   ")

        # displaying 3F, 4F and 5F with colour coding
        if occupied_seats[i] and (i == 7 or i == 11 or i == 15):
            print(f"{bcolors.WARNING}{all_seats[i]}{bcolors.ENDC}" + " ▢", end="\n")
        elif not occupied_seats[i] and (i == 7 or i == 11 or i == 15):
            print(f"{bcolors.OKGREEN}{all_seats[i]}{bcolors.ENDC}" + " ▢", end="\n")

    # displaying Economy Class
    print("             " + f"{bcolors.BOLD}Economy Class{bcolors.ENDC}" + "            ")

    for i in range(16, 52):
        # displaying 6A, 7A, 8A and 9A with colour code
        if occupied_seats[i] and (i == 16 or i == 22 or i == 28 or i == 34):
            print("▢ " + f"{bcolors.WARNING}{all_seats[i]}{bcolors.ENDC}", end="   ")
        elif not occupied_seats[i] and (i == 16 or i == 22 or i == 28 or i == 34):
            print("▢ " + f"{bcolors.OKGREEN}{all_seats[i]}{bcolors.ENDC}", end="   ")

        # displaying 6B, 7B, 8B and 9B with colour code
        if occupied_seats[i] and (i == 17 or i == 23 or i == 29 or i == 35):
            print(f"{bcolors.WARNING}{all_seats[i]}{bcolors.ENDC}", end="   ")
        elif not occupied_seats[i] and (i == 17 or i == 23 or i == 29 or i == 35):
            print(f"{bcolors.OKGREEN}{all_seats[i]}{bcolors.ENDC}", end="   ")

        # displaying 6C, 7C, 8C and 9C with colour code
        if occupied_seats[i] and (i == 18 or i == 24 or i == 30 or i == 36):
            print(f"{bcolors.WARNING}{all_seats[i]}{bcolors.ENDC}", end="         ")
        elif not occupied_seats[i] and (i == 18 or i == 24 or i == 30 or i == 36):
            print(f"{bcolors.OKGREEN}{all_seats[i]}{bcolors.ENDC}", end="         ")

        # displaying 6D, 7D, 8D and 9D with colour coding
        if occupied_seats[i] and (i == 19 or i == 25 or i == 31 or i == 37):
            print(f"{bcolors.WARNING}{all_seats[i]}{bcolors.ENDC}", end="   ")
        elif not occupied_seats[i] and (i == 19 or i == 25 or i == 31 or i == 37):
            print(f"{bcolors.OKGREEN}{all_seats[i]}{bcolors.ENDC}", end="   ")

        # displaying 6E, 7E, 8E and 9E with colour coding
        if occupied_seats[i] and (i == 20 or i == 26 or i == 32 or i == 38):
            print(f"{bcolors.WARNING}{all_seats[i]}{bcolors.ENDC}", end="   ")
        elif not occupied_seats[i] and (i == 20 or i == 26 or i == 32 or i == 38):
            print(f"{bcolors.OKGREEN}{all_seats[i]}{bcolors.ENDC}", end="   ")

        # displaying 6F, 7F, 8F and 9F with colour coding
        if occupied_seats[i] and (i == 21 or i == 27 or i == 33 or i == 39):
            print(f"{bcolors.WARNING}{all_seats[i]}{bcolors.ENDC}" + " ▢", end="\n")
        elif not occupied_seats[i] and (i == 21 or i == 27 or i == 33 or i == 39):
            print(f"{bcolors.OKGREEN}{all_seats[i]}{bcolors.ENDC}" + " ▢", end="\n")

    for i in range(40, 52):
        # displaying 10A and 11A with colour code
        if occupied_seats[i] and (i == 40 or i == 46):
            print("▢ " + f"{bcolors.WARNING}{all_seats[i]}{bcolors.ENDC}", end="   ")
        elif not occupied_seats[i] and (i == 40 or i == 46):
            print("▢ " + f"{bcolors.OKGREEN}{all_seats[i]}{bcolors.ENDC}", end="   ")

        # displaying 6B, 7B, 8B and 9B with colour code
        if occupied_seats[i] and (i == 41 or i == 47):
            print(f"{bcolors.WARNING}{all_seats[i]}{bcolors.ENDC}", end="  ")
        elif not occupied_seats[i] and (i == 41 or i == 47):
            print(f"{bcolors.OKGREEN}{all_seats[i]}{bcolors.ENDC}", end="  ")

        # displaying 6C, 7C, 8C and 9C with colour code
        if occupied_seats[i] and (i == 42 or i == 48):
            print(f"{bcolors.WARNING}{all_seats[i]}{bcolors.ENDC}", end="      ")
        elif not occupied_seats[i] and (i == 42 or i == 48):
            print(f"{bcolors.OKGREEN}{all_seats[i]}{bcolors.ENDC}", end="      ")

        # displaying 6D, 7D, 8D and 9D with colour coding
        if occupied_seats[i] and (i == 43 or i == 49):
            print(f"{bcolors.WARNING}{all_seats[i]}{bcolors.ENDC}", end="  ")
        elif not occupied_seats[i] and (i == 43 or i == 49):
            print(f"{bcolors.OKGREEN}{all_seats[i]}{bcolors.ENDC}", end="  ")

        # displaying 6E, 7E, 8E and 9E with colour coding
        if occupied_seats[i] and (i == 44 or i == 50):
            print(f"{bcolors.WARNING}{all_seats[i]}{bcolors.ENDC}", end="  ")
        elif not occupied_seats[i] and (i == 44 or i == 50):
            print(f"{bcolors.OKGREEN}{all_seats[i]}{bcolors.ENDC}", end="  ")

        # displaying 6F, 7F, 8F and 9F with colour coding
        if occupied_seats[i] and (i == 45 or i == 51):
            print(f"{bcolors.WARNING}{all_seats[i]}{bcolors.ENDC}" + " ▢", end="\n")
        elif not occupied_seats[i] and (i == 45 or i == 51):
            print(f"{bcolors.OKGREEN}{all_seats[i]}{bcolors.ENDC}" + " ▢", end="\n")

    accept_users_seat()


def accept_users_seat():  # accepting the users seat number ---------------------------------------------------
    global number_of_seats_booked
    global users_seat
    global all_seats_index
    global occupied_seats
    global terminator
    global current_user_number
    global name
    global phone_number
    global current_user_number

    while True:
        if current_user_number <= terminator:
            # accepting the name of the user
            name[current_user_number] = input("Your Name please: ")  # accepting the users name
            name[current_user_number].strip()  # removing unwanted spaces before and after the name
            name[current_user_number] = name[current_user_number] + " "  # adding a space after the name

            # declaration
            name_operator = name[current_user_number]
            word = ""
            new_name = ""

            # capitalizing name ----------------------------------------------------------------------------
            for i in range(0, len(name_operator)):
                ch = name_operator[i]
                word = word + ch

                if ch == ' ':
                    word = word.capitalize()
                    new_name = new_name + word
                    word = ""

            name[current_user_number] = new_name

            # accepting the phone number of the user --------------------------------------------------------
            phone_number = input("Enter your phone number: ")

            while True:
                if not phone_number.isdigit():
                    phone_number = input(f"{bcolors.WARNING}Looks like your phone number has alphabets... "
                                         f"Please enter the correct value: {bcolors.ENDC}")
                else:
                    break

            while len(phone_number) != 10:
                print("Please make sure that the phone number that you have entered is 10 digits long")
                print("The phone number you entered was " + str(len(phone_number)) + " digits long ")
                phone_number = input("Please enter the phone number: ")

            # accepting users seat
            users_seat[number_of_seats_booked] = input(f"{bcolors.BOLD}Please enter the seat "
                                                       f"that you want to book: {bcolors.ENDC}")

            # finding index of all seats
            for j in range(0, len(all_seats)):
                if all_seats[j] == users_seat[number_of_seats_booked]:
                    all_seats_index = j

            if occupied_seats[all_seats_index]:
                print(f"{bcolors.WARNING}{bcolors.BOLD}That seat has already been booked/reserved"
                      f"{bcolors.ENDC}{bcolors.ENDC}")
                continue
            elif not occupied_seats[all_seats_index]:
                occupied_seats[all_seats_index] = True
                number_of_seats_booked += 1
                print(
                    f"{bcolors.OKCYAN}Your seat {users_seat[number_of_seats_booked - 1]} has been booked{bcolors.ENDC}")
                current_user_number = current_user_number + 1

            time.sleep(3)

            # printing 40 lines of space:
            print("\n" * 40)

        if current_user_number <= terminator:
            display_aeroplane_seat()

        display_boarding_pass()


def display_boarding_pass():  # displaying boarding pass --------------------------------------------------------
    global users_seat
    global name
    global number_of_seats_booked
    global cost

    print("\n"*40)
    print(f"{bcolors.BOLD}{bcolors.UNDERLINE}{bcolors.HEADER}Boarding Pass for all the seats that you booked:"
          f"{bcolors.ENDC}{bcolors.ENDC}{bcolors.ENDC}")

    seed(10)

    _date = str(travel_date)
    value = random() * 10

    for i in range(0, number_of_seats_booked):

        # calculating the cost for the type of seat booked
        seat_booked = users_seat[i]
        seat_type = seat_booked[0]

        if int(seat_type) <= 2:
            cost = 100000
        elif int(seat_type) <= 5:
            cost = 40000
        else:
            cost = 10000

        #  I know you want to change the travels name? ↓↓↓
        print("   https://github.com/Anjna25/Airplane_Seating_Reservation-System     ")

        print(f"{bcolors.OKBLUE}Name: {bcolors.ENDC}{name[i]} "
              f"{bcolors.OKBLUE}Flight: {bcolors.ENDC}OKL012"
              f"{bcolors.OKBLUE} Seat Number: {bcolors.ENDC}{users_seat[i]}")
        print(f"{bcolors.OKGREEN}Gate: {bcolors.ENDC}{int(value)}"
              f"{bcolors.OKGREEN} date: {bcolors.ENDC}{travel_date}\t"
              f"{bcolors.OKGREEN}Cost: {bcolors.ENDC}{cost}")
        print(f"{bcolors.OKBLUE}From: {bcolors.ENDC}{current_location}\t{bcolors.OKCYAN}To: "
              f"{bcolors.ENDC}{destination}")

    sys.exit()
