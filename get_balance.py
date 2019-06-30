# My attempt at the get_balance() function

blockchain = [
    {
        "previous_hash": "-0-[]",
        "index": 1,
        "transactions": [
            {"sender": "Gaylon", "recipient": "Adrian", "amount": 8.0},
            {"sender": "Gaylon", "recipient": "Aaron", "amount": 5.0},
            {"sender": "Gaylon", "recipient": "Ashley", "amount": 37.0},
            {"sender": "Gaylon", "recipient": "Adrian", "amount": 11.0},
        ],
    },
    {
        "previous_hash": "-0-[]-1-[{'sender': 'Gaylon', 'recipient': 'Adrian', 'amount': 8.0}, {'sender': 'Gaylon', 'recipient': 'Aaron', 'amount': 5.0}, {'sender': 'Gaylon', 'recipient': 'Ashley', 'amount': 37.0}, {'sender': 'Gaylon', 'recipient': 'Adrian', 'amount': 11.0}]",
        "index": 2,
        "transactions": [
            {"sender": "Gaylon", "recipient": "Archie", "amount": 5.0},
            {"sender": "Gaylon", "recipient": "Aaron", "amount": 10.0},
            {"sender": "Gaylon", "recipient": "Gaylon", "amount": 40.0},
        ],
    },
]

participants = {"Aaron", "Archie", "Gaylon", "Adrian", "Ashley"}

# print(blockchain)
# tx_sender = [block for block in blockchain]
# print(tx_sender)


def get_balance(participant):
    tx_recipient = []
    for block in blockchain:
        for transaction in block["transactions"]:
            if participant == transaction["recipient"]:
                tx_recipient.append(transaction["amount"])
    print(tx_recipient)
    print(sum(tx_recipient))


# get_balance("Adrian")

# print(blockchain[0]["transactions"]

lc_test = [[tx["amount"] for tx in block["transactions"]] for block in blockchain]

# lc_test = [
#     transaction["amount"]
#     for transaction in [block["transaction"]]
#     for block in blockchain
# ]
print(lc_test)
