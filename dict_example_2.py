products = [
    {"p_name":"Apple Iphone 11","brand":"Apple","Category":"Mobile","price":98000},
    {"p_name":"Redmi Note 6","brand":"Xiaomi","Category":"Mobile","price":15000},
    {"p_name":"Sports Shoes","brand":"Puma","Category":"Shoes","price":3400},
    {"p_name":"JBL Headphones bluetooth","brand":"JBL","Category":"Headphones","price":1200},
    {"p_name":"Leather Jacket","brand":"Zara","Category":"Clothes","price":4500},
    {"p_name":"Puma Shoes","brand":"Puma","Category":"Shoes","price":2070},
    {"p_name":"Adidas Sports Shoes","brand":"Adidas","Category":"Shoes","price":1900},
    {"p_name":"Macbook Pro","brand":"Apple","Category":"Laptop","price":128000},
    {"p_name":"Lenovo thinkpad","brand":"Lenovo","Category":"Laptop","price":78000},
    {"p_name":"Asus Zenbook","brand":"Asus","Category":"Laptop","price":88000},
    ]

search = input("Enter product : ")
search = search.lower()
data = []
for i in range(len(products)):
    cond_1 = search in products[i]['p_name'].lower()
    cond_2 = search in products[i]['Category'].lower()
    cond_3 = search in products[i]['brand'].lower()

    if cond_1 or cond_2 or cond_3:
        print(products[i])
        data.append(products[i])

print("""
Apply Price Filter :
1. Low to High
2. High to Low
""")

def show(x):
    return x['price']

ch = input("Enter your choice : ")
if ch == "1":
    sorted_data = sorted(data,key=show)
    print(sorted_data)
else:
    sorted_data = sorted(data,key=show,reverse=True)
    print(sorted_data)


