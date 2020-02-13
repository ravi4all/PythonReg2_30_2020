# def even(num):
#     return num % 2 == 0

# print(even(34))
numbers = [i for i in range(1,50)]
# ev = filter(even,numbers)
# print(list(ev))

ev = filter(lambda x : x % 2 == 0, numbers)
print(list(ev))
