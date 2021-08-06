

products = {
    "americano":{"name":"Americano","price":150.00},
    "brewedcoffee":{"name":"Brewed Coffee","price":110.00},
    "cappuccino":{"name":"Cappuccino","price":170.00},
    "dalgona":{"name":"Dalgona","price":170.00},
    "espresso":{"name":"Espresso","price":140.00},
    "frappuccino":{"name":"Frappuccino","price":170.00},
}

def get_product(code):
  return products[code]


def get_property(code, property):
  return get_product(code)[property]

def make_receipt(orders):
    total_price = 0

    with open('receipt.txt', 'w') as file:
        file.write('==\n{:20} {:21} {:20} {:15}\n'.format('CODE', 'NAME', 'QUANTITY', 'SUBTOTAL'))
        for order_key, order_quantity in orders.items():
            price = get_property(order_key, 'price')
            subtotal = price * order_quantity
            line = '{:20} {:21} {:20} {:15}\n'.format( order_key, get_property(order_key, 'name'), str(order_quantity), str(subtotal) )
            # file.write( order_key + '\t\t\t\t' + get_property(order_key, 'name') + '\t\t\t' + str(order_quantity) + '\t\t\t\t' +  str(subtotal) + '\n')
            file.write(line)
            total_price += subtotal
        file.write('Total:\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t' + str(total_price) + '\n==')



def main():
    print('CoffeePython POS Terminal')
    orders = dict()

    inp = ''
    while inp != '/':
        inp = input('Input customer order ({product_code,quantity}): ')
        if inp and inp != '/':
            order_split_list = inp.split(',')
            if not len(order_split_list) == 2:
                print('Error format. Customer order should be in {product_code,quantity} format')
            else:
                product_code = order_split_list[0]
                quantity = int(order_split_list[1])
                if product_code in orders:
                    orders[product_code] += quantity
                else:
                    orders[product_code] = quantity
    make_receipt(orders)

 
if __name__ == '__main__':
    main()