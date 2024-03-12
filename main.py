from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo

Auction_Dictionary = {}

print(logo)

Bid_Again = "yes"

while(Bid_Again == "yes"):
   Name = input("What is your name?: ")
   Bid_Prince = int(input("What is your bid?: "))

   Auction_Dictionary[Name] = Bid_Prince
  
   Bid_Again = input("Are there any other bidders? Type 'yes' or 'no'")
   clear()

Highest_Bid = -1
Highest_Key = -1
for key in Auction_Dictionary:
  if(Auction_Dictionary[key] > Highest_Bid):
    Highest_Bid = Auction_Dictionary[key]
    Highest_Key = key
  
print(f"The winner is {Highest_Key} with a bid price of ${Highest_Bid}")  