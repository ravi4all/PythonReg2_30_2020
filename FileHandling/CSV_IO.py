# csv - comma seperated values
import csv

# data = [
#     ['name','age','sal','dept'],
#     ['Ram',34,359900,'IT'],
#     ['Shyam',39,65900,'HR'],
#     ['Manoj',24,25900,'IT'],
# ]

data = [
    {"name":"Ram","age":45,"sal":45000,"dept":"IT"},
    {"name":"Manoj","age":35,"sal":49000,"dept":"HR"},
    {"name":"Sumit","age":41,"sal":35000,"dept":"HR"},
    {"name":"Aman","age":29,"sal":31000,"dept":"IT"},
]

with open('data.csv','w',newline='') as file:
    writer = csv.writer(file)
    for item in data:
        writer.writerow(item)
