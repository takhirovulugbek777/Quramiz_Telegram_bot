# import requests
# import json
# from bs4 import BeautifulSoup
# from handlers.user.callbacks import reaction_to_next
#
# url = f"https://quramiz.uz/api/product2/filter?catalog=1/"
#
# payload = ""
# headers = {}
# response = requests.request("POST", url, headers=headers, data=payload).json()
# products_data = response['result']['products']['data']
# id_counts = {}
#
# # Loop through each item (product) in products_data
# for item in products_data:
#     # Get the ID of the current product
#     product_id = item['id']
#
#     # Increment the count for the current ID in the id_counts dictionary
#     id_counts[product_id] = id_counts.get(product_id)
# print(len(id_counts))
#
#
# def category():
#     if category == "Стройматериалы 👷":
#         num_category = '1/'
#     elif category == 'Инструмент 🛠':
#         num_category = '2/'
#     elif category == "Электрика ⚡️":
#         num_category = 3
#     elif category == "Инженерные системы 🏗":
#         num_category = 4
#     elif category == "Интерьер и отделка 🖼":
#         num_category = 5
#     elif category == "Сантехника 🚰":
#         num_category = 6
#     elif category == "Крепеж 🔩":
#         num_category = 7
#     elif category == "Благоустройство 🧹":
#         num_category = 8
#     elif category == 'Новинки 🆕':
#         num_category = 9
#     else:
#         num_category = 1
#     API_NEXT = f'https://quramiz.uz/api/product2/filter?catalog={num_category}/'
import requests

product_id = 30603
response = requests.get(f'https://quramiz.uz/api/product2/{product_id}')
parsed_data = response.json()
product_name = parsed_data["result"]["name"]
print(product_name)
