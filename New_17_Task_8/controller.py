from student_data import student_new, student_grade, student_see


def start():
    if input('Введите 1 - если учитель, 3 - если ученик : ->  ') == '1':
        if input('Введите: 1 - для записи ученика, 2 - для выстаиления оценки '
                 ) == '1':
            student_new()
        elif input() == '2':
            student_grade()
    if input() == '3':
        student_see()


