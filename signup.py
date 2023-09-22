import re, time, getpass
import login
email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

class Sign_up:
    def __init__(self, first_name, last_name, email, password, confirm_password, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.confirm_password = confirm_password
        self.phone_number = phone_number

    # First Name Validation
    def get_first_name(self):
        self.first_name = self.first_name.replace(" ","")
        if self.first_name.isalpha():
            return self.first_name
        else:
            print("Invalid input \N{unamused face}")
    
    # Last Name Validation
    def get_last_name(self):
        self.last_name = self.last_name.replace(" ","")
        if self.last_name.isalpha():
            return self.last_name
        else:
            print("invalid input \N{unamused face}")

    # Email Validation
    def get_email(self):
        
        if re.fullmatch(email_regex, self.email):
            return self.email
        else:
            print("invalid input \N{unamused face}") 
    
    # password Validation
    def get_password(self):
        if len(self.password) < 6:
            print("Invalid Password \N{unamused face}")
        else:
            return self.password 
    
    # Confirm Password Validation
    def get_confirm_password(self):
        if self.password != self.confirm_password:
            print("Password is not the same \N{unamused face}")
        else:
            return self.confirm_password 
    
    # Phone Number Validation
    def get_phone_number(self):
        if len(self.phone_number) == 11 and (self.phone_number.startswith("010") or  self.phone_number.startswith("011") or self.phone_number.startswith("015")):
            return self.phone_number
        else:
            print("phone number is not valid \N{unamused face}")


def sign_up():
    print("Welcome to Sign Up form \N{grinning face}")
    print("Please Enter your information \N{smiling face with halo}")
    sign_up = Sign_up(None,None,None,None,None,None)

    # Get First Name
    first_name = sign_up.first_name = input("First Name: ")
    while not sign_up.get_first_name():
        first_name = sign_up.first_name = input("First Name: ")

    # Get Last Name
    last_name = sign_up.last_name = input("Last Name: ")
    while not sign_up.get_last_name():
        last_name = sign_up.last_name = input("Last Name: ")
    
    # Get Email
    email = sign_up.email = input("Email: ")
    while not sign_up.get_email():
        email = sign_up.email = input("Email: ")

    # Get Password
    password = sign_up.password = getpass.getpass("Password (Should be more the 6 characters): ")
    while not sign_up.get_password():
        password = sign_up.password = getpass.getpass("Password (Should be more the 6 characters): ")
    
    # Confirm Password
    confirm_password  = sign_up.confirm_password = getpass.getpass("Confirm Password: ")
    while not sign_up.get_confirm_password():
        confirm_password  = sign_up.confirm_password = getpass.getpass("Confirm Password: ")
    
    # Get Phone Number
    phone_number = sign_up.phone_number = input("Phone Number: ")
    while not sign_up.get_phone_number():
        phone_number = sign_up.phone_number = input("Phone Number: ")

    # Pass Values to file User Data:
    with open("userdata.txt","a") as user_data:
        user_data.write(f"{first_name}:{last_name}:{email}:{password}:{phone_number} \n")
    
    print(f"Welcome {first_name}, to our community \N{grinning face}")
    print("Redirecting to Login Form ...")
    time.sleep(2.0)
    login.login()
    
    
