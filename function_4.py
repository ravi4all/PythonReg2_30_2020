# Parameters/arguments in function

# Positional + Default arguments
def emp(name,sal,dept="IT"):
    print("Details of {} are : ".format(name))
    print("Salary is", sal)
    print("Dept is", dept)

emp("Ram",34500)
emp("Shyam",45000,"HR")