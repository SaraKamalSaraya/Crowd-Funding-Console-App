import getpass, time
import login_menu

def login():
    print("Welcome to Login form \N{grinning face}")
    login = Login(None,None)

    # Get Email and Password
    email = login.email = input("Email: ")
    password = login.password = getpass.getpass("Password: ")
    while not login.check_email_password():
        print("Invalid Email or Password \N{unamused face}")
        email = login.email = input("Email: ")
        password = login.password = getpass.getpass("Password: ")
    
    print(f"Welcome back \N{grinning face}")
    print("Redirecting to Login Menu ...")
    time.sleep(2.0)
    login_menu.login_menu(email)


class Login:
    def __init__(self, email, password):
        self.email = email
        self.password = password
    
    # Check if email and password are in the database
    def check_email_password(self):
        with open("userdata.txt","r") as user_data:
            users = user_data.readlines()
            for user in users:
                user = user.strip("\n")
                user_info = user.split(":")
                if user_info[2] == self.email and user_info[3] == self.password:
                    return True
            return False
