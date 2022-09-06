count = int(input("Insert quantity of tickets you need: "))
list_of_ages = [int(input("Insert age: ")) for i in range(count)]
price1 = 0
price2 = 990
price3 = 1390
list_of_prices = []
for value in list_of_ages:
    if value < 18:
        list_of_prices.append(price1)
    if 18 <= value <= 25:
        list_of_prices.append(price2)
    if value > 25:
        list_of_prices.append(price3)

if count > 3:
    print("Стоимость заказа со скидкой равна:", int(sum(list_of_prices)*0.9), "рублей")
else:
    print("Полная стоимость заказа равна:", sum(list_of_prices), "рублей")
