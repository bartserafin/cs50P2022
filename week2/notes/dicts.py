# using only lists
students = ["Hermoine", "Harry", "Ron", "Draco"]
houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]

# using dictionaries
students_dict = {
    "Hermoine": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin"
}

print("----")
print(students_dict["Hermoine"]) # give me a value of key "Hermoine"
print(students_dict["Draco"]) # give me a value of key "Draco"

print("----")
for student in students_dict:
    print(student) # it iterates over keys
    print(student, students_dict[student], sep=', ') # print -- student key, student value for key "student"


print("----")
students_data = [
    {"name": "Hermoine", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russel terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]

for student in students_data:
    print(student["name"], student["house"], student["patronus"], sep=", ")