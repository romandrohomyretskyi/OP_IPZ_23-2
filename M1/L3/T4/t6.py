'''
Напишіть програму, яка переводить градуси за Фаренгейтом в градуси за Цельсієм. 
TODO Відповідь програма повинна друкувати в один рядок в такому форматі:  "градусів Цельсія: <відповідь>"
Програма працює за таким алгоритмом:
(Пункт 1). Запитує число в градусах за Фаренгейтом. Людина вводить рядок, який потрібно перетворити в число.

(Пункт 2). Далі від цього числа треба відняти 32.

(Пункт 3). Результат помножити на 5 і розділити на 9.

(Пункт 4). Тепер рядок "градусів Цельсія:" потрібно об'єднати з кінцевою відповіддю, 
але відповідь спочатку переводиться з числа в рядок!

(Пункт 5). Останнє: надрукувати результат (наприклад, "градусів Цельсія: 232.777").
'''


a = int(input ("Напишіть число в Фаренгейтах:"))
b = a - 32
c = b*5/9
print ("Градусів Цельсія: ", c)