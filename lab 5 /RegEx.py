#task 1 Напишите программу на Python, которая соответствует строке, за которой следует ноль или более 's.'a''b'
import re
txt = input()
x = re.search('a.*b', txt)
print(x)

#task 2 Напишите программу на Python, которая соответствует строке, за которой следует от двух до трех .'a''b'
txt = input()
x = re.search('a.{1}b', txt)
y = re.search('a.{2}b', txt)
if re.search('a.{1}b', txt):
    print(x)
elif re.search('a.{2}b', txt):
    print(y)
else:
    print("Error")

#task 3 Напишите программу на Python для поиска последовательностей строчных букв, соединенных подчеркиванием.
txt = 'wgeerger_egregerignerio'
x = re.findall("[a-z]+\_+[a-z]", txt)
if x:
    print(x)
else:
    print("No match")

#task 4  Напишите программу на Python для поиска последовательностей одной прописной буквы, за которой следуют строчные буквы.
txt = 'WFIWFNWFRoerjoiernwif'
x = re.findall('[A-Z]{1}[a-z]+', txt)
print(x)

#task 5 Напишите программу на Python, которая соответствует строке, за которой следует что-либо, оканчивающееся на .'a''b'
txt = 'wkgmwrgiuageoigjoijwfb'
x = re.search('a.*b$', txt)
print(x)

#task 6 Напишите программу на Python, чтобы заменить все вхождения пробела, запятой или точки двоеточием.
txt = 'nernnero imerimer,ofnrmer.wpomermpr'
x = re.sub('[ .,]', ';', txt, 4)
print(x)

#task 7 Напишите программу на python для преобразования строки регистра змеи в строку регистра верблюда.
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
txt = 'HelloWorld'
x = re.findall('[A-Z][^A-Z]*', txt)
print(x)

#task 9 Напишите программу на Python для вставки пробелов между словами, начинающимися с заглавных букв.

str = "HelloWorld"
x = re.sub(r"([A-Z])", r" \1", str)
print(x)

#task 10 Напишите программу на Python для преобразования заданной строки верблюжьего регистра в змеиный регистр.

camel = 'HelloWorld'
snake = re.sub(r"([A-Z])", r" \1", camel)
snake = snake.lower()
snake = snake.strip()
snake = re.sub(r'\s', '_', snake)
print(snake)
