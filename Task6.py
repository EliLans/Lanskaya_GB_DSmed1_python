#Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text. Продолжить работу над заданием.
# В программу должна попадать строка из слов, разделенных пробелом. Каждое слово состоит из латинских букв
# в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().

def int_func(text):
    word = text[0].upper() + text[1:].lower()
    return word

string = input("Введите слова через пробел: ")
for word in string.split(" "):
    print(f'{int_func(word)}')