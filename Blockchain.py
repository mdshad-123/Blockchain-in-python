import datetime
import json
import hashlib
from flask import Flask, jsonify

class Blockchain:
    def _init_(seLf):
        seLf.chain = []
        seLf.create_blockchain(proof=1, previous_hash='0')

    def create_Blockchain(seLf, index, timestmp, proof, previous_hash):
        block = {
        'index': len(seLf.chain) + 1,
        'timestamp':str(datetime.datetime.now()),
        'proof': proof,
        'previous_hash': previous_hash
        }

        seLf.chain.append(block)
        return block

    def get_previous_block(seLf):
        last_block = seLf.chain[-1]
        return last_block

    def proof_of_work(seLf, previous_proof):
        # miners proof submitted
        new_proof = 1
        # status of proof of work
        check_proof = False
        while check_proof is False:
        # problem and algorithm based off the previous proof and new proof
         hash_opreation=hashlib.sha256(str(new_proof ** 2 - previous_proof **2).encode()).hexdigest()
        # check miners solution to problem, by using miners proof in cryptographic encryption
        # if miner proof results in 4 leading zero's in the hash operation, then:
        if hash_opreation[:4]=='0000': 
            check_proof=True
        else:
            # if miners solution is wrong, give mine another chance untill correct
            new_proof += 1
            return new_proof

# generate a hash of  an entire block
def hash(self,block):
    encoded_block = json.dumps(block, sort_keys=True).encode()
    return hashlib.sha256(encoded_block).hexdigest()

# check if the blockchain is valid
def is_chain_valid(seLf, chain):
# get the first block in the chain and it serves as the previuos block
    previous_block = chain[0]
# an index of the blocks in the chain for iteration
    block_index = 1
    while block_index < len(chain):
    # get the currrent block
        block = chain[block_index]
# check if the current block link to previous block has the same as the hash of the previous block
    if block["previous_hash"] !=seLf.hash(previous_block):
            return False
    
    # get the previous proof from the previous block
    previous_proof = previous_block['proof']
    # get the current proof from the current block
    current_proof = block['proof']

    # run the proof data through the algorithm
    hash_operation = hashlib.sha256(str(current_proof ** 2 - previous_proof ** 2).encode()).hexdigest()

    # check if hash operation is invalid
    if hash_operation[:4] !='0000':
        return False
    # set the previous block to the  current block after running validation on current block
    previous_block = block
    block_index += 1
    return True

app = Flask(__name__)

blockchain = Blockchain()

@app.route('/mine_block',methods=['GET'])
def mine_block():
    # get the data we need to create a block
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    block = blockchain.create_blockchain(proof, previous_hash)
    response = {'message': 'Block mined',
            'index': block['index'],
            'timestamp': block['timestamp'],
            'proof': block['proof'],
            'previous_hash': block['previous_hass']}
    return jsonify(response), 200

@app.route('/get_chain', methods=['GET'])
def get_chain():
    response = {'chain':blockchain.chain,
                'length': len(blockchain.chain)}
    return jsonify(response), 200

@app.route('/is_blockchain-valid', methods=['GET'])
def is_blockchain_valid():

    valid = blockchain.is_chain_valid(blockchain.chain)
    
    if valid:
        response = {'message': "yes,The blockchain is valid."}

    else:
        response = {'message': 'No, The Blockchain is not valid.'}
        
        return jsonify(response), 200
    app.run (host='0.0.0.0,port=5000')