import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, transactions, nonce=0):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.transactions = transactions
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        data = str(self.index) + self.previous_hash + str(self.timestamp) + str(self.transactions) + str(self.nonce)
        return hashlib.sha256(data.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 4  # Number of leading zeroes for Proof of Work

    def create_genesis_block(self):
        return Block(0, "0", int(time.time()), "Genesis Block")

    def get_last_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_last_block().hash
        new_block.hash = new_block.calculate_hash()
        new_block.nonce = self.proof_of_work(new_block)
        self.chain.append(new_block)

    def proof_of_work(self, block):
        target = "0" * self.difficulty
        while block.hash[:self.difficulty] != target:
            block.nonce += 1
            block.hash = block.calculate_hash()
        return block.nonce


# Add the create_blockchain_code function to generate a blockchain code for the vote

def create_blockchain_code(user, candidate):
    blockchain = Blockchain()
    last_block = blockchain.get_last_block()

    # Construct a transaction for the vote
    transaction_data = {
        "user_id": user.id,
        "candidate_id": candidate.id,
    }

    new_block = Block(
        index=last_block.index + 1,
        previous_hash=last_block.hash,
        timestamp=int(time.time()),
        transactions=transaction_data,
    )

    # Add the new block to the blockchain
    blockchain.add_block(new_block)

    return new_block.hash
