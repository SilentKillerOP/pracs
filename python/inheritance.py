class Employee:
    def __init__(self,name,surname,ssn):
        self.name = name
        self.surname = surname
        self.ssn = ssn
       

class Developer(Employee):
    def __init__(self, name, surname, ssn,stack,language):
            super().__init__(name, surname, ssn)
            self.stack = stack
            self.language = language

class Tester(Employee):
    def __init__(self, name, surname, ssn,stack,language):
            super().__init__(name, surname, ssn)
            self.language = language
            self.stack = stack

class Role:
    def __init__(self,role):
        self.role = role

class Manager(Employee,Role):
    developer_list = []
    tester_list = []
    def __init__(self, name, surname, ssn,role):
        super().__init__(self,name,surname,ssn,)
        Role.__init__(self,role)
        
    def add_dev(self):
        if self.role.lower() == "developer":
            if self.name not in Manager.developer_list:
                Manager.developer_list.append(self.name)
    
    def remove_dev(self):
        if self.role.lower() == "developer":
            if self.name  in Manager.tester_list:
                Manager.developer_list.remove(self.name)

    def add_tester(self):
        if self.role.lower() == "tester":
            if self.name not in Manager.tester_list:
                Manager.tester_list.append(self.name)
    
    def remove_tester(self):
        if self.role.lower() == "tester":
            if self.name  in Manager.tester_list:
                Manager.tester_list.remove(self.name)
    

while True:
    ssn_count = 1
    print("*"*50)
    print("Welcome to the Employee Management System")
    emp_name = input("Enter your name: ")
    emp_surname = input("Enter your surname: ")
    manager_name = input("Enter your manager's name: ")
    emp_role = input(f"Hello {emp_name}! Please enter your role either developer or tester: ")
    manager = Manager(name = manager_name,surname = emp_surname,ssn = ssn_count,role = emp_role,dept = "Marketing",stack ="Data analysis",language = "Python")
    ssn_count+=1
    print("*"*50)
    choice = int(input("Enter what do you want to do?\n1.Add a developer\n2.Remove a developer\n3.Add a Tester\n4.Remove a Tester\n5.To exit\n"))
    if choice ==1:
        manager.add_dev() 

    elif choice==2:
        manager.remove_dev()

    elif choice==3:
        manager.add_tester()
    
    elif choice==4:
        manager.remove_tester()

    else:
        break
    
    exit = input("Would you like to end (y/n): ")
    if exit == 'y':
        break
    else:
        continue
    

print(f"Developer list is:{manager.developer_list}")
print(f"Tester list is:{manager.tester_list}")


    