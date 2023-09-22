import os, time
import login_menu

def delete_project(email):
    user_email= email
    print("Start Deleting process \N{grinning face}")
    title = input("Enter Title of Project you want to Delete: ")
    delete_project = Delete_Prpject(user_email,title)

class Delete_Prpject:
    def __init__(self,email,title):
        self.email = email
        self.title = title
        self.delete()

    def delete(self):
        flag = 0
        with open("projects.txt") as file:
            projects = file.readlines()
            for project in projects:
                project = project.strip("\n")
                project_info = project.split(":")
                if project_info[0] == self.email:
                    if project_info[1] == self.title:
                        finalInfor = ":".join(project_info)
                        with open("temp.txt","a") as edit_file:
                            data = finalInfor.strip("\n")
                            data = f"{data}\n"
                            if not (self.email == project_info[0] and self.title == project_info[1] ):
                                edit_file.writelines(data)
                                flag = 0
                            else:
                                print("Done!!! \N{grinning face}")
                                flag = 1
                    else:
                        project_info = ":".join(project_info)
                        with open("temp.txt","a") as not_edit_file:
                            data = project_info.strip("\n")
                            data = f"{data}\n"
                            not_edit_file.writelines(data)
                else:
                    project_info = ":".join(project_info)
                    with open("temp.txt","a") as not_edit_file:
                        data = project_info.strip("\n")
                        data = f"{data}\n"
                        not_edit_file.writelines(data)
        if flag == 0:
            print("No file with that title \N{unamused face}")
        os.remove("projects.txt")
        os.rename("temp.txt","projects.txt")
        print("Redirecting to Login Menu ...")
        time.sleep(2.0)
        login_menu.login_menu(self.email)