# Stock Portfolio Tracker
# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 330,
    "AMZN": 140
}

portfolio = {}
total_investment = 0

print("===== Stock Portfolio Tracker =====")
print("Available Stocks:")
for stock, price in stock_prices.items():
    print(f"{stock} : ${price}")

while True:
    stock_name = input("\nEnter Stock Name (or type 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("Stock not available! Please choose from the list.")
        continue

    try:
        quantity = int(input(f"Enter quantity of {stock_name}: "))

        if quantity <= 0:
            print("Quantity should be greater than zero.")
            continue

        portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity

    except ValueError:
        print("Please enter a valid integer quantity.")

print("\n========== Portfolio Summary ==========")

if not portfolio:
    print("No stocks purchased.")
else:
    for stock, quantity in portfolio.items():
        investment = stock_prices[stock] * quantity
        total_investment += investment
        print(f"{stock} | Quantity: {quantity} | Price: ${stock_prices[stock]} | Investment: ${investment}")

    print("---------------------------------------")
    print(f"Total Investment Value: ${total_investment}")

    # Save result to a text file
    with open("portfolio_summary.txt", "w") as file:
        file.write("===== Stock Portfolio Summary =====\n\n")
        for stock, quantity in portfolio.items():
            investment = stock_prices[stock] * quantity
            file.write(
                f"{stock} | Quantity: {quantity} | "
                f"Price: ${stock_prices[stock]} | Investment: ${investment}\n"
            )
        file.write("\n---------------------------------------\n")
        file.write(f"Total Investment Value: ${total_investment}")

    print("\nPortfolio summary has been saved as 'portfolio_summary.txt'")