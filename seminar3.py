# Задание No1
# ✔ Вручную создайте список с целыми числами, которые
# повторяются. Получите новый список, который содержит
# уникальные (без повтора) элементы исходного списка.
# ✔ *Подготовьте два решения, короткое и длинное, которое
# не использует другие коллекции помимо списков.

# my_list = [1,2,3,3,4,5,5,6,7,2,2,3]
# print (my_list)
# 
# result=[]
# for i in my_list:
#     if i not in result:
#         result.append(i)
#         
# print (result)
# 
# result = set(my_list)
# print (result)

# 
# Задание No3
# Погружение в Python | Коллекции
# Пользователь вводит данные. Сделайте проверку данных
# и преобразуйте если возможно в один из вариантов ниже:
# ✔ Целое положительное число
# ✔ Вещественное положительное или отрицательное число
# ✔ Строку в нижнем регистре, если в строке есть
# хотя бы одна заглавная буква
# ✔ Строку в нижнем регистре в остальных случаях
# 
# def reformat(text: str) -> (int, float, str):
#     result = None
#     if text.isdigit():
#         if "." not in text:
#             result = int(text)
#         else:
#             result = float(text)
#     elif text.lower() != text:
#         result = text.lower()
#     else:
#         result = text.upper()
#     return result
# 
# print(reformat("12345"))
# print(reformat("123.45"))
# print(reformat("текст"))
# print(reformat("Текст"))
# 



