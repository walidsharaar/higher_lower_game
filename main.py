from data import data
import random
from art import logo, vs
#todo get data from random account

def get_different_account():
    """Get data from random account"""
    return random.choice(data)

# todo format the account data
def format_data(account):
    """formating the dictionary data into printable format."""
    account_name = account["name"]
    account_descrp= account["description"]
    account_country= account["country"]
    return(f"{account_name}, a {account_descrp} , from {account_country}")


def check_answer(guess,first_account_follower,second_account_follower):

    """if statement usage to check the correct answer"""

    if first_account_follower > second_account_follower:
        return guess=="a"
    else:
        return guess =="b"



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

guess = input("Who has the more followers? A or B  ").lower()
first_account_follower = first_account["follower_count"]
second_account_follower = second_account["follower_count"]

# todo check the user guess
is_right = check_answer(guess,first_account_follower,second_account_follower)
score = 0
if is_right:
    score +=1
    print(f"You guess right! your score is {score}")
else:
    print(f"Sorry you are wrong. Your score is : {score}")


