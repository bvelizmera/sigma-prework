from datetime import datetime


def age_calculator(date_of_birth_str):

    # Parse input string
    date_of_birth = datetime.strptime(date_of_birth_str, "%Y-%m-%d")

    # Retrieve current date
    current_date = datetime.now()

    # Calculate difference

    age_difference = current_date.year - date_of_birth.year

    if (date_of_birth.month, date_of_birth.day) > (current_date.month, current_date.day):
        age_difference -= 1

    return age_difference


def check_for_valid_date():

    # Ensure that user inputs right date format

    while True:
        date_request = input("Enter your date of birth (YYYY-MM-DD): ")

        try:
            datetime.strptime(date_request, "%Y-%m-%d")
            return date_request

        except ValueError:
            print("Wrong format. Please try again!")


date = check_for_valid_date()

age_gap = age_calculator(date)

print(age_gap)
