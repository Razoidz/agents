import requests

# url = "https://jsonplaceholder.typicode.com/posts"
# try:
#     response = requests.get(url,timeout=10)
#     response.raise_for_status()
#     print(response.status_code)
#     datas = response.json()
#     print(len(datas))

#     for data in datas[:5]:
#         if data["userId"] == 1:
#             # print(f"{data['id']}  {data['title']}")
#             print(data)
# except requests.exceptions.RequestException:
#     print("The Api request failed")
def fetch_posts():
    try:
        url = "https://jsonplaceholder.typicode.com/posts"
        response = requests.get(url,timeout=10)
        response.raise_for_status()
        data = response.json()
        try:
            if isinstance(data,list):
                return data
        except:
            raise ValueError("Expected a list of posts")
    except requests.exceptions.RequestException:
        print("The Api request failed")
        raise 
        
def get_user_posts(user_id):
    
        user_posts = []
        posts_dictionary = fetch_posts()
        if posts_dictionary is None:
             return []
        for data in posts_dictionary:
            if "userId" not in data:
                 continue
            if data["userId"] == user_id:
                user_posts.append(data)
            
        return user_posts
   
try:
    posts = get_user_posts(2)
    print(posts)
except requests.exceptions.Timeout:
     print("The request timed out")
except requests.exceptions.RequestException:
    print("Something went wrong")
try:
    posts = get_user_posts(1)
except ValueError:
    print("Invalid API response")
except requests.exceptions.RequestException:
    print("Request failed")   
# orders = [
#     {"id": 101, "amount": 25000, "status": "pending"},
#     {"id": 102, "amount": 12000, "status": "completed"},
#     {"id": 103, "amount": 30000, "status": "pending"},
#     {"id": 104, "amount": 18000, "status": "cancelled"},
# ]

# def get_eligible_orders(orders):
#     eligible_orders = []
#     for order in orders:
#         if order.get("status","unknown") == "pending" and isinstance(order.get("amount"),(int,float)) and order.get("amount") >= 20000:
#             eligible_orders.append(order)
#     return eligible_orders
# result = get_eligible_orders(data)
# print(result)