fName = input("Enter your First name: ")
sName = input("Enter your Surname: ")
print("Hello {} {}, let's calculate your Profit!".format(fName, sName))

items_sold = int(input("How many items have you sold? "))
print("You have sold {} item(s). How much money do you need?".format(items_sold))
money_needed = float(input(""))


sale_prices = []
for i in range(1, items_sold + 1):
    price = float(input("Enter the sale price of item {}:".format(i)))
    sale_prices.append(price)


profits = []
for i in range(items_sold):
    profit = round(sale_prices[i] * 0.8, 2)  # the 2 just rounds to 2 decimal points as you cant have any smaller than 1p
    profits.append(profit)
    print("Profit from item {}: {}".format(i + 1, profit))

total_profit = sum(profits)
average_profit = round(total_profit / items_sold, 2)
print("Your average profit per item is {}.".format(average_profit))


if total_profit >= money_needed:
    print("Well done {} {}! You've reached your target".format(fName, sName))
else:
    print("Based on your numbers you have not reached your target. I'm sorry {} {}.".format(fName, sName))
