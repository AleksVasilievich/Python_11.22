# from baza_dist import student_dist

student_nick = {}

def add_student():
    student_nick[input('Введите Фамилию и Имя: '  )] = input('Введите, класс, пара, вариант через пробел: ').split()
    # return dict(input())
    # return ','.join(input().split(','))
    # return input('Введите данные (Фамилия, Имя, класс через пробел): ').split(' ')
    # baza[input('Введите фамилию и имя: ')] = input('Введите класс, парта, вариант: через пробел: ')
    return student_nick
# print(baza)
    
    

def add_grade():
    # studen_g = input('Введите оценки через пробел: ').split()
    # return dict(input())
    # return ','.join(input().split(','))
    return ' '.join(input('Введите оценки через пробел: ').split())