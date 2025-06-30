import hashlib 
import time
def mine(block_data, difficulty):
    prefix = '0' * difficulty 
    # Define the difficulty level (number of leading zeros)
    nonce = 0 # Nonce starts at 0
    print("Mining in progress...") 
    start_time = time.time()
    while True:
        # Combine the block data with the nonce and hash it 
        block_hash = hashlib.sha256((block_data +
        str(nonce)).encode()).hexdigest()
        # Check if the hash matches the difficulty 
        if block_hash.startswith(prefix):
            elapsed_time = time.time() - start_time 
            print(f"Block mined successfully!") 
            print(f"Hash: {block_hash}") 
            print(f"Nonce: {nonce}")
            print(f"Time taken: {elapsed_time:.2f} seconds") 
            return block_hash, nonce
        # Increment the nonce and try again 
        nonce += 1
# Example usage
block_data = "Sample Block Data"
difficulty = 5 # Difficulty level (higher value means more work) 
mine(block_data, difficulty)