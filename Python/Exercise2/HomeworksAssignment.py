import json



class homeworkAssignment:
    def __init__(self, subj, title, due_date):
        self.subj = subj
        self.title = title
        self.due_date = due_date

    def manage_homeworks(self):
        print("--------What kind of operation you need to do?--------\n")
        print("1: Add a new homework             2: delete a homework\n")
        print("3: Find homework                  4: return back\n")
        print("------------------------------------------------------\n")
        a = input("type here: ")
        if a == "1":
            self.add_homework()
        elif a == "2":
            self.delete_homework()
        elif a == "3":
            self.find_homework()
        elif a == "4":
            return
        else:
            print("Invalid input, try again")
    
    def add_homework(self):
        try:
            with open("Homeworks.json", "r") as f:
                data = json.load(f)
        except:
            data = {}
        print(data)
        new_homework = {
            self.title: [self.subj, self.due_date],
        }
        for t in data.keys():
            if t == self.title:
                print("There is already a homework with this name")
                return
        data.update(new_homework)
        with open("Homeworks.json", "w") as f:
            json.dump(data, f, indent=4)
        print("Homework added successfully!")
    
    def delete_homework(self):
        try:
            with open("Homeworks.json", "r") as f:
                data = json.load(f)
        except:
            data = {}
        data1 = {t: info for t, info in data.items() if t != self.title}
        print(data)
        print(data1)
        if data1 != data:
            with open("Homeworks.json", "w") as f:
                json.dump(data1, f, indent=4)
            print("Homework deleted successfully!")
        else:
            print("There's no such homework! Check if all infos are correct")

    def find_homework(self):
        try:
            with open("Homeworks.json", "r") as f:
                data = json.load(f)
        except:
            print("No homeworks available yet.")
            return
        data1 = {t: info for t, info in data.items() if t == self.title}
        print(data, type(data))
        print(data1)
        if data1:
            print("Homework found: ", data1)
        else:
            print("There's no such homework! Check if all infos are correct")