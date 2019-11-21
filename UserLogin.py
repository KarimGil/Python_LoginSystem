users = {} #Creates a dictionary to store user details
status = '' # To know if the person is registered or not

def displayMenu():
    #Function for main menu
    status = input("Are you Registered User? Yes/No? Press Q to exit")
    if status == "Yes":
        oldUser()
    elif status == "No":
        newUser()
    else:
        print("Session Ends")
        quit()

def newUser():
    #If the user is new NewUser function will create their account
    createLogin = input("Create User Name: ")

    if createLogin in users:
        print("Login name already exist")

    else:
        createPass = input("Enter Password: ")
        users[createLogin] = createPass
        print("\n User Created \n")

def oldUser():
    #If the user is already registered this function will fetch their details and welcome them.
    login = input("Enter User Name: ")
    passw = input("Enter Password: ")

    if login in users and users[login] == passw:
        print("\n Login Successful\n")
        print("\n Welcome "+login+"!")
    else:
        print("\nInvalid User or Password\n")

while status != "Q":
    displayMenu()




