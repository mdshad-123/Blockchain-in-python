
import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

def calculate_hash(index, previous_hash, timestamp, data):
    value = str(index) + str(previous_hash) + str(timestamp) + str(data)
    return hashlib.sha256(value.encode()).hexdigest()

def create_genesis_block():
    return Block(0, "0", int(time.time()), "Genesis Block", calculate_hash(0, "0", int(time.time()), "Genesis Block"))

def create_new_block(previous_block, data):
    index = previous_block.index + 1
    timestamp = int(time.time())
    hash = calculate_hash(index, previous_block.hash, timestamp, data)
    return Block(index, previous_block.hash, timestamp, data, hash)

# Create the blockchain and add blocks
blockchain = [create_genesis_block()]
previous_block = blockchain[0]

num_blocks_to_add = 10

for i in range(num_blocks_to_add):
    new_data = f"This is block {i + 1}"
    new_block = create_new_block(previous_block, new_data)
    blockchain.append(new_block)
    previous_block = new_block
    print(f"Block: l{new_block.index} has been added to the blockchain!")
    print(f"Hash: {new_block.hash}\n")
