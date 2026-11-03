import logging

logging.basicConfig(
    filename="automation.log",
    level=logging.INFO,
    format = "%(asctime)s %(levelname)s %(message)s"
    )
orders = [
    {"id": 101, "amount": 25000, "status": "pending",'attempts': 0},
    {"id": 102, "amount": 12000, "status": "completed",'attempts': 0},
    {"id": 103, "amount": 30000, "status": "pending",'attempts': 0},
    {"id": 104, "amount": 18000, "status": "cancelled",'attempts': 0}
]
def process_order(order):
    # Simulate successful processing
    return True
MAX_ATTEMPTS = 3
for order in orders:
    
    if order.get("status","Unknown") == "processed":
        continue
    if order.get("status","Unknown") == "pending" and isinstance(order.get("amount"),(int,float))and order.get("amount") >= 20000:
        result= process_order(order)
        if result:
            order["status"] = "processed"
            # print(order.get("status"))
            logging.info(f"Order {order['id']} processed successfully")
        else:
            logging.error(f"Order {order['id']} processed failed")
            order['attempts'] += 1
            if order["attempts"] >= MAX_ATTEMPTS:
                # Stop retrying
                order['status'] = "failed"
    print(order["attempts"])
