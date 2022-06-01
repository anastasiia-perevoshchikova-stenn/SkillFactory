per_cent = {'TKB': 5.6, 'SKB': 5.9, 'VTB': 4.28, 'SBER': 4.0}
b1, b2, b3, b4 = per_cent.get('TKB'), per_cent.get('SKB'), per_cent.get('VTB'), per_cent.get('SBER')
list_of_percents = [b1, b2, b3, b4]

amount = int(input("Add your amount: "))
list_of_amounts = []

am_tkb, am_skb, am_vtb, am_sber = round(amount * b1 / 100), round(amount * b2 / 100), round(amount * b3 / 100), round(amount * b4 / 100)
list_of_amounts.append(am_tkb)
list_of_amounts.append(am_skb)
list_of_amounts.append(am_vtb)
list_of_amounts.append(am_sber)
print(list_of_amounts)

list_of_amounts.sort()
print("Максимальная сумма, которую вы можете заработать —", list_of_amounts[-1])