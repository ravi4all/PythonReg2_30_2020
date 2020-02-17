file = open('file_1.txt','r')
# data = file.read()

# data = file.read(20)
# data = file.readline()

# data = file.readlines()

file.seek(20)
data = file.read(20)
print(data)
file.close()