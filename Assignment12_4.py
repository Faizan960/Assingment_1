#change password file
def change_password():
    try:
        username = input("Enter your username: ")
        old_password = input("Enter your old password: ")
        new_password = input("Enter your new password: ")

        with open('data/users.txt', 'r') as file:
            lines = file.readlines()

        found = False
        for i, line in enumerate(lines):
            data = line.strip().split(',')
            if data[0] == username and data[1] == old_password:
                lines[i] = f"{username},{new_password}\n"
                found = True
                break

        if found:
            with open('data/users.txt', 'w') as file:
                file.writelines(lines)
            print("Password changed successfully!")
        else:
            print("Invalid username or password. Please try again.")
    except Exception as e:
        print("Error occurred while changing password:", str(e))