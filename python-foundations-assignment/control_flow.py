
import random
import time


#  Exercise 1 – Age Eligibility Checker

print("*" * 40)
print("     AGE ELIGIBILITY CHECKER")
print("*" * 40)

age = int(input("Enter your age : "))

if age < 0:
    print("  Please enter a valid age.")
elif age < 13:
    print(f"  You are a child ({age} years old).")
elif age < 18:
    print(f"  You are a teenager ({age} years old).")
else:
    print(f"  You are an adult ({age} years old).")
print()


# Exercise 2 – Password Validator

print("*" * 40)
print("            PASSWORD VALIDATOR")
print("*" * 40)

password = input("  Create a password : ")
length   = len(password)

if length < 6:
    strength = "Weak password! --- Use at least 6 characters."
elif length < 10:
    strength = "Moderate Strength! –-- Consider using atleast 10 characters."
else:
    strength = "Strong password!  –-- Great password length!"

print(f"  Password strength: {strength}\n")


#  Exercise 3 – Grade Classification


print("*" * 40)
print("     GRADE CLASSIFICATION")
print("*" * 40)

score = float(input(" Enter your score (0 – 100) : "))

if score < 0 or score > 100:
    print(" Invalid score. Score must be between 0 and 100.")
elif score >= 70:
    grade, remark = "A", "Distinction "
elif score >= 60:
    grade, remark = "B", "Credit "
elif score >= 50:
    grade, remark = "C", "Merit "
elif score >= 45:
    grade, remark = "D", "Pass "
else:
    grade, remark = "F", "Fail "

print(f"  Grade: {grade} | {remark}\n")


#  Exercise 4 – Multiplication Table

print("*" * 40)
print("     MULTIPLICATION TABLE")
print("*" * 40)

while True:
  try:
      num = int(input(" Enter a number : "))
      break 
  except ValueError:
      print(" Invalid input! Please enter a whole number (e.g, 5, 12, 892) ")
  print()
for i in range(1, 13):
    print(f"  {num} × {i} = {num * i}")
print()


#  Exercise 5 – Number Guessing Game


print("*" * 40)
print("     NUMBER GUESSING GAME")
print("*" * 40)

secret_num   = random.randint(1, 100)
attempts = 0
max_tries = 7

print(f"  Hello! I'm Houdini the Magician !!! 🧙‍♂️")
print(f"  I'm thinking of a number between 1 and 100. Can you guess it?")
print(f"  You have {max_tries} attempts. Good luck!\n")

while attempts < max_tries:
    guess     = int(input(f"  Attempt {attempts + 1}/{max_tries} – your guess : "))
    attempts += 1

    if guess < secret_num:
        print("  Too low!  Try higher.\n")
    elif guess > secret_num:
        print("  Too high!  Try lower.\n")
    else:
        print(f"   Correct! The number was {secret_num}. You got it in {attempts} attempt(s)!")
        break
else:
    print(f"  Oh no! You're out of attempts. \nThe number was {secret_num}. Better luck next time!")
print()


#  Exercise 6 – Countdown Timer


print("*" * 30)
print("     COUNTDOWN TIMER")
print("*" * 30)

print("  Counting down from 10...")
print()
for i in range(10, 0, -1):
    print(f"  {i}...")
    time.sleep(0.5)
print("  Liftoff!\n")


#  Exercise 7 – ATM Withdrawal Simulation

print("*" * 30)
print("        ATM WITHDRAWAL SIMULATION")
print("*" * 30)

account_balance = 50000.00   
print(f"  Account balance: ₦{account_balance:,.2f}")

withdrawal = float(input("  Enter amount to withdraw (₦) : "))

if withdrawal <= 0:
    print("  Invalid amount. Please enter a positive value.")
elif withdrawal > account_balance:
    print("  Insufficient funds. Transaction declined.")
elif withdrawal % 500 != 0:
    print("  Amount must be in multiples of ₦500.")
else:
    account_balance -= withdrawal
    print(f"  ₦{withdrawal:,.2f} dispensed successfully.")
    print(f"  Remaining balance: ₦{account_balance:,.2f}")
print()


#  Exercise 8 – Login System

print("*" * 30)
print("     LOGIN SYSTEM")
print("*" * 30)

STORED_USERNAME = "bethel.builds"
STORED_PASSWORD = "WomenInData25"
MAX_ATTEMPTS    = 3

for attempt in range(1, MAX_ATTEMPTS + 1):
    print(f"  Attempt {attempt} of {MAX_ATTEMPTS}")
    username = input("  Username : ")
    password = input("  Password : ")

    if username == STORED_USERNAME and password == STORED_PASSWORD:
      print("\n   Login successful! Welcome, Bethel \n")
      break
    else:
      remaining = MAX_ATTEMPTS - attempt
      if remaining > 0:
         print(f"    Incorrect credentials. {remaining} attempt(s) left.\n")
      else:
         print("   Account locked. Too many failed attempts.\n")