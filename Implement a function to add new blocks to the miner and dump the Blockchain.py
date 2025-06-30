import hashlib 
import time 
class Block:
    def __init__ (self, index, previous_hash, timestamp, data, nonce=0): 
        self.index = index
        self.previous_hash = previous_hash 
        self.timestamp = timestamp 
        self.data = data
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self): 
        """
            Generate a hash for the block using SHA-256. 
        """
        block_contents = f"{self.index}{self.previous_hash}{self.timestamp}{self.data}{self.nonce}"
        return hashlib.sha256(block_contents.encode()).hexdigest()
    def mine_block(self, difficulty): 
        """
        Implements proof-of-work by mining a block to match the required difficulty.
        """
        target = '0' * difficulty
        while not self.hash.startswith(target): 
            self.nonce += 1
            self.hash = self.calculate_hash() 
class Blockchain:
    def __init__ (self, difficulty=4):
        self.chain = [self.create_genesis_block()] 
        self.difficulty = difficulty
    def create_genesis_block(self): 
        """
            Create the first block of the blockchain. 
        """
        return Block(0, "0", time.time(), "Genesis Block")
    def get_latest_block(self):
        """
        Fetch the latest block in the chain. """
        return self.chain[-1]
    def add_block(self, data): 
        """
        Add a new block to the blockchain. 
        """
        latest_block = self.get_latest_block() 
        new_block = Block(
            index=latest_block.index + 1, 
            previous_hash=latest_block.hash, 
            timestamp=time.time(), data=data
        )
        new_block.mine_block(self.difficulty) 
        self.chain.append(new_block)
    def dump_blockchain(self): 
        """
            Display all blocks in the blockchain. 
        """
        for block in self.chain: 
            print(f"Index: {block.index}")
            print(f"Previous Hash: {block.previous_hash}") 
            print(f"Timestamp: {block.timestamp}") 
            print(f"Data: {block.data}")
            print(f"Nonce: {block.nonce}") 
            print(f"Hash: {block.hash}") 
            print("-" * 50)
# Example usage
if __name__ == " main ":
# Create a blockchain instance 
    my_blockchain = Blockchain()
# Add new blocks
    my_blockchain.add_block("First transaction: Alice pays Bob 50 coins.") 
    my_blockchain.add_block("Second transaction: Bob pays Charlie 20 coins.")
# Dump the blockchain print("Blockchain contents:") my_blockchain.dump_blockchain()