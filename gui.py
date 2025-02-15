import tkinter as tk
from tkinter import ttk, messagebox
from main import predict_stock_prices

def create_gui():
    def on_submit():
        ticker = ticker_entry.get()
        start_date = start_date_entry.get()
        end_date = end_date_entry.get()
        period = period_var.get()

        if not ticker or not start_date or not end_date:
            messagebox.showerror("Error", "Please fill all fields.")
            return

        predictions = predict_stock_prices(ticker, start_date, end_date, period)
        result_label.config(text=f"Next 7 Days Predictions:\n{predictions}")

    # GUI Design
    root = tk.Tk()
    root.title("Stock Price Prediction")

    tk.Label(root, text="Stock Ticker (e.g. AAPL):").pack(pady=5)
    ticker_entry = tk.Entry(root)
    ticker_entry.pack(pady=5)

    tk.Label(root, text="Start Date (YYYY-MM-DD):").pack(pady=5)
    start_date_entry = tk.Entry(root)
    start_date_entry.pack(pady=5)

    tk.Label(root, text="End Date (YYYY-MM-DD):").pack(pady=5)
    end_date_entry = tk.Entry(root)
    end_date_entry.pack(pady=5)

    tk.Label(root, text="Select Period:").pack(pady=5)
    period_var = tk.StringVar(value="Daily")
    period_dropdown = ttk.Combobox(root, textvariable=period_var, values=["Daily", "Weekly", "Monthly", "Yearly"])
    period_dropdown.pack(pady=5)

    tk.Button(root, text="Submit", command=on_submit).pack(pady=10)
    result_label = tk.Label(root, text="", fg="green", font=("Arial", 10))
    result_label.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
