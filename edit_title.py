from create_project import check_title
import os, time
import login_menu

def edit_title(email,title):
    user_email = email
    project_title = title
    print("Start Editing Title process \N{grinning face}")
    edit_title = Edit_Title(user_email,project_title)

class Edit_Title:
    def __init__(self,email,title):
        self.email = email
        self.title = title
        self.edit_title()
    
    def edit_title(self):
        flag = 0
        with open("projects.txt") as file:
            projects = file.readlines()
            for project in projects:
                project = project.strip("\n")
                project_info = project.split(":")
                if self.email == project_info[0]:
                    if self.title == project_info[1]:
                        while True:
                            newTitle = input("Enter Your New Title : ")
                            if self.title.isalpha() and check_title(newTitle):
                                break
                            else:
                                print("Invalid naming of a title, Try again")
                        project_info[1] = newTitle
                        finalInfor = ":".join(project_info)
                        with open("temp.txt", "a") as edit_file:
                            data = finalInfor.strip("\n")
                            data = f"{data}\n"
                            edit_file.writelines(data)
                            print("Done !!!")
                            flag = 1
                    else:
                        project_info = ":".join(project_info)
                        with open("temp.txt", "a") as not_edit_file:
                            data = project_info.strip("\n")
                            data = f"{data}\n"
                            not_edit_file.writelines(data)

                else:
                    project_info = ":".join(project_info)
                    with open("temp.txt", "a") as not_edit_file:
                        data = project_info.strip("\n")
                        data = f"{data}\n"
                        not_edit_file.writelines(data)

        if flag == 0:
            print(f"We can not found a title with this name [{self.title}]")

        os.remove("projects.txt")
        os.rename("temp.txt", "projects.txt")
        print("Redirecting to Login Menu ...")
        time.sleep(2.0)
        login_menu.login_menu(self.email)
