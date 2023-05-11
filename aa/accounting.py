def print_arr(arr, n):
    for i in range(n):
        print(arr[i], end=" ")
    print()

size = 1
count = 0
arr = [None] * size
p = arr
account = 0

print("Initial account balance =", account)
print()

while True:
    n = int(input("Enter the number you wish to insert in the dynamic table: "))
    account += 3  # adding 3 to the account

    if count < size:
        p[count] = n
        count += 1
        print_arr(p, count)
        account -= 1
    else:
        print("Double")
        new_arr = [None] * (size * 2)
        for i in range(count):
            new_arr[i] = p[i]
        account -= count
        p = new_arr
        p[count] = n
        size *= 2
        count += 1
        account -= 1
        print_arr(p, count)

    print("Account balance:", account)
    print()

# https:://raw.githubusercontent.com/SilentkillerOP/pracs/sem6/aa/accounting.py