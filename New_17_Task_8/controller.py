from student_data import student_new, student_grade, student_see


def start():
    if int(input('Введите 1 - если учитель, 2 - если ученик : ->  ')) == 1:
        if int(input('Введите: 1 - для записи ученика, 2 - для выстаиления оценки: '
                 )) == 1:
            student_new()
        else: 
            student_grade()
    else : 
        student_see()


