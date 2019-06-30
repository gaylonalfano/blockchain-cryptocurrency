# ~/Code/blockchain_cryptocurrency/blockchain.py
genesis_block = {"previous_hash": "", "index": 0, "transactions": []}
blockchain = [genesis_block]
open_transactions = []
owner = "Gaylon"
participants = {owner}


def hash_block(block):
    """Returns a hash value for any given block"""
    return "-".join([str(block[key]) for key in block])


# def get_balance(participant):
#     """Returns the current amount of funds a participant has on balance.

#     Arguments:
#         :participant: The specified participant.
#     """
#     tx_sender = [[transaction['amount'] for transaction in block['transactions'] if participant is transaction['sender'] for block in blockchain]


def get_last_blockchain_value():
    """Returns the last value of the current blockchain.
    Returns None if blockchain is empty."""
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_transaction(recipient, sender=owner, amount=1.0):
    """Store transaction details inside a dictionary, which
    is stored within a list. Store the sender and recipient
    to the participants set if unique.

    Arguments:
        :sender: The sender of the coins.
        :recipient: The recipient of the coins.
        :amount: The amount of coins sent with the transaction. Default = 1.0.
	    :participants: A unique set of participants in the blockchain.
    """
    transaction = {"sender": sender, "recipient": recipient, "amount": amount}
    open_transactions.append(transaction)
    participants.add(sender)
    participants.add(recipient)


def mine_block():
    """Store all open transactions into a new block
    and add new block to existing Blockchain."""
    last_block = blockchain[-1]
    # Hash the previous block by concat dict values
    hashed_block = hash_block(last_block)
    print(hashed_block)

    block = {
        "previous_hash": hashed_block,
        "index": len(blockchain),
        "transactions": open_transactions,
    }
    # Add block to existing blockchain
    blockchain.append(block)
    return True


def get_transaction_recipient_value():
    """Returns the input of the user for the transaction recipient and
    transaction amount."""
    tx_recipient = input("Enter the recipient for the transaction: ")
    tx_amount = float(input("Please enter your transaction amount: "))
    return (tx_recipient, tx_amount)


def get_user_choice():
    """Returns the input of the user's choice (e.g., add value or print blockchain)."""
    user_input = input("Your choice: ")
    return user_input


def print_blockchain_elements():
    """Prints all elements of the current blockchain"""
    for block in blockchain:
        print("Outputting Block")
        print(block)
    else:
        print("-" * 20)


def verify_chain():
    """Check that first element of any block matches entire previous block's value."""
    for (index, block) in enumerate(blockchain):
        if index == 0:
            continue
        if block["previous_hash"] != hash_block(blockchain[index - 1]):
            return False
    return True


waiting_for_input = True

while waiting_for_input:
    print("Please choose:")
    print("1: Add a new transaction value")
    print("2: Mine a new block")
    print("3: Output the blockchain blocks")
    print("4: Output participants")
    print("h: Manipulate the chain")
    print("q: Quit")
    user_choice = get_user_choice()
    if user_choice == "1":
        tx_data = get_transaction_recipient_value()
        recipient, amount = tx_data
        # Add the transaction amount to the blockchain
        add_transaction(recipient, amount=amount)
        print(open_transactions)
    elif user_choice == "2":
        if mine_block():
            open_transactions = []
    elif user_choice == "3":
        print_blockchain_elements()
    elif user_choice == "4":
        print(participants)
    elif user_choice == "h":
        # Make sure you can't hack if blockchain is empty
        if len(blockchain) >= 1:
            blockchain[0] = {
                "previous_hash": "",
                "index": 0,
                "transactions": [
                    {"sender": "Ashley", "recipient": "Archie", "amount": 72}
                ],
            }
    elif user_choice == "q":
        # This will exit the loop since it's condition will be False
        waiting_for_input = False
    else:
        print("Input was invalid, please pick a value from the list!")
    if not verify_chain():
        print_blockchain_elements()
        print("Invalid blockchain!")
        # Break the loop
        break
else:
    print("User left! While loop is finished.")


print("Done!")
