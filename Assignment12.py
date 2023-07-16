#main file
import assignment_12_1,assignment_12_2,assignment_12_3,assignment_12_4,assignment_12_5
def main():
    while True:
        print("\nLogin Page")
        print("1. Login")
        print("2. Register")
        print("3. Forgot Password")
        print("4. Change Password")
        print("5. Navigate to a Site")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            assignment_12_1.login()
        elif choice == "2":
            assignment_12_2.register()
        elif choice == "3":
            assignment_12_3.forgot_password()
        elif choice == "4":
            assignment_12_4.change_password()
        elif choice == "5":
            assignment_12_5.navigate_to_site()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()