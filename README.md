# Stock Portfolio Tracker 📈

A simple console-based Stock Portfolio Tracker built with Python as part of the **CodeAlpha Python Programming Internship** (Task 2).

## Project Description

This program allows users to build a stock portfolio by selecting stocks from a predefined list, entering the quantity they own, and viewing a complete investment summary. The portfolio is also saved to a text file for future reference.

> **Note:** This project uses hardcoded sample stock prices. It does NOT connect to any live stock market API.

## Features

- Displays a list of available stocks with sample prices
- Lets the user add multiple stocks to their portfolio
- Calculates the investment value for each stock (price × quantity)
- Displays a formatted portfolio summary with total investment value
- Saves the portfolio summary to `portfolio.txt`
- Validates stock symbols (must be in the predefined list)
- Validates quantity input (must be a positive whole number)
- Handles invalid input gracefully without crashing
- Clean and professional console output

## Technologies Used

- **Python 3** — standard library only
- **File handling** — for saving the portfolio to a text file

## How the Program Works

1. The program displays a list of available stocks and their sample prices.
2. The user enters a stock symbol and the quantity they own.
3. The program validates the input and calculates the investment value.
4. The user can keep adding stocks or type `done` to finish.
5. A formatted portfolio summary is displayed on the console.
6. The summary is saved to `portfolio.txt`.

## Stock Price Dictionary

The program uses a hardcoded Python dictionary with sample stock prices:

```python
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 180,
    "NVDA": 120,
}
```

These are **manually defined values for demonstration purposes only**. They do not reflect real-time market data.

## How to Run

1. Make sure Python 3 is installed on your system.
2. Open a terminal or command prompt.
3. Navigate to the project folder:
   ```
   cd CodeAlpha_StockPortfolio
   ```
4. Run the program:
   ```
   python portfolio_tracker.py
   ```

## Example Input

```
Enter stock symbol (or 'done' to finish): AAPL
Enter quantity: 10

Enter stock symbol (or 'done' to finish): TSLA
Enter quantity: 5

Enter stock symbol (or 'done' to finish): NVDA
Enter quantity: 20

Enter stock symbol (or 'done' to finish): done
```

## Example Output

```
=======================================================
           PORTFOLIO SUMMARY
=======================================================
Stock      Qty      Price ($)    Value ($)
-------------------------------------------------------
AAPL       10       180          1800
TSLA       5        250          1250
NVDA       20       120          2400
-------------------------------------------------------
TOTAL PORTFOLIO VALUE:         $5450
=======================================================

Portfolio saved to 'portfolio.txt'.
```

## File Saving

After building the portfolio, the program automatically saves the summary to `portfolio.txt` in the same folder. The file contains the stock details, individual values, and the total portfolio value.

## Concepts Learned

- Working with **dictionaries** to store and look up stock prices
- Using **lists of dictionaries** to store portfolio data
- **Functions** for organizing code into reusable blocks
- **Input validation** with `try/except` and conditional checks
- **String formatting** for clean, aligned console output
- **File handling** — writing data to a text file using `open()` and `write()`
- **`while` loops** for repeated user interaction
- **`if/elif/else`** for decision making
- Using **`if __name__ == "__main__"`** for proper program entry

## Limitations

- Stock prices are hardcoded and do not update in real time
- Only 6 sample stocks are available
- Does not track profit, loss, or price changes over time
- Portfolio is rebuilt from scratch each time the program runs

## Future Improvements

- Connect to a live stock API for real-time prices
- Add the ability to remove stocks from the portfolio
- Track portfolio performance over time
- Add buy/sell price tracking for profit/loss calculations
- Load and save portfolio data using JSON or CSV files

## Author

**Meghana L L**
CodeAlpha Python Programming Internship
