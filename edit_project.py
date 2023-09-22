import login_menu
import edit_title
import edit_details
import edit_target
import edit_start_date
import edit_end_date

class Edit_Project:
    def __init__(self,email):
        self.email = email
        self.edit_menu()

    def edit_menu(self):
        print("Start Editing process \N{grinning face}")
        print("This is a list of your choices, please choose a number:")
        print("[1] Edit title")
        print("[2] Edit Details")
        print("[3] Edit Target")
        print("[4] Edit Start Date")
        print("[5] Edit End Date")
        print("[6] Back to Login Menu")
        choice = input("Your choice is: ")

        if not choice.isnumeric():
            print("Invalid input. Please try again \N{unamused face}")
            edit_project(self.email)
        else:
            choice = int(choice)
            title = check_project_title(self.email)
            while not title:
                title = check_project_title(self.email)
            if choice == 1:
                edit_title.edit_title(self.email,title)
            elif choice == 2:
                edit_details.edit_details(self.email,title)
            elif choice == 3:
                edit_target.edit_target(self.email,title)
            elif choice == 4:
                edit_start_date.edit_start_date(self.email,title)
            elif choice == 5:
                edit_end_date.edit_end_date(self.email,title)
            elif choice == 6:
                print("Okay beybey \N{loudly crying face}")
                login_menu.login_menu(self.email)
            else:
                print("Invalid Number. Please try again \N{loudly crying face}")
                edit_project(self.email)

def edit_project(email):
    user_email = email
    edit_project = Edit_Project(user_email)

def check_project_title(email):
    user_email = email
    title = input("Enter Project title you want to edit: ")
    with open("projects.txt") as file:
        projects = file.readlines()
        for project in projects:
            project = project.strip("\n")
            project_info = project.split(":")
            if project_info[0] == user_email and project_info[1] == title:
                return title
        else:
            print("No project with that title \N{loudly crying face}")

    