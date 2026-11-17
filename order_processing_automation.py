import logging
import json
import sqlite3
logging.basicConfig(
    filename="automation.log",
    level=logging.INFO,
    format= "%(asctime)s %(levelname)s %(message)s"
    )
# orders = [
#     {"id": 101, "amount": 25000, "status": "pending",'attempts': 0},
#     {"id": 102, "amount": 12000, "status": "completed",'attempts': 0},
#     {"id": 103, "amount": 30000, "status": "pending",'attempts': 0},
#     {"id": 104, "amount": 18000, "status": "cancelled",'attempts': 0}
# ]
connection = sqlite3.connect("orders.db")
cursor = connection.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS orders(
    id INTEGER PRIMARY KEY,
    amount REAL,
    status TEXT,
    attempts INTEGER
);
""")
cursor.execute("""
    INSERT OR IGNORE INTO orders (id, amount, status, attempts)
    VALUES (101, 25000, 'pending', 0)
""")

connection.commit()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
print(cursor.fetchall())
def load_file(path="orders.json", default=None):
    try:
        with open(path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        logging.warning(f"{path} not found, using default data")
        return default if default is not None else []
    except json.JSONDecodeError:
        logging.error(f"{path} is not valid JSON")
        return default if default is not None else []
orders=load_file()
def process_order(order):
    # Simulate successful processing
    return True

MAX_ATTEMPTS = 3
for order in orders:
    if order["status"] == "pending" and isinstance(order.get("amount"), (int, float)) and order["amount"] >= 20000:
        while order["attempts"] < MAX_ATTEMPTS:
            try:
                ok = process_order(order)
            except Exception:
                logging.exception(f"Order {order['id']} raised an error")
                ok = False

            if ok:
                order["status"] = "processed"
                logging.info(f"Order {order['id']} processed successfully")
                break

            order["attempts"] += 1
            logging.warning(f"Order {order['id']} failed, attempt {order['attempts']}")
        else:
            order["status"] = "failed"
            logging.critical(f"Order {order['id']} exhausted maximum retry attempts")
   
def save_file(orders):
    with open("orders.json", "w") as file:
        json.dump(orders,file, indent=4)
save_file(orders)
