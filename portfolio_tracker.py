"""
Stock Portfolio Tracker - CodeAlpha Python Programming Internship (Task 2)

A simple console-based stock portfolio tracker that lets the user
build a portfolio from a set of predefined stock prices and calculates
the total investment value.

NOTE: The stock prices used in this program are MANUALLY DEFINED sample
values. They are NOT live market prices and do not reflect real-time
stock data.
"""


# Sample stock prices (hardcoded, NOT live market data)
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 180,
    "NVDA": 120,
}


def display_available_stocks():
    """Show all available stocks and their sample prices."""
    print("\nAvailable Stocks:")
    print("-" * 30)
    print(f"{'Symbol':<10} {'Price ($)':<10}")
    print("-" * 30)
    for symbol, price in STOCK_PRICES.items():
        print(f"{symbol:<10} {price:<10}")
    print("-" * 30)


def get_stock_symbol():
    """Ask the user for a stock symbol and validate it.

    Returns the uppercase symbol if valid, or None if invalid.
    """
    symbol = input("\nEnter stock symbol (or 'done' to finish): ").strip().upper()

    if symbol == "DONE":
        return "DONE"

    if symbol not in STOCK_PRICES:
        print(f"'{symbol}' is not available. Please choose from the list above.")
        return None

    return symbol


def get_quantity():
    """Ask the user for a quantity and validate it.

    Returns a positive integer, or None if the input is invalid.
    """
    try:
        quantity = int(input("Enter quantity: "))
    except ValueError:
        print("Invalid input. Please enter a whole number.")
        return None

    if quantity <= 0:
        print("Quantity must be a positive number.")
        return None

    return quantity


def build_portfolio():
    """Let the user add stocks to their portfolio one at a time.

    Returns a list of dictionaries, each with symbol, quantity, price, and value.
    """
    portfolio = []

    print("\nAdd stocks to your portfolio. Type 'done' when finished.")

    while True:
        symbol = get_stock_symbol()

        if symbol == "DONE":
            break
        if symbol is None:
            continue

        quantity = get_quantity()
        if quantity is None:
            continue

        price = STOCK_PRICES[symbol]
        value = price * quantity

        portfolio.append({
            "symbol": symbol,
            "quantity": quantity,
            "price": price,
            "value": value,
        })

        print(f"Added {quantity} shares of {symbol} (${value})")

    return portfolio


def display_portfolio(portfolio):
    """Print the portfolio summary to the console."""
    if not portfolio:
        print("\nYour portfolio is empty.")
        return 0

    print("\n" + "=" * 55)
    print("           PORTFOLIO SUMMARY")
    print("=" * 55)
    print(f"{'Stock':<10} {'Qty':<8} {'Price ($)':<12} {'Value ($)':<12}")
    print("-" * 55)

    total = 0
    for item in portfolio:
        print(f"{item['symbol']:<10} {item['quantity']:<8} {item['price']:<12} {item['value']:<12}")
        total += item["value"]

    print("-" * 55)
    print(f"{'TOTAL PORTFOLIO VALUE:':<30} ${total}")
    print("=" * 55)

    return total


def save_portfolio(portfolio, total, filename="portfolio.txt"):
    """Save the portfolio summary to a text file."""
    with open(filename, "w") as file:
        file.write("=" * 55 + "\n")
        file.write("           PORTFOLIO SUMMARY\n")
        file.write("=" * 55 + "\n")
        file.write(f"{'Stock':<10} {'Qty':<8} {'Price ($)':<12} {'Value ($)':<12}\n")
        file.write("-" * 55 + "\n")

        for item in portfolio:
            file.write(
                f"{item['symbol']:<10} {item['quantity']:<8} "
                f"{item['price']:<12} {item['value']:<12}\n"
            )

        file.write("-" * 55 + "\n")
        file.write(f"{'TOTAL PORTFOLIO VALUE:':<30} ${total}\n")
        file.write("=" * 55 + "\n")

    print(f"\nPortfolio saved to '{filename}'.")


def main():
    """Main function — runs the portfolio tracker."""
    print("\nWelcome to the Stock Portfolio Tracker!")
    print("(Note: Stock prices are sample values, not live data.)")

    display_available_stocks()

    portfolio = build_portfolio()

    if portfolio:
        total = display_portfolio(portfolio)
        save_portfolio(portfolio, total)
    else:
        print("\nNo stocks were added. Nothing to save.")

    print("\nThank you for using the Stock Portfolio Tracker!")


if __name__ == "__main__":
    main()
