count = int(input("Введите количество билетов: "))
list_of_ages = [int(input("Введите возраст посетителя: ")) for i in range(count)]
list_of_prices = []
for value in list_of_ages:
    if value < 18:
        list_of_prices.append(0)
    elif 18 <= value <= 25:
        list_of_prices.append(990)
    else:
        list_of_prices.append(1390)

if count > 3:
    print("Стоимость заказа со скидкой равна:", int(sum(list_of_prices)*0.9), "рублей")
else:
    print("Полная стоимость заказа равна:", sum(list_of_prices), "рублей")
