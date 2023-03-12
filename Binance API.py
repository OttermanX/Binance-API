from flask import Flask, render_template, request, flash, redirect, jsonify
from binance.client import Client
from binance.enums import *
import websocket
import json











app = Flask(__name__, static_url_path='/static', static_folder='static')
app.secret_key = b'somelongrandomsdsfsstring'







#def on_message(ws, message):
 #   json_message = json.loads(message)
  #  eth_price = json_message["c"]
   # print(f"Current ETH price: {eth_price}")

#symbol = "ethusdt"
#socket = f"wss://stream.binance.com:9443/ws/{symbol}@ticker"
#ws = websocket.WebSocketApp(socket, on_message=on_message)

# start the WebSocket connection
#ws.run_forever()


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        global client
        api_key = request.form['key']
        api_secret = request.form['secret']
        client = Client(api_key, api_secret)
        usdtbalance = client.get_asset_balance(asset="USDT")['free']
        lrcbalance = client.get_asset_balance(asset="LRC")['free']
        exchange_info = client.get_exchange_info()
        symbols = exchange_info['symbols']
        account = client.get_account()
        balances = account['balances']
        print(request.form)
    else:
        usdtbalance = 'API Required'
        lrcbalance = 'API Required'
        exchange_info = {}
        symbols = []
        account = {}
        balances = [] 
    return render_template('index.html', usdtbalance=usdtbalance, my_balances=balances, symbols=symbols, lrcbalance=lrcbalance)




@app.route('/buy', methods=['GET', 'POST'])
def buy():
    print(request.form)
    try:
        usdtbalance = client.get_asset_balance(asset="USDT")['free']
        lrc_price = client.get_symbol_ticker(symbol='LRCUSDT')['price']
        
        quant = int(float(usdtbalance) / float(lrc_price))
        order = client.create_order(symbol=request.form['bsymbol'], 
            side=SIDE_BUY,
            type=ORDER_TYPE_MARKET,
            quantity=quant)
    except Exception as e:
        flash(e.message, "error")
    return redirect('/')

@app.route('/sell', methods=['GET', 'POST'])
def sell():
    print(request.form)
    try:      
        lrcbalance = client.get_asset_balance(asset="LRC")['free']
        reallrcb = int(float(lrcbalance))
        order = client.create_order(symbol=request.form['ssymbol'], 
            side=SIDE_SELL,
            type=ORDER_TYPE_MARKET,
            quantity=reallrcb)
    except Exception as e:
       flash(e.message, "error")
    return redirect('/')
    


if __name__ == "__main__":
    app.run(debug=True)

