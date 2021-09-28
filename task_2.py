'''2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.'''

with open('text_file_task-2.txt') as file:
    i = 1
    for element in file.readlines():
        print(f'Количество слов в строке {i}: {len(element.split())}')
        i += 1
    count_lines = len(file.readlines())
    print(f'Количество строк в файле: {i - 1}')
