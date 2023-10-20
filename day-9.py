import os

gavel = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         |_________|
                         `---------`
                       .-------------.
                      |_______________|
'''

print(gavel)
print("Welcome to the secret auction.")

bids = {}
bidding = True

while bidding:
    bidder = input("What is your name: ").title()
    bids[bidder] = int(input("What's your bid? "))

    add_bidder = input("Are there any other bidders? Type 'yes' or 'no': ")
    if add_bidder == 'no':
        bidding = False

    os.system('cls')

highest_bidder = max(bids, key=bids.get)
highest_bid = max(bids.values())

print(f"The winner is {highest_bidder} with a bid of {highest_bid}")
