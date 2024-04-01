# Create a program that allows a user to choose one of
# up to 9 time zones from a menu. You can choose any
# zones you want from the all_timezones list.
#
# The program will then display the time in that timezone, as
# well as local time and UTC time.
#
# Entering 0 as the choice will quit the program.
#
# Display the dates and times in a format suitable for the
# user of your program to understand, and include the
# timezone name when displaying the chosen time.


import datetime
import pytz

tz_list = ["Africa/Timbuktu",
           "Asia/Hong_Kong",
           "Asia/Kuala_Lumpur",
           "America/New_York",
           "Europe/Berlin", ]

# Obtain the naive UTC datetime
naive_utc = datetime.datetime.utcnow()

# Makes the naive UTC datetime timezone aware
utc_time = pytz.utc.localize(naive_utc)

# Converts the aware UTC datetime into the datetime of the local timezone
# local_time = pytz.utc.localize(naive_utc).astimezone()
local_time = utc_time.astimezone()

while True:
    # Print the list and obtain user input
    print("Please choose a timezone from the list below (or 0 to quit)")
    for tz in tz_list:
        print(tz)
    chosen_timezone = input(": ")

    # Check if the user chose a valid timezone
    if chosen_timezone in tz_list:
        # Obtain the tzinfo from the chosen_timezone string
        chosen_timezone = pytz.timezone(chosen_timezone)
        # Obtain the aware datetime using the tzinfo
        chosen_time = utc_time.astimezone(chosen_timezone)

        # Print out the time and timezone
        print("UTC time:\t{}".format(utc_time.strftime("%A %x %X %Z")))
        print("Local time:\t{}".format(local_time.strftime("%A %x %X %Z")))
        print("Chosen time:\t{}".format(chosen_time.strftime("%A %x %X %Z")))
        print()
    
    # If input is 0, exit the program
    elif chosen_timezone == "0":
        break