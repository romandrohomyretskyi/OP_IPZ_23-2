'''
Виведіть площу виділеного червоним трикутника.

1) Запросіть два числа a і b - сторони прямокутника.
2) Зверніть увагу: площа червоного трикутника дорівнює половині площі намальованого прямокутника!
Відповідь має відповідати формату виведення, як вказано в прикладі. 
Формула знаходження площі  прямокутника S = a * b.
'''


a = int(input("Введіть довжину сторони a прямокутника: "))
b = int(input("Введіть довжину сторони b прямокутника: "))

s = a * b
s = s / 2
print("Площа: ", s)