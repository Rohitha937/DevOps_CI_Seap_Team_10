def add_bid(current_bid, new_bid):
    if new_bid > current_bid:
        return new_bid
    return current_bid


def get_winner(bidder, bid_amount):
    return {
        "winner": bidder,
        "amount": bid_amount
    }


def is_valid_bid(current_bid, new_bid):
    return new_bid > current_bid


if __name__ == "__main__":
    print("Online Auction Management System")

    current_bid = 1000
    new_bid = 1500

    highest_bid = add_bid(current_bid, new_bid)

    print("Highest Bid:", highest_bid)
    print("Winner:", get_winner("Rohitha", highest_bid))
    print("Auction Status: Active")