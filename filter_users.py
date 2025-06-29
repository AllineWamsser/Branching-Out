import json

def load_users():
    """Loads user data from the JSON file."""

    with open("users.json", "r") as file:
        return json.load(file)

def filter_users_by_name(name):
    """Filters users by name and prints results."""

    users = load_users()
    filtered_users = [user for user in users if user["name"].lower() == name.lower()]
    for user in filtered_users:
        print(user)

def filter_by_age(age):
    """Filters users by age and prints results."""

    users = load_users()
    filtered_users = [user for user in users if user["age"] == age]
    for user in filtered_users:
        print(user)

def filter_by_email(email):
    """Filters users by email and prints results."""
    users = load_users()
    filtered_users = [user for user in users if user ["email"].lower() == email.lower()]
    for user in filtered_users:
        print(user)

if __name__ == "__main__":
    filter_option = input("What would you like to filter by? (name/age/email): ").strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search)

    elif filter_option == "age":
        try:
            age_to_search = int(input("Enter an age to filter users: "))
            filter_by_age(age_to_search)
        except ValueError:
            print("Please enter a valid number for age.")

    elif filter_option == "email":
        email_to_search = input("Enter an email to filter users: ").strip()
        filter_by_email(email_to_search)

    else:
        print("Filtering by that option is not yet supported.")