import create_project
import view_projects
import edit_project
import delete_project
import search_project
# Intro Point
def login_menu(email):
    print("Welcome to my Crowd-Funding console app \N{grinning face}")
    print("This is a list of your choices, please choose a number:")
    print("[1] Create a Fund Raise Campaign Project")
    print("[2] View All Projects")
    print("[3] Edit Own Projects")
    print("[4] Delete Own Projects")
    print("[5] Search For a Project")
    print("[6] Exit")
    useremail = email
    choice = input("Your choice is: ")

    if not choice.isnumeric():
        print("Invalid input. Please try again \N{unamused face}")
        login_menu(useremail)
    else:
        choice = int(choice)
        if choice == 1:
            create_project.create_project(email)
        elif choice == 2:
            view_projects.view_projects(email)
        elif choice == 3:
            edit_project.edit_project(email)
        elif choice == 4:
            delete_project.delete_project(email)
        elif choice == 5:
            search_project.search_project(email)
        elif choice == 6:
            print("Okay beybey \N{loudly crying face}")
        else:
            print("Invalid Number. Please try again \N{loudly crying face}")
            login_menu(useremail)


