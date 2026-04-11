import os

def clear():
    """Clears the terminal screen - works on Windows, Mac, and Linux"""
    os.system('cls' if os.name == 'nt' else 'clear')

bids = {}
bidding_finished = False

while not bidding_finished:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  bids[name] = price
  
  # Clear the screen immediately after recording the bid
  clear()
  
  should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  if should_continue == "no":
    bidding_finished = True
  elif should_continue != "yes":
    print("Invalid input! Please type 'yes' or 'no'.")
    bidding_finished = True

# Final clear before showing winner (optional, makes it cleaner)
clear()

highest_bid = 0
winner = ""
for bidder in bids:
  bid_amount = bids[bidder]
  if bid_amount > highest_bid:
    highest_bid = bid_amount
    winner = bidder
    
print(f"The winner is {winner} with a bid of ${highest_bid}.")