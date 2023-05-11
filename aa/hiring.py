import random

n = int(input("Enter the number of candidates to hire: "))
arr = [0] * n

for i in range(n):
    t = random.randint(1, 20)
    while t in arr:
        t = random.randint(1, 10)
    arr[i] = t

print("Skill score of all candidates are:")
for i in range(n):
    print(arr[i], end=" ")
print()

cost = 0
cost_hire = 100
cost_fire = 50
best = arr[0]
cost += cost_hire


for i in range(1, n):
    if arr[i] > best:
        print("Candidate hired", arr[i], "Candidate fired", best)
        best = arr[i]
        cost += cost_hire + cost_fire

print("Randomized Candidate hired", best, cost)

arr.sort()
best = arr[0]

for i in range(1, n):
    if arr[i] > best:
        print("Candidate hired", arr[i], "Candidate fired", best)
        best = arr[i]
        cost += cost_hire + cost_fire

print("Worst case Candidate hired", best, cost)
