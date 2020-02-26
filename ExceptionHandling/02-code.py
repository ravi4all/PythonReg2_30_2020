try:
    f_num = int(input("Enter first num : "))
    s_num = int(input("Enter second num : "))

    a = f_num + s_num
    b = f_num - s_num
    c = f_num / s_num
    d = f_num * s_num

except BaseException as ex:
    print("Some error",ex)

else:
    print("Sum is", a)
    print("Diff is", b)
    print("Div is", c)
    print("Mul is", d)