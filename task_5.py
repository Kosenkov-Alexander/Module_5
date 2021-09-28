'''5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.'''

with open('task_5.txt', 'w+') as file:
    print('7 10 3 20 30', file=file)
    file.seek(0)
    sum = 0
    my_list = file.readlines()
    for el in my_list[0].split():
        sum += int(el)

print(f'Сумма чисел равна: {sum}')