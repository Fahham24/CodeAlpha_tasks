# Stock Portfolio Tracker 📈

## Project Overview
The Stock Portfolio Tracker is a simple Python application that calculates the total value of a user's stock holdings using manually defined stock prices. Users enter stock symbols and quantities, and the program calculates the investment value.

This project uses predefined prices for educational purposes and does not fetch live stock market data.

## Features
- Stores stock symbols and prices in a Python dictionary.
- Accepts stock symbols and quantities from the user.
- Calculates the value of individual stock holdings.
- Calculates the total portfolio value.
- Optionally saves the results in a TXT or CSV file.

## Technologies Used
- Python 3
- Built-in Python data structures
- Optional file handling

## Sample Stock Prices
The program can use a dictionary such as:

```python
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 420,
    "AMZN": 190
}
```

These values are illustrative examples, not current market prices.

## Key Concepts
- Dictionaries
- User input and output
- Variables and data types
- Loops and conditional statements
- Basic arithmetic
- File handling

## How to Run
1. Install Python 3 on your computer.
2. Save the code in a file named `stock_portfolio_tracker.py`.
3. Open a terminal or command prompt in the project folder.
4. Run the following command:

```bash
python stock_portfolio_tracker.py
```

## How It Works
1. The program displays the available stock symbols and predefined prices.
2. The user enters a stock symbol and the quantity owned.
3. The program calculates the value of each holding using:

`Investment Value = Stock Price × Quantity`

4. It adds the individual values to calculate the total portfolio value.
5. If implemented, the user can save the result to a file.

## Future Improvements
- Fetch live stock prices through a reliable financial API.
- Allow users to track multiple stocks.
- Add input validation and error handling.
- Generate portfolio reports in CSV format.
- Display individual holdings and total investment in a formatted table.

## Disclaimer
This project is for educational purposes only. It does not provide financial advice or real-time market information.

## Conclusion
This project helps beginners practice dictionaries, calculations, user input, and optional file handling using a practical financial example.