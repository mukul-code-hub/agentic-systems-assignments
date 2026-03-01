#User information and string concatenation

firstname = input("What is your first name? ")
lastname = input("What is your last name? ")
age = input("What is your age? ")
try:
    age_int = int(age)

    if age_int < 0:
        print("Age cannot be negative.")
    else:
        full_name = firstname + " " + lastname
        print("Full Name : " + full_name)

    new_age = age_int + 1
    print("You will be " + str(new_age) + " next year.")
except ValueError:
    print("Invalid age input.")
