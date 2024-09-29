from flask import Flask, render_template, request
import yfinance as yf

# Flask Object: Create the Flask app instance
app = Flask(__name__)

# Route for the home page with a form to input the stock symbol
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle the stock data request and display the result
@app.route('/get_stock', methods=['POST'])
def get_stock():
    stock_symbol = request.form.get('symbol').upper()  # Get the stock symbol from the form

    try:
        # Fetch stock data from Yahoo Finance
        stock = yf.Ticker(stock_symbol)
        stock_info = stock.info

        # Extract relevant data
        name = stock_info.get('longName', 'N/A')
        price = stock_info.get('currentPrice', 'N/A')
        market_cap = stock_info.get('marketCap', 'N/A')
        sector = stock_info.get('sector', 'N/A')
        dividend_yield = stock_info.get('dividendYield', 'N/A')

        return render_template('result.html', 
                               symbol=stock_symbol,
                               name=name,
                               price=price,
                               market_cap=market_cap,
                               sector=sector,
                               dividend_yield=dividend_yield)
    except Exception as e:
        # If an error occurs (invalid symbol, network issue, etc.)
        return f"An error occurred: {e}"

# Main block to run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
