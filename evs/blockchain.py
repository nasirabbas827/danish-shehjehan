import hashlib
import time
from .models import VoteBlocks

class Block:
    def __init__(self, index, previous_hash, transactions, timestamp):
        self.index = index
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.timestamp = timestamp
        self.nonce = 0

    def calculate_hash(self):
        data = str(self.index) + self.previous_hash + str(self.transactions) + str(self.timestamp) + str(self.nonce)
        return hashlib.sha256(data.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "0", "Genesis Block", int(time.time()))

    def get_last_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_last_block().calculate_hash()
        new_block.nonce = self.proof_of_work(new_block)
        self.chain.append(new_block)

    def proof_of_work(self, block, difficulty=2):
        while True:
            hash_attempt = block.calculate_hash()
            if hash_attempt[:difficulty] == "0" * difficulty:
                return block.nonce
            block.nonce += 1

    def add_block_to_database(self, user, candidate):
        # Create a transaction for the vote
        transaction = {
            'voter': user.username,
            'candidate': candidate.name,
            'timestamp': int(time.time())
        }

        # Add the transaction to a new block
        new_block = Block(len(self.chain), self.get_last_block().calculate_hash(), transaction, int(time.time()))
        self.add_block(new_block)

        # Save the blockchain code in the database
        blockchain_code = new_block.calculate_hash()
        blockchain_entry = VoteBlocks(user=user, candidate=candidate, blockchain_code=blockchain_code)
        blockchain_entry.save()
        return blockchain_code
