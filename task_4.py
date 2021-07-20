'''4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.'''

my_list = []

with open('task_4.txt', encoding='UTF-8') as file:
    for element in file.readlines():
        my_list.append(element)
i = 0
for el in my_list:
    if el.split()[0] == 'One':
        my_list[i] = 'Один - 1'
    elif el.split()[0] == 'Two':
        my_list[i] = 'Два - 2'
    elif el.split()[0] == 'Three':
        my_list[i] = 'Три - 3'
    elif el.split()[0] == 'Four':
        my_list[i] = 'Четыре - 4'
    i += 1

with open('task_4_for_write.txt', 'w', encoding='UTF-8') as new_file:
    for el in my_list:
        print(f'{el}', file=new_file)



