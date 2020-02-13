def temp_conv(cel):
    return 9/5 * cel + 32

# f = temp_conv(34.4)
# print(f)
temperatures = [34.65,29.5,28.4,32.4,31.5]
# f = []
# for temp in temperatures:
#     f.append(temp_conv(temp))
#
# print(f)

# f = list(map(temp_conv,temperatures))
# print(f)

def myMap(func,iter1):
    data = []
    for i in range(len(iter1)):
        f = func(iter1[i])
        data.append(f)
    return data

f = myMap(temp_conv,temperatures)
print(f)