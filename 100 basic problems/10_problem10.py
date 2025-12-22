#Write a program that will take user input of cost price and selling price and determines whether its a loss or a profit

buy_price = float(input("Enter buying price : "))
sell_price = float(input("Enter selling price : "))

difference = sell_price - buy_price

if difference < 0:
    print(f"You are in loss of {abs(difference):.2f}!")
elif difference > 0 :
    print(f"You are in profit of {difference:.2f}!")
else:
    print("No Profit and no loss")
