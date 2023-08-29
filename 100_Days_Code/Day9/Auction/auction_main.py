import os
from art import logo

print(logo)

bids = {}
is_bidding_finished = False


def find_highest_bidder(bidding_record: dict):
    highest_bid = 0
    highest_bidder = ""

    for key, value in bidding_record.items():
        if value > highest_bid:
            highest_bid = value
            highest_bidder = key
    return highest_bidder


# Loop through asking for bidders and bids and adding them to the bids Dictionary until they
# no more bidders are input
while not is_bidding_finished:
    name = input("What is your name?: ")
    price = float(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input(
        "Are there any other bidders? Type 'yes' or 'no'. ")
    if should_continue == "yes":
        os.system("cls")
    else:
        winner = find_highest_bidder(bids)
        print(f"The winnder is {winner} with a bid of ${bids[winner]: .2f}.")
        is_bidding_finished = True
