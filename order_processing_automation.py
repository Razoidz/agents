orders = [
    {"id": 101, "amount": 25000, "status": "pending"},
    {"id": 102, "amount": 12000, "status": "completed"},
    {"id": 103, "amount": 30000, "status": "pending"},
    {"id": 104, "amount": 18000, "status": "cancelled"}
]
for order in orders:
    if order.get("status","Unknown") == "processed":
        continue
    if order.get("status","Unknown") == "pending" and isinstance(order.get("amount"),(int,float))and order.get("amount","Unknown") >= 20000:
            print(order.get("id"))