
class Employee():
 def __init__(self, id, name, salary, designation):
    self.name = name
    self.id = id
    self.salary = salary
    self.designation = designation


class Developer(Employee):
 def __init__(self, id, name, salary):
     super().__init__(id, name, salary, "Developer")


class Tester(Employee):
 def __init__(self, id, name, salary):
    super().__init__(id, name, salary, "Tester")


class Manager(Employee):
 def __init__(self, id, name, salary):
    self.count = 1
    super().__init__(id, name, salary, "Manager")
 def adddeveloper(self, id, name, salary):
    d = Developer(id, name, salary)
    self.count += 1
    return d
 def removedeveloper(self, dv):
    del dv
    self.count -= 1
 def addtester(self, id, name, salary):
    t = Tester(id, name, salary)
    self.count += 1
    return t
 def removetester(self, tt):
     del tt
     self.count -= 1
 def employeecount(self):
    return self.count


if __name__ == '__main__':
 print("\nHello Employee")
 id = int(input("Enter your ID : "))
 name = input("Enter your name : ")
 salary = int(input("Enter your salary : "))
 role = int(
     input("What is your designation?\n1)Manager\n2)Developer\n3)Tester\nEnter - "))
 if role == 1:
    M = Manager(id, name, salary)
 print(f"Hello {M.name}")
 dev, tes = [], []
 while 1:
    ch = int(input("\nWhat do you want to do?\n1)Add Developer\n2)Remove Developer\n3)AddTester\n4)Remove Tester\n5)Employee Count\n6)Quit the system\nEnter - "))
    if ch == 1:
        id=int(input(" Enter ID : "))
        name=input(" Enter name : ")
        salary=int(input(" Enter salary : "))
        d=M.adddeveloper(id, name, salary)
        dev.append(d)
    elif ch == 2:
        print(f"Developers : ")
        i=1
        for item in dev:
            print(f"{i}) {item.name}(ID: {item.id})", end=", ")
            i += 1
        id=int(input("Enter index to be deleted : "))
        dv=dev[id-1]
        M.removedeveloper(dv)
        dev.remove(dv)
    elif ch == 3:
        id=int(input(" Enter ID : "))
        name=input(" Enter name : ")
        salary=int(input(" Enter salary : "))
        t=M.addtester(id, name, salary)
        tes.append(t)
    elif ch == 4:
        print(f"Testers :")
        i=1
        for item in tes:
            print(f"{i}) {item.name}(ID: {item.id})", end=", ")
            i += 1
            id=int(input("Enter the index to be removed : "))
            tt=tes[id-1]
            M.removetester(tt)
            tes.remove(tt)
    elif ch == 5:
     k=M.employeecount()
     print(" Employee count is "+str(k))
     print(f" Developers : ")
     i=1
     for item in dev:
         print(f" {i}) {item.name}(ID: {item.id})", end=", ")
         i += 1
     print(f"\n Testers :")
    i=1
    for item in tes:
        print(f" {i}) {item.name}(ID: {item.id})", end=", ")
        i += 1
    else:
            print("Bye!")
 exit()
print()
