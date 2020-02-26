try:
    file = open('file_1.txt','w')
    data = file.write()
    print(data)
except BaseException as ex:
    print(ex)
finally:
    print("File Closed")
    file.close()