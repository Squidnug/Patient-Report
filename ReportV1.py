
print("Verification Process")
name = input("Enter name (Last, First): ")
age = input("Enter age: ")

print("Information")
birth_year = input("Enter birth date (mm/dd/yy): ")
allergy = input("Enter allergies (Peanuts, Pollen): ")
Pconditions = input("Enter previous condtions (If none 'N/A'): ")
Ccondtions = input("Enter current condtions (If none 'N/A'): ")
patient_status = input("Enter how much years you have been a patient here: ")

patient_status = int(patient_status)

if patient_status == 0:
    patient_status = ("New Patient")
elif patient_status > 0:
    patient_status = ("Registered Patient")


print("Paitent Report")
print("Name: " + name)
print ("Birth Year: " + birth_year)
print("Age: " + age)
print("Allergies: " + allergy)
print("Previous Condtions: " + Pconditions)
print("Current Condtions")
print ("Status: " + patient_status)