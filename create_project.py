import datetime ,time, re
import login_menu
   
class Create_Project:
    def __init__(self, title, details, target, start_date, end_date):
        self.title = title
        self.details = details
        self.target = target
        self.strart_date = start_date
        self.end_date = end_date
    
    # Title Validation
    def get_title(self):
        self.title = self.title.strip()
        if self.title.isalpha() and check_title(self.title):
            return self.title    

    # Details Validation ---- No needed validations
    def get_details(self):
        return self.details
    
    # Target Validation
    def get_target(self):
        if self.target.isnumeric():
            return self.target
        else:
            print("Invalid input \N{unamused face}")
    
    # Date Validation
    def get_strart_date(self):
        from datetime import datetime
        year = datetime.now().year
        month = datetime.now().month
        day = datetime.now().day
        now = f"{year}-{month}-{day}"
        now = datetime.strptime(now,'%Y-%m-%d')
        now = str(now.strftime('%Y-%m-%d'))
        pattern_str = r'^\d{4}-\d{2}-\d{2}$'
        try:
            if re.match(pattern_str, self.strart_date):
                datetime.strptime(self.strart_date, '%Y-%m-%d')
                if self.strart_date < now:
                    print("Start date can't be before Today. \N{unamused face}")     
                else:
                    return self.strart_date
            else:
                print("Incorrect data format, should be YYYY-MM-DD \N{unamused face}")
        except ValueError:
            print("Incorrect data format, should be YYYY-MM-DD \N{unamused face}")

     # End Date Validation
    def get_end_date(self):
        pattern_str = r'^\d{4}-\d{2}-\d{2}$'
        try:
            if re.match(pattern_str, self.end_date):
                datetime.datetime.strptime(self.end_date, '%Y-%m-%d')
                if self.strart_date < self.end_date:
                    return self.strart_date
                else:
                    print("Start date can't be equal or before End date. \N{unamused face}")
            else:
                print("Incorrect data format, should be YYYY-MM-DD \N{unamused face}")
        except ValueError:
            print("Incorrect data format, should be DD-MM-YYYY \N{unamused face}")

# ********************************************************************************************************

def create_project(email):
    user_email = email
    print("Start Creating a New Project \N{grinning face}")
    print("Please Project information \N{smiling face with halo}")
    create_project = Create_Project(None,None,None,None,None)

    # Get title
    title = create_project.title = input("Title: ")
    while not create_project.get_title():
        title = create_project.title = input("Title: ")
    
    # Get Details
    details = create_project.details = input("Details: ")
    while not create_project.get_details():
        details = create_project.details = input("Details: ")
    
    # Get Target
    target = create_project.target = input("Target: ")
    while not create_project.get_target():
        target = create_project.target = input("Target: ")
    
    # Get Start Date     YYYY-MM-DD
    strart_date = create_project.strart_date = input("Start Date: ")
    while not create_project.get_strart_date():
        strart_date = create_project.strart_date = input("Start Date: ")
    
    # Get End Date     
    end_date = create_project.end_date = input("End Date: ")
    while not create_project.get_end_date():
        end_date = create_project.end_date = input("End Date: ")
    
    # Pass Values to file Projects:
    with open("projects.txt","a") as projects:
        projects.write(f"{user_email}:{title}:{details}:{target}:{strart_date}:{end_date} \n")
    
    print(f"Your project is added to the Crowd-Funding console app \N{grinning face}")
    print("Redirecting to Login Menu ...")
    time.sleep(2.0)
    login_menu.login_menu(user_email)
    
# ********************************************************************************************************

def check_title(title):
    with open("projects.txt","r") as file:
        projects = file.readlines()
        for project in projects:
            project = project.strip("\n")
            project_info = project.split(":")
            if project_info == [""]:
                break
            elif project_info[1] == title:
                print("This title already exit. \N{unamused face}")
                return False
    return True