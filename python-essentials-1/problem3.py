# Age Category and Eligibility Checker

def check_eligibility(age) -> None:
    if age < 13:
        print("You are a child.")
    elif age <= 17:
        print("You are a teenager.")
    elif age <= 59:
        print("You are an adult.")
    else:
        print("You are a senior citizen.")

def check_vote_eligibility(age) -> None:
    if age >= 18:
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote.")

name = input("What is your name? ")
age = input("What is your age? ")
try:
    print("Hello, " + name + "!")
    age_int = int(age)
    if age_int < 0:
        print("Age cannot be negative.")
    else:
       # Check age category and voting eligibility
       check_eligibility(age_int)
       check_vote_eligibility(age_int)
    
except ValueError:
    print("Invalid age input. Please enter a valid number.")