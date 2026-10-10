# stock_portfolio.py

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 180
}

print("===== STOCK PORTFOLIO TRACKER =====")

# Display available stocks
print("\nAvailable Stocks:")
for stock, price in stock_prices.items():
    print(stock, "=$", price)

# User input
stock_name = input("\nEnter stock name: ").upper()
quantity = int(input("Enter quantity: "))

# Check if stock exists
if stock_name in stock_prices:

    price = stock_prices[stock_name]
    total_investment = price * quantity

    print("\n===== PORTFOLIO DETAILS =====")
    print("Stock:", stock_name)
    print("Price per share: $", price)
    print("Quantity:", quantity)
    print("Total Investment: $", total_investment)

    # Save result to a text file
    save = input("\nDo you want to save the result? (yes/no): ").lower()

    if save == "yes":
        with open("portfolio_result.txt", "w") as file:
            file.write("===== STOCK PORTFOLIO =====\n")
            file.write("Stock: " + stock_name + "\n")
            file.write("Price per share: $" + str(price) + "\n")
            file.write("Quantity: " + str(quantity) + "\n")
            file.write("Total Investment: $" + str(total_investment) + "\n")

        print("Result saved in portfolio_result.txt")

else:
    print("Stock not found!")