try:
    f_num = int(input("Enter first num : "))
    s_num = int(input("Enter second num : "))

    a = f_num + s_num
    print("Sum is",a)

    b = f_num - s_num
    print("Diff is",b)

    c = f_num / s_num
    print("Div is",c)

    d = f_num * s_num
    print("Mul is",d)
except ZeroDivisionError:
    print("Cannot Divide by zero")
except ValueError:
    print("Invalid Input")
except TypeError:
    print("Unsupported Operations")
except BaseException as ex:
    print("Some error",ex)