from tokenize import endpats

with open('26.txt') as file:
    windows_count = int(file.readline())
    tasks_count = int(file.readline())
    tasks = file.readlines()

tasks = [task.split() for task in tasks]
tasks = [(int(s), int(e)+4) for s, e in tasks]
tasks = sorted(tasks)

ind = 0
count = 0
w = [0] * windows_count
for start, end in tasks:
    for i, window in enumerate(w):
        if start >= window:
            w[i] = end
            ind = i+1
            count += 1
            break

print(count, ind)

# 1132 5




