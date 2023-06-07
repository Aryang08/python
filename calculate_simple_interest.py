def calculate_simple_interest(principal, rate):
    return (principal * rate) / 100

def calculate_interest_for_fixed_deposit(gender, is_senior_citizen, principal):
    if gender == "female" and is_senior_citizen:
        rate = 8
    elif gender == "female" and not is_senior_citizen:
        rate = 6
    elif gender == "male" and is_senior_citizen:
        rate = 7
    elif gender == "male" and not is_senior_citizen:
        rate = 5
    else:
        print("Invalid gender or senior citizen status.")
        return

    interest = calculate_simple_interest(principal, rate)
    return interest

gender = input("Enter the gender (male/female): ")
is_senior_citizen = input("Is the customer a senior citizen? (yes/no): ")
principal = float(input("Enter the principal amount: "))

if is_senior_citizen.lower() == "yes":
    is_senior_citizen = True
else:
    is_senior_citizen = False

interest = calculate_interest_for_fixed_deposit(gender.lower(), is_senior_citizen, principal)

if interest is not None:
    print("Simple Interest:", interest)
