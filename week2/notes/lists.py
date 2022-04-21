students = ["Hermoine", "Harry", "Ron"]
print(students)


for student in students:
    print(student)

print(students[0])
print(students[1])
print(students[2])

print("------------")
print(students[::]) # from beginning to an end
print("------------")
print(students[:1]) # from begining to index 1 excluded, there is a STOP BLOCK before index 1
print("------------")
print(students[1:]) # from index 1 included to the end
print("------------")
print(students[1:-1]) # from index 1 to last index excluded, there is a STOP BLOCK before last index


# len()
print("------------")
for i in range(len(students)):
    print(i + 1, students[i])