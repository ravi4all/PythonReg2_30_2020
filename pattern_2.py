'''
    *
   ***
  *****
 *******
*********
'''
for i in range(7):
    print(' ' * (7 - i) + '*' * (2*i + 1))

# Alternative
for i in range(7):
    for j in range(7 - i):
        print(' ',end='')
    for k in range(2*i + 1):
        print('*',end='')
    print()

'''
    1
   2 3
  4 5 6
 7 8 9 10
'''
n = 0
for i in range(4):
    for j in range(4 - i):
        print(' ',end='')
    for k in range(i+1):
        n += 1
        print(n,end=' ')
    print()













