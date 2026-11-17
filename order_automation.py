import json
def load_orders():
    with open("orders.json","r")as file:
        return json.load(file)
orders = load_orders()


def save_orders(orders):
    with open("orders.json","w")as file:
        json.dump(orders,file, indent=4)
def change_order(orders,id):
    processed = False
    found = False
    for order in orders:
        if order['id'] == id:
            found = True
            if order['status'] == 'pending':
                
                order['status'] = 'processed'
                processed = True
   
    if processed:
        save_orders(orders)
    elif found:
            print("Order already processed not eligible")
    else:
        print("Order Id does not exist")
change_order(orders,101)
change_order(orders, 102)
change_order(orders, 999)