'''
Програма повинна вивести площу прямокутного трикутника з заданими катетами. 
Чому вона повертає неправильне число? 
Знайдіть і виправте всі помилки.
'''


def area_tr(a, b):
    ans = a * b
    return ans
    ans = ans / 2
    ans = int(ans)


print(area_tr(4, 5))