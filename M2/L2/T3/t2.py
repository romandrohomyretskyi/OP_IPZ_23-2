'''
Виправте помилки (розставте правильно відступи!).
Програма повинна множити або ділити два числа. 
При цьому, якщо задана операція не ділення, 
виконується множення. Операція ділення проводиться 
з перевіркою: при спробі поділу на 0 виводиться помилка.
'''

a = int(input("Введи перше число: "))
b = int(input("Введи друге число: "))
op = input("Введи операцію (ділення чи множення): ")
error1 = "Помилка: ділити на нуль не можна!"
if op == "/":
if b == 0:
print(error1)
else:
print(a/b)
else:
print(a*b)
