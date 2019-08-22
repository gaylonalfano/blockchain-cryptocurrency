# ~/Code/blockchain_cryptocurrency/blockchain.py
MINING_REWARD = 10
genesis_block = {"previous_hash": "", "index": 0, "transactions": []}
blockchain = [genesis_block]
open_transactions = []
owner = "Gaylon"
participants = {owner}


def hash_block(block):
    """Returns a hash value for any given block"""
    return "-".join([str(block[key]) for key in block])


def get_balance(participant):
    """Returns the current amount of funds a participant has on balance.

    Arguments:
        :participant: The participant we want to calculate the current balance
    """
    # Fetch a list of all sent coin amounts for the given person (empty lists are returned if the person was NOT the sender)
    # This fetches sent amounts of transactions that were already included in blocks of the blockchain
    tx_sender = [
        [
            transaction["amount"]
            for transaction in block["transactions"]
            if participant == transaction["sender"]
        ]
        for block in blockchain
    ]
    # Fetch a list of all sent coin amounts for the given person (empty lists are returned if the person was NOT the sender)
    # This fetches sent amounts of open transactions (to avoid double spending)
    open_tx_sender = [
        transaction["amount"]
        for transaction in open_transactions
        if transaction["sender"] == participant
    ]
    tx_sender.append(open_tx_sender)
    amount_sent = 0
    for tx in tx_sender:
        amount_sent += sum(tx)
    # This fetches received coin amounts of transactions that were already included in blocks of the blockchain
    # We ignore open transactions here because you shouldn't be able to spend coins before the transaction was confirmed + included in a block
    tx_recipient = [
        [
            transaction["amount"]
            for transaction in block["transactions"]
            if participant == transaction["recipient"]
        ]
        for block in blockchain
    ]
    amount_received = 0
    for tx in tx_recipient:
        if len(tx) > 0:
            amount_received += sum(tx)

    # starting_balance = 100
    # current_balance = starting_balance + (amount_received - amount_sent)
    # Return the total balance
    return amount_received - amount_sent


def get_last_blockchain_value():
    """Returns the last value of the current blockchain.
    Returns None if blockchain is empty."""
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def verify_transaction(transaction):
    """Returns True if sender has enough funds to send a transaction. False if not."""
    return get_balance(transaction["sender"]) >= transaction["amount"]


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
    if verify_transaction(transaction):
        open_transactions.append(transaction)
        participants.add(sender)
        participants.add(recipient)
        return True
    return False


def mine_block():
    """Store all open transactions into a new block
    and add new block to existing Blockchain."""
    last_block = blockchain[-1]
    # Hash the previous block by concat dict values
    hashed_block = hash_block(last_block)
    print(hashed_block)
    reward_transaction = {
        "sender": "MINING",
        "recipient": owner,
        "amount": MINING_REWARD,
    }
    # Create a copy of open_transactions to add reward to
    copied_transactions = open_transactions[:]
    copied_transactions.append(reward_transaction)
    block = {
        "previous_hash": hashed_block,
        "index": len(blockchain),
        "transactions": copied_transactions,
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


def verify_transactions():
    """Returns True if all open transactions are valid."""
    return all([verify_transaction(tx) for tx in open_transactions])


waiting_for_input = True

while waiting_for_input:
    print("Please choose:")
    print("1: Add a new transaction value")
    print("2: Mine a new block")
    print("3: Output the blockchain blocks")
    print("4: Output participants")
    print("5: Check transactions validity")
    print("h: Manipulate the chain")
    print("q: Quit")
    user_choice = get_user_choice()
    if user_choice == "1":
        tx_data = get_transaction_recipient_value()
        recipient, amount = tx_data
        # Add the transaction amount to the blockchain if verified
        if add_transaction(recipient, amount=amount):
            print("Added transaction!")
        else:
            print("Transaction failed!")
        print(open_transactions)
    elif user_choice == "2":
        if mine_block():
            open_transactions = []
    elif user_choice == "3":
        print_blockchain_elements()
    elif user_choice == "4":
        print(participants)
    elif user_choice == "5":
        if verify_transactions():
            print("All transactions are valid.")
        else:
            print("There are invalid transactions!")
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
    print(f"Balance of {owner}: {get_balance(owner):6.2f}")
else:
    print("User left! While loop is finished.")


print("Done!")
