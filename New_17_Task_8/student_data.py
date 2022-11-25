# from baza_dist import student_dist, grade_dist
from teacher import add_student, add_grade, student_nick
import json



def student_new():
    # with open('New_17_Task_8\student_t.txt', 'w', encoding= 'utf-8') as data:
    #     data.write(add_student())
    
    # # with open('New_17_Task_8\student_j.json', 'a', encoding= 'utf-8') as outfile:
    json.dump(add_student(), open('New_17_Task_8\student_j.json', 'a'))
    print(student_nick)

def student_grade():
    json.dump(add_grade(), open('New_17_Task_8\student_j.json', 'a'))
    print(student_nick)

def student_see():
    path = 'New_17_Task_8\student_j.json'
    data = open(path, 'r', encoding='utf_8')
    for line in data:
       print(line, end='')
