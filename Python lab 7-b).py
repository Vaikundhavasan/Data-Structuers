def findHighestBidder(x):
    highestBid = 0
    winner = ""
    for i in x:
        bidAmount = x[i]
        if(bidAmount > highestBid):
            highestBid = bidAmount
            winner = i
    print(f"The Winner is {winner} with bid of {highestBid} ")

print("Implement Applications using Dictionaries")
print(".........................................")
bid = {}
bidding_finished = False
while(bidding_finished == False):
    name =  input("Enter Your Name : ")
    price = int(input("Enter Your Bid : "))
    bid[name] = price
    should_continue = int(input("Are There any other bidders? 1.Yes or 2.No : "))
    if(should_continue==2):
        bidding_finished = True
        findHighestBidder(bid)
