# Setup
from web3 import Web3
import requests
import json

ALCHEMY_API_KEY = '2zQoIf1Cx9A95Mwo0t6YCjV6YrNpQh1b'

# Alchemy API URL
alchemy_url = f"https://eth-sepolia.g.alchemy.com/v2/{ALCHEMY_API_KEY}"
web3 = Web3(Web3.HTTPProvider(alchemy_url))

# Print if web3 is successfully connected
print(web3.is_connected())

# Test - Get the latest block number
latest_block = web3.eth.get_block("latest")
print(latest_block)

# Verify if the connection is successful
if web3.is_connected():
    print("-" * 50)
    print("Connection Successful")
    print("-" * 50)
else:
    print("Connection Failed")


# Contract address for which you want to get the ABI
contract_address = "0xF648c345d597376C9aFe8FeB531d5b1285165259"


# Set your Etherscan API Key here
# ETHERSCAN_API_KEY = 'SQRBFK92VSFVFGM3ZZVCQT3AKM3XACMQSA'

# URL for the Etherscan API endpoint to get contract ABI
# etherscan_url = f"https://api.etherscan.io/api?module=contract&action=getabi&address={contract_address}&apikey={ETHERSCAN_API_KEY}"

# Make an API request to Etherscan
#response = requests.get(etherscan_url)

# Parse the response JSON
#data = response.json()

# Check if the request was successful
#if data['status'] == '1' and data['message'] == 'OK':
#    # ABI is returned as a JSON-encoded string, so we need to parse it
#    contract_abi = json.loads(data['result'])
#    print("Contract ABI:")
#    print(json.dumps(contract_abi, indent=2))
#else:
#    print("Error fetching contract ABI:", data['result'])


# Initialize the address calling the functions/signing transactions
caller = "0xE42400B2bAB460ce8924f90Ca7C1Ca870053D56E"  # Ethereum address from MetaMask wallet
private_key = "dfc457669132f93158dcbaf5b1c42b5c3a702d4725cb1834eef6164fcfee459c"  # PRIVATE_KEY - Metamask. To sign the transaction

# Initialize address nonce
nonce = web3.eth.get_transaction_count(caller)

# Initialize contract ABI and address
#abi = '[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"balanceLeft","type":"uint256"}],"name":"balance","type":"event"},{"inputs":[{"internalType":"address payable","name":"recipient","type":"address"}],"name":"destroy","outputs":[],"stateMutability":"nonpayable","type":"function"}]'
#abi = '[{"inputs":[{"internalType":"string","name":"initialSentence","type":"string"}],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"getSentence","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"newSentence","type":"string"}],"name":"setSentence","outputs":[],"stateMutability":"nonpayable","type":"function"}]'
abi = '[{"inputs":[{"internalType":"string","name":"initialSentence","type":"string"}],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"getSentence","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"newSentence","type":"string"}],"name":"setSentence","outputs":[],"stateMutability":"nonpayable","type":"function"}]'
# contract_address = "0xE7F2321B685C439E292B01466aB292539e96C029"

# Simple sentence storage contract
contract_address = "0xF648c345d597376C9aFe8FeB531d5b1285165259" # CONTRACT_ADDRESS -  Deployed contracts tab in Remix

try:
    parsed_abi = json.loads(abi)
    print("ABI is valid JSON.")
except json.JSONDecodeError as e:
    print(f"Invalid JSON: {e}")

# Parse the ABI string to a Python object
parsed_abi = json.loads(abi)

# Then use the parsed ABI to create the contract instance
contract = web3.eth.contract(address=contract_address, abi=parsed_abi)

# Now, parsed_abi should be a list of dictionaries
if isinstance(parsed_abi, list):
    # Extract functions from the ABI
    functions = [item for item in parsed_abi if item.get('type') == 'function']

    # Iterate over the functions and print details
    for func in functions:
        func_name = func.get('name', 'Unnamed function')
        inputs = func.get('inputs', [])
        input_details = ', '.join([f"{inp['type']} {inp['name']}" for inp in inputs])
        print(f"Function name: {func_name}({input_details})")
else:
    print("The ABI was not parsed into a list as expected.")

# Create the contract instance
contract = web3.eth.contract(address=contract_address, abi=parsed_abi)

# Example function call (Make sure the function exists in your ABI)
try:
    # Replace 'getSentence' with an actual function from your contract's ABI
    quote = contract.functions.getSentence().call()
    print("The famous quote is:", quote)
    pass  # Replace or remove this pass statement with your function call
except Exception as e:
    print(f"Error calling function: {e}")



