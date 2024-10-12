# task 01 == Виправте синтаксичні помилки.
"""Syntax errors are edited."""
print('Hello', end=' ')
print('world!')

# task 02 == Виправте синтаксичні помилки
"""Syntax errors are edited."""
hello = 'Hello'
world = 'world'
if True:
    print(f'{hello} {world}!')

# task 03  == Вcтавте пропущену змінну у ф-цію print
"""Missing variable is pasted."""
for letter in 'Hello world!':
    print(letter)

# task 04 == Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук
"""# of bananas is 4 time bigger than # of apples."""
apples = 2
banana = apples * 4

# task 05 == виправте назви змінних
"""Variables are changed."""
storona_1 = 1
storona_2 = 2
storona_3 = 3
storona_4 = 4

# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача
"""Perimetr is calculating."""
perimetery = storona_1 + storona_2 + storona_3 + storona_4
print(perimetery)


"""
    # Задачі 07 -10.:
    # Переведіть задачі з книги "Математика, 2 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в другому класі
"""
# task 07
"""
У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
Скільки всього дерев посадили в саду?
"""
"""There are 4 apples, 9 pears and 2 plums. Then we count all trees"""
apples = 4

pears = apples + 5

plums = apples - 2

total = apples + pears + plums

print(f'Усього дерев в саду: 4 + 9 + 2 = {total}')


# task 08
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""
"""There was +5 degrees celcius at morning, then temperature droped by 10 degrees
and then raised by 4"""
temperature_morning = 5
temperature_afternoon = temperature_morning - 10
temperature_evening = temperature_afternoon + 4
print(f'Температура надвечір: 5 - 10 + 4 = {temperature_evening}')

# task 09
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""
"""There are 24 boys and 12 girls. 1 boy and 2 girls getiing sick. How many kids
are there?"""

total_boys = 24
total_girls = total_boys / 2
total_boys_today = total_boys - 1
total_girls_today = total_girls - 2
total_kids_today = total_boys_today + total_girls_today
print(f'Сьогодні в гуртку: всього хлопчиків 24 - 1 = {total_boys_today}. Всього дівчаток 12 - 2 = {total_girls_today}.'
      f'Всього дітей: {total_kids_today}')


# task 10
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""
"""First book costs 8, second one cost 2 more, third one - half of 1 and 2 together.
What is total cost of these 3 books?"""
first_book = 8
second_book = first_book + 2
third_book = (first_book / 2) + (second_book / 2)
total_cost = first_book + second_book + third_book
print(f'Усі книжки разом будуть коштувати: 8 + 10 + (8 + 10 / 2) = {total_cost}')
