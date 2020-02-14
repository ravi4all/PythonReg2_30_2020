def loginCheck(func):
    name = 'Ram'
    if name == 'Ram':
        print("Already Logged In")
        return func
    else:print("Login First")

@loginCheck
def postData():
    post = input("Enter your post : ")
    print("Post published...")
    print("Post -",post)

@loginCheck
def uploadPic():
    print("Pic Uploaded")

uploadPic()