from data import data
import random
from art import logo, vs

# todo format the account data
def format_data(account):
    """formating the dictionary data into printable format."""
    account_name = account["name"]
    account_descrp= account["description"]
    account_country= account["country"]
    return(f"{account_name}, a {account_descrp} , from {account_country}")


#todo display art
print(logo)

# todo generate random from the list of data

first_account= random.choice(data)
second_account= random.choice(data)
# ensure two accounts are different
if first_account == second_account:
    second_account=random.choice(data)

print(f"Compare A : {format_data(first_account)}")
print(vs)
print(f"Compare B : {format_data(second_account)}")

#todo ask user guess

guess = input("Who has the more followers? A or B").lower()



