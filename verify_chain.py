import pdb

blockchain = [[[1]], [[1], 2.0], [[[1], 2.0], 3.0], [
    [[[1], 2.0], 3.0], 4.0], [[[[[1], 2.0], 3.0], 4.0], 5.0]]


def verify_chain():
    """Check that first element of any block matches entire previous block's value."""
    for block in blockchain:
        pdb.set_trace()
        print(f'Number: {blockchain.index(block)}')
        print(f'Current val: {block}')
        print(f'First element: {block[0]}')
        print(f'Previous val: {blockchain[blockchain.index(block) - 1]}')
        if block is blockchain[0]:
            print('First block!')
            print(block)
            continue
        elif block is blockchain[1] and block[0] == blockchain[1][0]:
            print('Second block!')
        elif block[0] == blockchain[blockchain.index(block) - 1]:
            print(f'First element of CURRENT block: {block[0]}')
            print(f'PREVIOUS block: {blockchain[blockchain.index(block) - 1]}')
        else:
            print('NO MATCH!')


verify_chain()
