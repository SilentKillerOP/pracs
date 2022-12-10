inputt = open('input.txt', 'w+')
numbers = input('Enter numbers:')
inputt.writelines(numbers)
numbers = numbers.split(' ')
n = []
for i in numbers:
    n.append(int(i))

inputt.close()
outputt = open('output.txt', 'w+')
n.sort()

for i in n:
    outputt.write(str(i)+" ")

outputt.close()
