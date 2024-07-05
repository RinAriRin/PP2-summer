#task 1 Напишите программу на Python, которая соответствует строке, за которой следует ноль или более 's.'a''b'
import re
txt = input("Введите строку: ")
x = re.search(r'a(s*)b', txt)
if x:
    print("Найдено совпадение:", x.group())
else:
    print("Совпадений не найдено")

#task 2 Напишите программу на Python, которая соответствует строке, за которой следует от двух до трех .'a''b'
import re
txt = input("Введите строку: ")
x = re.search(r'a(b{2,3})', txt)
if x:
    print("Найдено совпадение:", x.group())
else:
    print("Совпадений не найдено")

#task 3 Напишите программу на Python для поиска последовательностей строчных букв, соединенных подчеркиванием.
import re
txt = input("Введите строку: ")
x = re.findall(r"[a-z]+_[a-z]+", txt)
if x:
    print("Найдено совпадение:", x)
else:
    print("Совпадений не найдено")


#task 4  Напишите программу на Python для поиска последовательностей одной прописной буквы, за которой следуют строчные буквы.
import re

txt = input("Введите строку: ")
x = re.findall(r'[A-Z][a-z]+', txt)
if x:
    print("Найдено совпадение:", x)
else:
    print("Совпадений не найдено")

#task 5 Напишите программу на Python, которая соответствует строке, за которой следует что-либо, оканчивающееся на .'a''b'
import re
txt = input("Введите строку: ")
x = re.search(r'a.*b$', txt)
if x:
    print("Найдено совпадение:", x.group())
else:
    print("Совпадений не найдено")

#task 6 Напишите программу на Python, чтобы заменить все вхождения пробела, запятой или точки двоеточием.
import re
txt = input("Введите строку: ")
x = re.sub(r'[ .,]', ':', txt)
print(x)

#task 7 Напишите программу на python для преобразования строки регистра змеи в строку регистра верблюда.
import re
txt = 'hello_world'
txt2 = txt.upper()
camel = ''
i = 0
while(i != len(txt)):
    if txt[i] == '_':
        camel += txt[i] + txt2[i+1]
        i += 2
    else:
        camel += txt[i]
        i += 1
camel = re.sub('_', '', camel)
print(camel)

#task 8 Напишите программу на Python для разделения строки на прописные буквы.
import re
txt = input("Введите строку: ")
x = re.findall('[A-Z][^A-Z]*', txt)
print(x)

#task 9 Напишите программу на Python для вставки пробелов между словами, начинающимися с заглавных букв.
import re
str = "HelloWorld"
x = re.sub(r"([A-Z])", r" \1", str)
print(x)

#task 10 Напишите программу на Python для преобразования заданной строки верблюжьего регистра в змеиный регистр.
import re

camel = input("Введите строку в верблюжьем регистре: ")
snake = re.sub(r"([A-Z])", r"_\1", camel)
snake = snake.lower()
if snake.startswith('_'):
    snake = snake[1:]
print("Строка в змеином регистре:", snake)

