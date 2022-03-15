# My first simple Blockchain in Python

import hashlib


class MyCoinBlock:
    def __init__(self, previous_block_hash, transaction_list):  # self - экземпляр каждого объекта
        self.previous_block_hash = previous_block_hash  # ссылка на предыдущий блок
        self.transaction_list = transaction_list  # список транзакций, совершенных в текущем блоке

        self.block_data = f"{' - '.join(transaction_list)} - {previous_block_hash}"
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()


class Blockchain:
    def __init__(self):
        self.chain = []
        self.generate_genesis_block()

    def generate_genesis_block(self):
        self.chain.append(MyCoinBlock("0", ['Genesis Block']))

    def create_block_from_transaction(self, transaction_list):
        previous_block_hash = self.last_block.block_hash
        self.chain.append(MyCoinBlock(previous_block_hash, transaction_list))

    def display_chain(self):
        for i in range(len(self.chain)):
            print(f"Data {i + 1}: {self.chain[i].block_data}")
            print(f"Hash {i + 1}: {self.chain[i].block_hash}\n")

    @property
    def last_block(self):
        return self.chain[-1]

t1 = "Max sends 23.1 MC to Joe"
t2 = "Joe sends 12.5 MC to Adam"
t3 = "Adam sends 31.2 MC to Bob"
t4 = "Bob sends 21.5 MC to Charlie"
t5 = "Charlie sends 10.2 MC to Yauheni"
t6 = "Yauheni sends 11.1 MC to Max"

myblockchain = Blockchain()

myblockchain.create_block_from_transaction([t1, t2])
myblockchain.create_block_from_transaction([t3, t4])
myblockchain.create_block_from_transaction([t5, t6])

myblockchain.display_chain()
