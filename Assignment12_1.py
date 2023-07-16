#logiin file

def login():
    try:
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        with open('data/users.txt', 'r') as file:
            for line in file:
                data = line.strip().split(',')
                if data[0] == username and data[1] == password:
                    print("Login Successful!")
                    return

        print("Invalid username or password. Please try again.")
    except Exception as e:
        print("Error occurred while logging in:", str(e))