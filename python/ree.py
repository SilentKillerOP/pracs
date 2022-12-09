import re

tp = open('myfile.txt', 'r')

mail = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
number = r'\S[^a-zA-Z\n]+\d+\S[^a-zA-Z\n]'
sitee = r"(http|https)://[\w\-]+(\.[\w\-]+)+\S*"
name = r'Mr.+|Mrs.+'
m = tp.read()
m = m.split('\n')

mails = []
numbers = []
names = []

for i in m:
    if (re.match(mail, i)):
        mails.append(i)
    elif re.match(number, i):
        numbers.append(i)
    elif re.match(name, i):
        names.append(i)


print("Mails :",mails,"\nNumbers:", numbers,"\nNames:", names,"\n")
