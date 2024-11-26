
menu = {
    1 : ('cheseburger', 10),
    2 : ('burger', 20),
    3 : ('pizza', 50)
}

def get_price():

    while True:
        print(f'''Menu: 
                1. cheeseburger - $10
                2. burger - $20
                3. pizza - $50  
''')
        
        choice = input('Enter the number of the product you want to order: ')
        if choice.isdigit():
            choice = int(choice)
            if choice in menu:
                x = menu[choice][1]
                # print(f'You have ordered {menu[choice][0]} for ${menu[choice][1]}')
                break
            else:
                print('Invalid option!')
        else:
            print('Invalid option!')

    return menu[choice][0], menu[choice][1]


x = get_price()


def get_qty():
    while True:    
        quantity = input('Enter the number of quantity: ')
        if quantity.isdigit():
            quantity = int(quantity)
            if quantity > 1:
                        print(f'You order consists of {quantity} {x[0]}s for ${x[1] * quantity}. ')
                        break
            else:
                        print(f'Youre order consists of {quantity} {x[0]} for ${x[1] * quantity}. ')
                        break
        else:
            print('Invalid option!')


get_qty()
