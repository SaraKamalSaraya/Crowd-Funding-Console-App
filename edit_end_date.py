import os, time, re, datetime
import login_menu

def edit_end_date(email,title):
    user_email = email
    project_title = title
    print("Start Editing End Date process \N{grinning face}")
    edit_end_date = Edit_End_Date(user_email,project_title)

class Edit_End_Date:
    def __init__(self,email,title):
        self.email = email
        self.title = title
        self.edit_end_date()
    
    def edit_end_date(self):
        flag = 0
        with open("projects.txt") as file:
            projects = file.readlines()
            for project in projects:
                project = project.strip("\n")
                project_info = project.split(":")
                if self.email == project_info[0]:
                    if self.title == project_info[1]:
                        print(f"Your End Date should be after {project_info[4]}")
                        while True:
                            new_end_date = input("Enter Your New End Date: ")
                            pattern_str = r'^\d{4}-\d{2}-\d{2}$'
                            start_date = project_info[4].strip()
                            start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
                            start_date = str(start_date.strftime('%Y-%m-%d'))
                            try:
                                if re.match(pattern_str, new_end_date):
                                    datetime.datetime.strptime(new_end_date, '%Y-%m-%d')
                                    if start_date < new_end_date:
                                        break
                                    else:
                                        print("Start date can't be equal or before End date. \N{unamused face}")
                                else:
                                    print("Incorrect data format, should be YYYY-MM-DD \N{unamused face}")
                            except ValueError:
                                print("Incorrect data format, should be DD-MM-YYYY \N{unamused face}")

                        project_info[5] = new_end_date
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



