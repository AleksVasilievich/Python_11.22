# from baza_dist import student_dist

student_nick = {}

def add_student():
    student_nick[input('Введите Фамилию и Имя: ')] = input('Введите, класс, пара, вариант через пробел: ').split()
    return student_nick
    
    

def add_grade():
    student_nick[input('Введите Фамилию и Предмет: ')] = input('Введите оценки: ').split()
    return student_nick