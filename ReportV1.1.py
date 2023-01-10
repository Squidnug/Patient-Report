import datetime




def validate_birth_date(year, month, day):
    try:
        datetime.datetime(year, month, day)
        current_date = datetime.datetime.now()
        if current_date.date() < datetime.date(year, month, day):
            return False
        return True
    except ValueError:
        return False

def calculate_age(year, month, day):
    current_date = datetime.datetime.now()
    birth_date = datetime.datetime(year, month, day)
    age = current_date.year - birth_date.year
    if current_date.month < birth_date.month or (current_date.month == birth_date.month and current_date.day < birth_date.day):
        age -= 1
    return age

print("Information")

name = input("Enter name (Last, First): ")

while True:
    birth_date = input("Enter birth date (MM/DD/YYYY): ")
    try:
        month, day, year = map(int, birth_date.split('/'))
        if validate_birth_date(year, month, day):
            age = calculate_age(year, month, day)
            break
        else:
            print("The birth date is invalid. Please enter a date in the past.")
    except ValueError:
        print("Invalid input. Birth date must be in the format MM/DD/YYYY.")


allergy = input("Enter allergies (Peanuts, Pollen, If none 'N/A'): ")
Pconditions = input("Enter previous condtions (If none 'N/A'): ")
Ccondtions = input("Enter current condtions (If none 'N/A'): ")
patient_status = input("Have you been a patient here before? (y/n): ")



if patient_status == ("n"):
    patient_status = ("New Patient")
elif patient_status == ("y"):
    patient_status = ("Registered Patient")


print("Paitent Report")
print("Name: " + name)
print ("Birth Year: " + birth_date)
print("Age: " , age)
print("Allergies: " + allergy)
print("Previous Condtions: " + Pconditions)
print("Current Condtions" + Ccondtions)
print ("Status: " + patient_status)


schedule = input("Thank you for updating your information would you like to schedule an appointment (y/n): ")



def validate_date(date_text):
    try:
        datetime_object = datetime.datetime.strptime(date_text, '%m-%d-%Y')
        if datetime_object.date() < datetime.datetime.today().date():
            return False
        return True
    except ValueError:
        return False

def validate_time(time_text):
    try:
        datetime.datetime.strptime(time_text, '%H:%M')
        return True
    except ValueError:
        return False

if schedule == "y":
    while True:
        date = input("Enter a date in the format MM-DD-YYYY: ")
        if validate_date(date):
            while True:
                time = input("Enter a time in the format HH:MM (24hrs): ")
                if validate_time(time):
                    print("Thank you, your schedule information should come up shortly.")
                    break
                else:
                    print("Provide future time. Please try again")
            break
        else:
            print("Provide future date. Please try again.")
else:
    print("Hope to see you again.")
    exit()





print("Schedule Information")
print("Date: " + date)
print("Time: " + time)


