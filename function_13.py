temperatures = [34.65,29.5,28.4,32.4,31.5]
meters = [1000,1200,4500]
hrs = [5,4,6,1,2]

f = list(map(lambda x : 9/5 * x + 32,temperatures))
km = list(map(lambda x : x / 1000,meters))
sec = list(map(lambda x : x * 60 * 60,hrs))
print(f,km,sec)
