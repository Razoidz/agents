# import random

# from numpy import average
# # weather = {
# #     'time':3,
# #     'temp': 23.2,
# #     'feels_like':24.0,
# #     'humidity': 91,
# #     'pressure': 1014,
# # }

# # reservation = {
# #     15: "Alice",
# #     17: "Bob",
# #     21: "Carol",
# #     21 : "Bayo"
# # }

# # students = [{
# #     'name': 'Alice',
# #     "grade": 7,
# # },{
# #     'name': 'Bob',
# #     "grade": 7,
# # },{
# #     'name': 'Carol',
# #     "grade": 7,
# # },{
# #     'name': 'David',
# #     "grade": 6,
# # }
# # ]
# # names = [{'name': 'Alice', 'age': 3}, {'name': 'Zophie', 'age': 17}]
# # #for name in names:
# #     # if name['age'] == 3:
# #     #     print(name['age'])
# # structure = {'humans': ['Alice', 'Bob'], 'pets': ['Zophie', 'Pookah']}
# # #print(structure['pets'][0])
# # pet_owners = {'Alice': ['Spot', 'Mittens'], 'Al': ['Zophie']}
# # for name in pet_owners:
    
# #    print(pet_owners['Alice'])
# def get_random_weather_data():
#     temp =random.randint(-50,50)
#     feels_like = random.uniform(temp - 10, temp + 10)
#     humidity = random.randint(0,100)
#     pressure = random.randint(990,1010)
#     data = {
#         'temp': temp,
#         'feels_like': round(feels_like),
#         'humidity': humidity,
#         'pressure':pressure,
#     }
#     return data
# weather_data = []
# for  i in range(1,100):
#     weather_data.append(get_random_weather_data())
# #print(weather_data)
# def get_average_temperature(weather_data):
#     total_temp = 0
#     for weather in weather_data:
#         total_temp += weather['temp']
#     average_temp = total_temp/len(weather_data)
#     print(average_temp)
# get_average_temperature(weather_data)
#chess_board =  {'d7': 'bQ', 'd2': 'wB', 'f1': 'bP', 'a3': 'bN'}


