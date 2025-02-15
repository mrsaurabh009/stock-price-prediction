from flask import Flask, request, render_template
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
import yfinance as yf

app = Flask(__name__)

# Load model and scaler
model = load_model('stock_model.h5')
scaler = np.load('scaler.npy')

# Function to get latest stock data
def get_latest_stock_price(ticker):
    data = yf.download(ticker, period="7d", interval="1h")
    prices = data['Close'].values
    
    # Adjust input to 60 values
    if len(prices) < 60:
        prices = np.pad(prices, (60 - len(prices), 0), mode='constant')
    else:
        prices = prices[-60:]  # Use only the last 60 values
    return prices

# Function to make predictions
def predict_stock_price(ticker):
    prices = get_latest_stock_price(ticker)
    scaled_prices = prices / scaler  # Scale using saved scaler
    
    # Reshape input to (1, 60, 1)
    X = np.array(scaled_prices).reshape(1, 60, 1)
    
    # Predict and reverse scale
    prediction = model.predict(X).item()  # Convert to scalar
    return prediction * scaler

# Routes for web interface
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    ticker = request.form['ticker']
    try:
        prediction = predict_stock_price(ticker)
        result = f"The predicted stock price for {ticker} is: ${round(float(prediction), 2)}"

    except Exception as e:
        result = f"Error: {str(e)}"
    return result

if __name__ == '__main__':
    app.run(debug=True)
