Track_1 = {
    "Open": 98,
    "Closed": 78,
    "Deferred": 43,
    "name":"Kiran R"

}
Track_2 = {
    "Open" : 56,
    "Closed" : 91,
    "Deferred" : 91,
    "name" : "Abdul"
}


Track_List = [Track_1,Track_2]

#print(Student_List)
min_marks = 0
highest_score_student = ''

for Name in Track_List:
    if (Name.get("Open") > min_marks):
        min_marks = Name.get("Open")
        highest_score_student = Name.get('name')

print(f"highest Open defects is {min_marks} by {highest_score_student}")

min_Science = 0
highest_score_science =''

for Name in Track_List:
    if (Name.get("Closed") > min_Science):
        min_Science = Name.get("Closed")
        highest_score_science = Name.get('name')
print(f"highest Closed defects is {min_Science} by {highest_score_science}")


