foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy(C to Confirm) : ")
    if food.upper() == "C":
        break

    else:
        price = float(input(f"Enter the price of {food} : $"))
        foods.append(food)
        prices.append(price)

print("======= YOUR CART =======")
print(foods)

print()
for price in prices:
    total = total + price
print("Your Total Bill Amount is: $"+str(total))
