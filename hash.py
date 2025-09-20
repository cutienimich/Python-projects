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
       return hashlib.sha256(f"{self.index}{self.previous_hash}{self.timestamp}{self.data}".encode()).hexdigest()
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
blockchain = Blockchain()
blockchain.add_block(Block(1, "", int(time.time()), "First Block"))
blockchain.add_block(Block(2, "", int(time.time()), "Second Block"))
# Print the blockchain
for block in blockchain.chain:
   print(f"Index: {block.index}")
   print(f"Previous Hash: {block.previous_hash}")
   print(f"Timestamp: {block.timestamp}")
   print(f"Data: {block.data}")
   print(f"Hash: {block.hash}\n")