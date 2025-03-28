import art

def find_highest_bid(bidding_dictionary):
    highest_value = 0
    matching_key = "key"

    for bidder in bidding:
        if bidding[bidder] > highest_value:
            highest_value = bidding[bidder]
            matching_key = bidder

    print(f"The winner is {matching_key} with ${bidding[matching_key]} bid.")

print(art.logo)
print("Welcome to the Blind Auction")

answer = "yes"
bidding = {}

while answer != "no":
    name = input("What's your name?: ")
    bid = int(input("What's your bid?: $"))
    bidding[name] = bid
    answer = input("Is here anyone else who wants to participate? Type 'yes' or 'no': ").lower()
    print("\n" * 20)

# print(bidding)
# maximum_bid = max(bidding, key=bidding.get)

find_highest_bid(bidding)


