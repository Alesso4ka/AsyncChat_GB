import subprocess
import locale

"""1. Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате
и проверить тип и содержание соответствующих переменных. Затем с помощью
онлайн-конвертера преобразовать строковые представление в формат Unicode и также
проверить тип и содержимое переменных. Затем с помощью онлайн-конвертера преобразовать
в набор кодовых точек Unicode (НО НЕ В БАЙТЫ!!!) и также проверить тип и содержимое переменных.

*Попытайтесь получить кодовые точки без онлайн-конвертера!
без хардкода!

Подсказки:
--- 'разработка' - буквенный формат
--- '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430' - набор кодовых точек
--- используйте списки и циклы, не дублируйте функции
"""

print('**№ 1 v1 **')
word_1 = 'разработка'
word_2 = 'сокет'
word_3 = 'декоратор'
print(type(word_1), type(word_2), type(word_3))
print((word_1, word_2, word_3))

word_1 = '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430'
word_2 = '\u0441\u043e\u043a\u0435\u0442'
word_3 = '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'
print(type(word_1), type(word_2), type(word_3))
print((word_1, word_2, word_3))

print('**№ 1 v2 **')

strs = ['разработка', 'сокет', 'декоратор']

for s in strs:
    print(type(s), s)

strs_unicode = [
    '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430',
    '\u0441\u043e\u043a\u0435\u0442',
    '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'
]

for s in strs_unicode:
    print(type(s), s)

"""2. Каждое из слов «class», «function», «method» записать в байтовом типе
без преобразования в последовательность кодов (не используя методы encode
 и decode) и определить тип, содержимое и длину соответствующих переменных. 
Подсказки:
--- b'class' - используйте маркировку b''
--- используйте списки и циклы, не дублируйте функции"""

print('** № 2 v1 **')
word_1 = b'class'
word_2 = b'function'
word_3 = b'method'

print(type(word_1), type(word_2), type(word_3))
print(word_1, word_2, word_3)
print((len(word_1), len(word_2), len(word_3)))

print('** № 2 v2 **')
words = []
words.append(b'class')
words.append(b'function')
words.append(b'method')

for word in words:
    print(word)
    print(type(word))
    print(len(word))

"""3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в
байтовом типе с помощью маркировки b'' (без encode decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
--- обязательно!!! усложните задачу, "отловив" исключение,
придумайте как это сделать"""

print('** № 3 v1 **')
word_1 = b'attribute'
word_2 = 'класс'.encode('utf-8')  # невозможно записать в байтовом типе
word_3 = 'функция'.encode('utf-8')  # невозможно записать в байтовом типе
word_4 = b'type'

print((word_1, word_2, word_3, word_4))

print('** № 3 v2 **')
words = []
words.append(b'attribute')  # возможно
words.append(b'класс')  # невозможно записать SyntaxError: bytes can only contain ASCII literal characters.
words.append(b'функция')  # невозможно записать SyntaxError: bytes can only contain ASCII literal characters.
words.append(b'type')  # возможно

for word in words:
    print(word)
    print(type(word))
    print(len(word))

"""4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из
строкового представления в байтовое и выполнить обратное преобразование (используя
методы encode и decode).
Подсказки:
--- используйте списки и циклы, не дублируйте функции"""

print('** № 4 v1 **')
word_1 = 'разработка'.encode('utf-8')
word_2 = 'администрирование'.encode('utf-8')
word_3 = b'protocol'
word_4 = b'standard'

print((word_1, word_2, word_3, word_4))
word_1 = word_1.decode('utf-8')
word_2 = word_2.decode('utf-8')
word_3 = word_3.decode('utf-8')
word_4 = word_4.decode('utf-8')
print((word_1, word_2, word_3, word_4))

print('** № 4 v2 **')
words = []
words.append("разработка")
words.append("администрирование")
words.append("protocol")
words.append("standard")

# b_words = []

for word in words:
    print(word)
    print(type(word))
    b_word = str.encode(word, encoding='utf-8')
    print(b_word)
    print(type(b_word))
    s_word = bytes.decode(b_word, encoding='utf-8')
    print(s_word)
    print(type(s_word))
    print()

"""5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из
байтовового в строковый тип на кириллице."""

print('** № 5 v1 **')
import subprocess
import chardet
import os

args_1 = ['ping', 'yandex.ru']
args_2 = ['ping', 'youtube.com']
ya_ping = subprocess.Popen(args_1, stdout=subprocess.PIPE)
print(ya_ping.stdout)
for line in ya_ping.stdout:
    res = chardet.detected(line)
    print(line.decode(encoding=res['encoding']))
ytb_ping = subprocess.Popen(args_2, stdout=subprocess.PIPE)
print(ytb_ping.stdout)
for line in ytb_ping.stdout:
    res = chardet.detected(line)
    print(line.decode(encoding=res['encoding']))