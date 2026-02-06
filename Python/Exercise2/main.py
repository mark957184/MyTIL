from datetime import datetime
import HomeworksAssignment
import dotenv, os
b = dict(dotenv.dotenv_values("PossibleLogins.env"))
b = [pa for pa in b.values()]
c = dict(dotenv.dotenv_values("TeachersSubj.env"))

def main():
    a = input("Please login to access homeworks (name:password): ")
    if a in b:
        print("Login successful!\n")
        a = a.split(":")
        d = [subj for d, subj in c.items() if d == a[0]]
        a[1] = d[0]
        print(f"Welcome back, {a[0]}!\n")
        while True:
            e = input("Insert the title of the homework: \n")
            if not e:
                print("Title cannot be empty, try again")
                continue
            else:
                f = input("Insert the due date of the homework (DD/MM/YYYY): \n")
                try:
                    datetime.strptime(f, "%d/%m/%Y")
                    teacher = HomeworksAssignment.homeworkAssignment(a[1], e, f)
                    teacher.manage_homeworks()
                    continue
                except ValueError:
                    print("Invalid date format. Please use DD/MM/YYYY.")
                    continue    
main()
