
import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, data):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        data = str(self.index) + str(self.previous_hash) + str(self.timestamp) + str(self.data)
        return hashlib.sha256(data.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "0", int(time.time()), "Genesis Block")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

# Create a blockchain and add some blocks
my_blockchain = Blockchain()
my_blockchain.add_block(Block(1, my_blockchain.get_latest_block().hash, int(time.time()), "Data 1"))
my_blockchain.add_block(Block(2, my_blockchain.get_latest_block().hash, int(time.time()), "Data 2"))
my_blockchain.add_block(Block(3, my_blockchain.get_latest_block().hash, int(time.time()), "Data 3"))
my_blockchain.add_block(Block(4, my_blockchain.get_latest_block().hash, int(time.time()), "Data 4"))

# Print the blockchain
for block in my_blockchain.chain:
    print(f"Index: {block.index}")
    print(f"Previous Hash: {block.previous_hash}")
    print(f"Timestamp: {block.timestamp}")
    print(f"Data: {block.data}")
    print(f"Hash: {block.hash}")
    print("\n")
