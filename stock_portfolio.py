stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 180
}
total_investment = 0
print("================================")
print("      STOCK PORTFOLIO TRACKER")
print("================================")
print("\nAvailable stocks:")
for stock, price in stock_prices.items():
    print(stock, ":", "$", price)

while True:
    stock = input("\nEnter stock name (or type 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("❌ Stock not available. Please choose from the available stocks.")
        continue

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("❌ Quantity must be greater than 0.")
            continue

        investment = stock_prices[stock] * quantity
        total_investment += investment

        print("✅", stock, "investment value: $", investment)

    except ValueError:
        print("❌ Please enter a valid number for quantity.")
print("\n================================")
print("Total Investment Value: $", total_investment)
print("================================")
print("Thank you for using the Stock Portfolio Tracker!")