# Binance-API
This is a Python Flask web application that interacts with the Binance API. It allows users to check their account balances, buy and sell cryptocurrencies (specifically LRC/USDT), and displays exchange information and symbols.

The app.py file contains the backend code for the Flask application, and the index.html file contains the frontend HTML and CSS code.

The Binance API is used to get account information, asset balances, exchange information, and to place buy/sell orders. The binance.client and binance.enums modules are used for this purpose.

The application also uses the websocket module to get real-time updates on the price of Ethereum, although this is commented out in the code.

The frontend of the application is designed using the Bootstrap CSS framework. It contains a navbar, input fields, buttons, and output fields to display account information and balances.

The application runs on the local server and can be accessed by navigating to http://localhost:5000/ in the web browser.
