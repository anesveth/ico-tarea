from flask import *
from web3 import Web3
environment='development'

app = Flask(__name__)
app.config['ENV'] = 'development'

web3infura = Web3(Web3.HTTPProvider('https://goerli.infura.io/v3/45ae0e73da314ca8b136c8712f74c69a'))
owl_token_contract = '0xE8701a8832B09A0A15Fa166ba3A6Ea3e91d116e6'

@app.route("/", methods=["POST","GET"])
def index():
    if request.method=="POST":
        account_name = request.form['account_name']
        pk = request.form['pk']
        tokennumber = request.form['tokennumber']
        print(account_name)
        print(pk)
        print(tokennumber)
        try:
            nonce = web3infura.eth.getTransactionCount(account_name)

            tx = {
                'nonce': nonce,
                'to' : owl_token_contract,
                'value': web3infura.toWei(tokennumber,'ether'),
                'gas': 87000,
                'gasPrice': web3infura.toWei(40,'gwei')
            }

            signed_tx = web3infura.eth.account.sign_transaction(tx, pk)
            tx_transaction = web3infura.eth.sendRawTransaction(signed_tx.rawTransaction)
            print(tx_transaction)

            return redirect('success')
        except:
            return redirect(url_for('error'))
    return render_template('index.html')

@app.route("/success", methods=["POST","GET"])
def success():
    return render_template('success.html')

@app.route("/error", methods=["POST","GET"])
def failure():
    return render_template('error.html')

if __name__ == "__main__":
    debuging=True
    
    app.run(host="0.0.0.0",port=8081,debug=True)