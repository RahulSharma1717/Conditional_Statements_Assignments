# Alice, Bob and Charlie are bidding on an artifact at an auction.
#
# Alice bids A rupees, Bob bids B rupees and Charlie bids C rupees (where A, B and C are distinct).
#
# According to the rule of the auction, the one who bids the highest amount will win the auction. Determine who will win the auction.

def auction_bidding():
    try:
        A = float(input("Enter the bid prediction by Alice: "))
        B = float(input("Enter the bid prediction by Bob: "))
        C = float(input("Enter the bid prediction by Charlie: "))

        if A != B and B != C and A !=C:
            if A > B and A > C:
                print("Alice wins the auction")
            elif B > A and B > C:
                print("Bob wins the auction")
            else:
                print("Charlie wins the auction")
        else:
            print("Enter distinct bids for Alice, Bob and Charlie")
    except ValueError:
        print("Invalid Input! Please enter numeric values as input")

auction_bidding()



"""Output:
Enter the bid prediction by Alice: 13.65
Enter the bid prediction by Bob: 13.42
Enter the bid prediction by Charlie: 13.58
Alice wins the auction
"""
