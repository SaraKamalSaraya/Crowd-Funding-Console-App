import os, time, re, datetime
import login_menu

def edit_start_date(email,title):
    user_email = email
    project_title = title
    print("Start Editing Start Date process \N{grinning face}")
    edit_start_date = Edit_Start_Date(user_email,project_title)

class Edit_Start_Date:
    def __init__(self,email,title):
        self.email = email
        self.title = title
        self.edit_start_date()
    
    def edit_start_date(self):
        flag = 0
        with open("projects.txt") as file:
            projects = file.readlines()
            for project in projects:
                project = project.strip("\n")
                project_info = project.split(":")
                if self.email == project_info[0]:
                    if self.title == project_info[1]:
                        print(f"Your Start Date should be befor {project_info[5]}")
                        while True:
                            new_start_date = input("Enter Your New Start Date: ")
                            from datetime import datetime
                            year = datetime.now().year
                            month = datetime.now().month
                            day = datetime.now().day
                            now = f"{year}-{month}-{day}"
                            now = datetime.strptime(now,'%Y-%m-%d')
                            now = str(now.strftime('%Y-%m-%d'))
                            pattern_str = r'^\d{4}-\d{2}-\d{2}$'
                            end_date = project_info[5].strip()
                            end_date = datetime.strptime(end_date, '%Y-%m-%d')
                            end_date = str(end_date.strftime('%Y-%m-%d'))
                            try:
                                if re.match(pattern_str, new_start_date):
                                    datetime.strptime(new_start_date, '%Y-%m-%d')
                                    if new_start_date < now:
                                        print("Start date can't be before Today. \N{unamused face}")     
                                    else:
                                        if new_start_date < end_date:
                                            break
                                        else:
                                            print("Can't start before end")
                                else:
                                    print("Incorrect data format, should be YYYY-MM-DD \N{unamused face}")
                            except ValueError:
                                print("Incorrect data format, should be YYYY-MM-DD \N{unamused face}")

                        project_info[4] = new_start_date
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