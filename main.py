print("Hello!\nIt's my first cafe.\nWelcome!")
coffee = ["americano", "espresso", "cappuccino", "rath", "mocchiato"]
price = [[200, 60], [300, 120], [400, 180], [500, 240]]

print("We can make some drinks for you:", end=" ")
for i in coffee[0:-1]:
    print(i, end=', ')
print(coffee[-1]+".")

while True:
    user_coffee = input()
    if user_coffee == "exit":
        exit(0)
    if user_coffee not in coffee:
        print("Sorry. We can't make it. Try again.")
    else:
        break

print("Ok. What is volume?")
for i in price[0: -1]:
    print(i[0], end=' ml, ')
print(str(price[-1][0]) + '?')

while True:
    tryvol = True
    user_volume = input()
    if user_volume == "exit":
        exit(0)
    for i in price:
        if int(user_volume) == i[0]:
            print('You should pay: ' + str(i[1]) + 'rub.')
            tryvol = False
            break
    if tryvol:
        print("Sorry. We can't make it. Try again.")


