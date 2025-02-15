📈 Stock Price Prediction Web App

A machine learning web application built with Flask to predict stock prices using LSTM models.

Features
- Predict stock prices for any ticker symbol (e.g., AAPL, RELIANCE)
- Real-time stock data fetched using `yfinance`
- LSTM model for time-series prediction
- Responsive web interface with HTML and CSS

Tech Stack
- **Backend:** Flask, TensorFlow, NumPy, Pandas
- **Frontend:** HTML, CSS
- **Data Source:** Yahoo Finance (`yfinance`)

📂 Project Structure

📁 stock-price-prediction/
├── app.py                # Flask application
├── templates/
│   └── index.html        # Frontend HTML page
├── static/
│   └── style.css         # CSS for styling
├── stock_model.h5        # Pre-trained LSTM model
├── scaler.npy            # Scaler for data normalization
└── requirements.txt      # Python dependencies


## ⚙️ Installation
1. **Clone the repository:**

   git clone https://github.com/yourusername/stock-price-prediction.git
   cd stock-price-prediction

2. **Create a virtual environment:**

   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

3. **Install dependencies:**

   pip install -r requirements.txt


 Usage
1. **Run the Flask app:**

   python app.py

2. **Open your browser:** Visit `http://127.0.0.1:5000`
3. **Enter stock ticker and date range:** Click `Predict`

Deployment (Optional)
Deploy your app on platforms like **Render, Heroku, or GitHub Pages.**

Contributing
Contributions are welcome! Feel free to fork this repository and submit a pull request.

License
This project is licensed under the MIT License.
