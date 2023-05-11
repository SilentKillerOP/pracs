def print_arr(arr, n):
    for i in range(n):
        print(arr[i], end=" ")
    print()

size = 1
count = 0
arr = [None] * size
p = arr
cost = 0

while True:
    n = int(input("Enter the number you wish to insert in the dynamic table: "))

    if count < size:
        p[count] = n
        count += 1
        print(p)
        print_arr(p, count)
        cost += 1
    else:
        print("Double")
        new_arr = [None] * (size * 2)
        for i in range(count):
            new_arr[i] = p[i]
        cost += count + 1
        size *= 2
        new_arr[count] = n
        count += 1
        p = new_arr
        print(p)
        print_arr(p, count)

    print("Amortized Cost:", cost )
    print()
