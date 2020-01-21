'''
*
**
***
****
*****
'''
for i in range(1,6):
    print('*' * i)

print("="*10)

# Alternative Using Nested Loop
for i in range(5):
    for j in range(i+1):
        print('*',end='')
    print()

print("="*10)

'''
*****
****
***
**
*
'''
for i in range(5,0,-1):
    for j in range(i):
        print('*',end='')
    print()
print("="*10)

'''
1
12
123
1234
12345
'''
for i in range(5):
    for j in range(i+1):
        print(j+1,end='')
    print()
print("="*10)

'''
a
ab
abc
abcd
abcde
'''
for i in range(5):
    x = 96
    for j in range(i+1):
        x += 1
        print(chr(x),end='')
    print()
print("="*10)


'''
a
bb
ccc
dddd
eeeee
'''
x = 96
for i in range(5):
    x += 1
    for j in range(i+1):
        print(chr(x),end='')
    print()
print("="*10)














