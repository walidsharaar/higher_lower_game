from data import data
import random
from art import logo, vs

#todo display art
print(logo)

# todo generate random from the list of data

first_account= random.choice(data)
second_account= random.choice(data)
# ensure two accounts are different
if first_account == second_account:
    second_account=random.choice(data)

# todo format the account data

account_name =first_account["name"]
account_descrp= first_account["description"]
account_country= first_account["country"]

print(f"{account_name}, a {account_descrp} , from {account_country}")



