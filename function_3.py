# Parameters/arguments in function

# Positional arguments
def emp(name,sal,dept):
    print("Details of {} are : ".format(name))
    print("Salary is", sal)
    print("Dept is", dept)

# emp("Ram",35000,"IT")
# emp("Aman",31000,"IT")
# emp("Anuj",25000,"HR")
data = {
    "names" : ["Ram","Shyam","Gopal","Akash","Sumit"],
    "dept" : ["IT","HR","IT","SALES","HR"],
    "sal" : [34000,21000,34560,45000,32000]
}

for i in range(len(data["names"])):
    if data["dept"][i] == "IT":
        name = data["names"][i]
        sal = data["sal"][i]
        dept = data["dept"][i]
        emp(name,sal,dept)
        print("="*20)