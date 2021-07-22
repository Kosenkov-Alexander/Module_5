'''6. Необходимо создать (не программно) текстовый файл,
где каждая строка описывает учебный предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.'''
summ_lessons = 0
my_dict = {}
with open('task_6.txt', encoding='UTF-8') as file:
    for element in file.readlines():
        key = element.split()[0].replace(':', '')
        for item in element.split():
            try:
                summ_lessons += int(item)
            except ValueError:
                continue
        my_dict[key] = summ_lessons
        summ_lessons = 0

print(my_dict)

