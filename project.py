tasks = []
tasks.append("wash dishes")
tasks.append("fold clothes")
tasks.append("water plants")
tasks.append("rake leaves")

print(tasks)

del tasks[2]
print(tasks)
removeByName = tasks.remove("rake leaves")
print(tasks)
sortedList = tasks.sort()
print(tasks)
reverseList = tasks.reverse()
print(tasks)