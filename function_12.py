# def temp_conv(cel):
#     return 9/5 * cel + 32
#
# def km_to_m(m):
#     return m/1000
#
# def hrs_to_mins(hrs):
#     return hrs * 60

def temp_conv(cel):return 9/5 * cel + 32

def km_conv(m):return m/1000

def hrs_to_sec(hrs):return hrs * 60 * 60

temperatures = [34.65,29.5,28.4,32.4,31.5]
meters = [1000,1200,4500]
hrs = [5,4,6,1,2]

# def myMap(func,data):
#     item = []
#     for i in range(len(data)):
#         item.append(func(data[i]))
#
#     return item
#
# f = myMap(temp_conv,temperatures)
# km = myMap(km_conv,meters)
# sec = myMap(hrs_to_sec,hrs)

f = list(map(temp_conv,temperatures))
km = list(map(km_conv,meters))
sec = list(map(hrs_to_sec,hrs))
print(f,km,sec)
