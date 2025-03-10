# Import and logo
from art import logo
print(logo)


# define a function that prints out the highest bidder
def find_highest_bidder(bidding_dictionary):
    highest_bid = 0
    winner = ""
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.")

# create an empty dictionary to store the bids
auction = {}

# define a parameter whose value drive the coninuation or otherwise of the loop
keep_bidding = True

#while loop
while keep_bidding:
    # Ask the user for input
    name = input("What is your name?: ")
    bid = float(input("What is your bid?: $"))
    auction[name] = bid
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'\n").lower()
    if other_bidders == 'yes':
        print("\n" * 100)
    elif other_bidders == "no":
        keep_bidding = False

print(f"These are the bids that came in: {auction}")
find_highest_bidder(auction)

