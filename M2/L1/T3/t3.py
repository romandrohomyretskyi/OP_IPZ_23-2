'''
                                    Початок
                                        |
                            Дізнатись перше число (a)
                                        |
                            Дізнатись друге число (b)
                                        |
                    ----False------ b рівне 0? ------True----
                    |                                       |
            відповідь = a/b                     відповідь = "Помилка, на нуль ділити не можна!"
                    |_______________________________________|
                                        |
                                Друкувати відповідь           
'''

a = int(input("Введи перше число:"))
b = int(input("Введи друге число:"))
if b == 0:
answer = "Помилка, на нуль ділити не можна!"
else:
answer = a / b
print(answer)
