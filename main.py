import yfinance as yf
import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM
from sklearn.preprocessing import MinMaxScaler

# Function to get stock data
def get_stock_data(ticker):
    data = yf.download(ticker, start="2020-01-01", end="2024-01-01")
    return data

# Function to train and save model
def train_and_save_model():
    data = get_stock_data('AAPL')  # Default: Apple stock
    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(data['Close'].values.reshape(-1, 1))

    # Create dataset for LSTM
    X, y = [], []
    for i in range(60, len(scaled_data)):
        X.append(scaled_data[i-60:i, 0])
        y.append(scaled_data[i, 0])
    X, y = np.array(X), np.array(y)
    X = X.reshape((X.shape[0], X.shape[1], 1))

    # Build LSTM model
    model = Sequential([
        LSTM(units=50, return_sequences=True, input_shape=(X.shape[1], 1)),
        LSTM(units=50),
        Dense(units=1)
    ])
    model.compile(optimizer='adam', loss='mean_squared_error')

    # Train model
    model.fit(X, y, epochs=5, batch_size=32)

    # Save model and scaler
    model.save('stock_model.h5')
    np.save('scaler.npy', scaler.scale_)
    print("Model and scaler saved!")

if __name__ == "__main__":
    train_and_save_model()
