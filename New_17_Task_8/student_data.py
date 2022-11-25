from baza_dist import student_dist, grade_dist

def student_new():
    with open('New_17_Task_8\student_j.json', 'w', encoding= 'utf-8') as data:
        data.write(student_dist())


def student_grade():
    with open('New_17_Task_8\student_t.txt', 'w', encoding= 'utf-8') as data:
        data.write(grade_dist())


def student_see():
    path = 'New_17_Task_8\student_t.txt'
    data = open(path, 'r', encoding='utf_8')
    for line in data:
       print(line)
    data.close()
