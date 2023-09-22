import time
import login_menu

def search_project(email):
    user_email = email
    print("Start Searching process \N{grinning face}")
    date = input("Enter the start date of your project: ")
    search_project = Search_Project(user_email,date)

class Search_Project:
    def __init__(self,email,date):
        self.email = email
        self.date = date
        self.search()
    
    def search(self):
        with open("projects.txt","r") as file:
            projects = file.readlines()
            flag = 0
            for project in projects:
                project = project.strip("\n")
                project_info = project.split(":")
                if project_info[0] == self.email and project_info[4] == self.date:
                    flag = 1
                    print(f"User Email: {project_info[0]}")
                    print(f"Project Title: {project_info[1]}")
                    print(f"Description: {project_info[2]}")
                    print(f"Total target: {project_info[3]}")
                    print(f"Start Date: {project_info[4]}")
                    print(f"End Date: {project_info[5]}")
            if flag == 0:
                print(f"You don't have projects starts at {self.date} \N{unamused face}")

        print("Redirecting to Login Menu ...")
        time.sleep(2.0)
        login_menu.login_menu(self.email)