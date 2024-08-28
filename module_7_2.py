def custom_write(file_name, strings):
    string_positions = {}
    file_name = open(file_name, 'a+t', encoding='utf-8')
    line = 0  # номер строки
    for item in strings:
        keys = []  # Строка, байт начала строки
        values = []  # Записываемая строка
        line += 1
        keys.append(line)
        keys.append(file_name.tell())
        keys = [tuple(keys)]
        file_name.write(f'{item} \n')
        values.append(item)
        string_positions.update(dict(zip(keys, values)))
    file_name.close()
    return string_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
