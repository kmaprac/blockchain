server=1 
rpcuser=your_rpc_user
rpcpassword=your_rpc_password 
rpcport=8332 
# rpcallowip=127.0.0.1
# bitcoind –daemon 
# !pip install requests 
import requests 
import json
from requests.auth import HTTPBasicAuth # Bitcoin Core RPC settings
rpc_url = "http://127.0.0.1:8332"
rpc_user = "your_rpc_user" # Replace with your RPC username rpc_password = "your_rpc_password" # Replace with your RPC password # Define a function to send RPC requests
def bitcoin_rpc(method, params=None):
    headers = {'content-type': 'application/json'} # Prepare the RPC request payload
    payload = { 
        "jsonrpc": "1.0",
        "id": "curltest", 
        "method": method, 
        "params": params or []
    }
    # Send the POST request
    response = requests.post(rpc_url, data=json.dumps(payload), headers=headers, auth=HTTPBasicAuth(rpc_user, rpc_password))
    if response.status_code == 200: 
        return response.json()
    else:
        raise Exception(f"Error: {response.status_code} - {response.text}")
# Example 1: Get the current block count 
block_count = bitcoin_rpc("getblockcount") 
print("Block Count:", block_count['result'])
# Example 2: Get blockchain information 
blockchain_info = bitcoin_rpc("getblockchaininfo") 
print("Blockchain Info:", blockchain_info['result'])
# Example 3: Get the wallet balance 
wallet_balance = bitcoin_rpc("getbalance") 
print("Wallet Balance:", wallet_balance['result'])
# Example 4: Get the current network difficulty 
difficulty = bitcoin_rpc("getdifficulty") 
print("Network Difficulty:", difficulty['result'])
# Example 5: Send a raw transaction (assuming you have a raw transaction to send) 
# # raw_tx = "<raw_transaction_data>"
# tx_id = bitcoin_rpc("sendrawtransaction", [raw_tx]) 
# # print("Transaction ID:", tx_id['result'])