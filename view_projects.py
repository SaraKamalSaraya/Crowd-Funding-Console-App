import login_menu
import time

def view_projects(email):
    user_email = email
    print("Choose one of the following:")
    print("[1] View All Projects")
    print("[2] View Only Your Projects")
    print("[3] Back to Login Menu")
    choice = input("Your choice is: ")

    if not choice.isnumeric():
        print("Invalid input. Please try again \N{unamused face}")
        view_projects(user_email)
    else:
        choice = int(choice)
        if choice == 1:
            view_all_projects(user_email)
        elif choice == 2:
            view_only_your_projects(user_email)
        elif choice == 3:
            print("Okay beybey \N{loudly crying face}")
            login_menu.login_menu(user_email)
        else:
            print("Invalid Number. Please try again \N{loudly crying face}")
            view_projects(user_email)


def view_all_projects(email):
    user_email = email
    with open("projects.txt","r") as file:
        projects = file.readlines()
        counter = 1
        flag = 0
        for project in projects:
            project = project.strip("\n")
            project_info = project.split(":")
            if project_info == [""]:
                flag = 0
            else:
                print(f"Project number {counter}:")
                print(f"User Email: {project_info[0]}")
                print(f"Title: {project_info[1]}")
                print(f"Details: {project_info[2]}")
                print(f"Target: {project_info[3]}")
                print(f"Start Date: {project_info[4]}")
                print(f"End Date: {project_info[5]}")
                counter += 1
                flag = 1
        if flag == 0:
            print("Their are no current projects")
        print("Redirecting to Login Menu ...")
        time.sleep(2.0)
        login_menu.login_menu(user_email)


def view_only_your_projects(email):
    user_email = email
    with open("projects.txt","r") as file:
        projects = file.readlines()
        counter = 1
        flag = 0
        for project in projects:
            project = project.strip("\n")
            project_info = project.split(":")
            if project_info == [""]:
                flag = 0
            else:
                if user_email == project_info[0]:
                    print(f"Project number {counter}:")
                    print(f"User Email: {project_info[0]}")
                    print(f"Title: {project_info[1]}")
                    print(f"Details: {project_info[2]}")
                    print(f"Target: {project_info[3]}")
                    print(f"Start Date: {project_info[4]}")
                    print(f"End Date: {project_info[5]}")
                    counter += 1
                    flag = 1
        if flag == 0:
            print("Their are no current projects")
        print("Redirecting to Login Menu ...")
        time.sleep(2.0)
        login_menu.login_menu(user_email)
