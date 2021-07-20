'''3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.'''

with open('text_file_task-3.txt', encoding='utf-8') as file:
    my_list = []
    average_salary = 0
    for el in file.readlines():
        average_salary += int(el.split()[1])
        if int(el.split()[1]) < 20:
            my_list.append(el.split()[0])
    print(f'Сотрудники у которых оклад менее 20 тысяч рублей: {my_list}')
    file.seek(0)
    print(f'Средняя величина дохода сотрудников: {average_salary / len(file.readlines())}')