# Import and logo
from art import logo
print(logo)

# create an empty dictionary to store the bids
auction = {}

keep_bidding = True

while keep_bidding:
    # Ask the user for input
    name = input("What is your name?: ")
    bid = input("What is your bid?: $")
    auction[name] = float(bid)
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'\n")
    if other_bidders == 'yes':
        print("\n" * 100)
    else:
        keep_bidding = False

max_key = max(auction, key = auction.get)

print(f"These are the bids that came in: {auction}")
print(f"The winner is {max_key} with a bid of ${auction[max_key]}")
