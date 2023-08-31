# Задача 1
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

# Вариант 1
# n = "a a a b c a a d c d d".split()
# print (n)
# s = ""
# for i in range(len(n)):
#     s = n[:i]
#     if s.count(n[i]) == 0:
#         print(n[i], end=" ")
#     else:
#         print(f"{n[i]}_{s.count(n[i])}", end=" " )

# Вариант 2

# lst = 'a a a b c a a d c d d'.split()
# lst1 = ''
# test ={}
# for i in lst:
#     if i not in test:
#         test[i] = 0
#         lst1 += i + ' '
#     else:
#         test[i] += 1
# lst1 += (f'{i}_{test[i]} ')
# print(lst1)

# st =''
# for i, ch in enumerate(lst):
#     if (_:= lst[:i].count(ch)) > 0:
#         st += (f'{ch}_{_} ')
# else:
#     st += ch + ' '
# print(st)

# Вариант 3
# all_letters = 'a b c a d b d d b c a a'.split()
# letters_count = {}
# result_str = ''
# for letter in all_letters:
#     if letter not in letters_count:
#         letters_count[letter] = 1
#         result_str += f'{letter} '
# else:
#     result_str += f'{letter}_{letters_count[letter]} '
#     letters_count[letter] += 1

# print(result_str)

# Задача 2
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells

# print(len(set(input().split())))

# Вариант 2 (не отвечает условию, но если текст надо использовать в дальнейшем)

# n = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea \
# shells on the sea shore I'm sure that the shells are sea shore shells"
# print(len(set(n.split())))

# Задача 3
# Ваня и Петя поспорили, кто быстрее решит
# следующую задачу: “Задана последовательность
# неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента
# последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в
# последовательность)”. Однако 2 друга оказались не
# такими смышлеными. Никто из ребят не смог до
# конца сделать это задание. Они решили так: у кого
# будет меньше ошибок в коде, тот и выиграл спор. За
# помощью товарищи обратились к Вам, студентам.

# m = 0
# while (n:= int(input())) != 0:
#     if n > m:
#         m = n
# print (m)

# Вариант 2
# max_el = 0
# while ((_ := int(input('Введите число: '))) != 0):
#     if max_el < _:
#         max_el = _
# print(max_el)