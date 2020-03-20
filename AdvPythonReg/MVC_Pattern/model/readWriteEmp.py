import csv

def readEmp():
    data = []
    with open('emp.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)

    return data

def writeEmp(obj):
    with open('emp.csv','a',newline='') as file:
        writer = csv.writer(file)
        data = [obj.id,obj.name,obj.email,obj.pwd,obj.dept,obj.sal]
        writer.writerow(data)

def updateEmp(data):
    with open('emp.csv','w',newline='') as file:
        writer = csv.writer(file)
        for item in data:
            writer.writerow(item)

def deleteEmp():
    pass