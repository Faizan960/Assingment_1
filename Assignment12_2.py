#registration file
def register():
    try:
        username = input("Enter a username: ")
        password = input("Enter a password: ")

        with open('data/users.txt', 'a') as file:
            file.write(f"{username},{password}\n")

        print("Registration Successful!")
    except Exception as e:
        print("Error occurred while registering:", str(e))