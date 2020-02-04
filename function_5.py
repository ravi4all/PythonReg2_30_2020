# Parameters/arguments in function

# Dynamic arguments
# *args
# def emp(name,sal,*address,dept="IT"):
#     print("Details of {} are : ".format(name))
#     print("Salary is", sal)
#     print("Address is", address)
#     print("Dept is",dept)

# emp("Ram",34500,"Delhi",dept="HR")
# emp("Shyam",45000,"Gurgaon","Delhi")
# emp("Raman",68000,"Gurgaon","Delhi","Noida","Pune")

# **kwargs - keyword arguments
def emp(**details):
    print(details)

emp(name='Ram')
emp(name='Ram',dept='IT')
emp(name='Ramesh',dept='HR',sal=45000,address='Rohini')