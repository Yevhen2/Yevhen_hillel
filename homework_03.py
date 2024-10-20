
"""split the text into several lines."""

# task 01 == Розділіть змінну alice_in_wonderland так,
# щоб вона займала декілька фізичних лінії


alice_in_wonderland = (
    """Would you tell me, please, which way I ought to go from here?"\n
That depends a good deal on where you want to get to," said the Cat.\n
I don't much care where - " said Alice.\n
Then it doesn't matter which way you go," said the Cat.\n
— so long as I get somewhere," Alice added as an explanation.\n
Oh, you're sure to do that," said the Cat,
"if you only walk long enough.""")


# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
"""counting single quotes"""

single_count = alice_in_wonderland.count("'")
print(f'Single quotes in text-  {single_count}')

# task 03 == Виведіть змінну alice_in_wonderland на друк

"""print the text from alice_in_wonderland variable"""
print(alice_in_wonderland)


"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""

"""calculate total area of black and azov seas"""
s_black_sea = 436402
s_azov_sea = 37800

s_total = s_black_sea + s_azov_sea

print(f'the total area of the black sea and the azov '
      f'sea is {s_total} square kilometers.')

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
"""calculate and print the number of products in each warehouse"""
total_products = 375291

first_and_second_products = 250449

second_and_third_products = 222950

first_products = total_products - second_and_third_products

third_products = total_products - first_and_second_products

second_products = total_products - (first_products + third_products)

print(f'In the first warehouse {first_products}, '
      f'in the second - {second_products}, i'
      f'n the third - {third_products}')
# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
"""calculate the total cost of computer"""

monthly_payment = 1179

loan_time = 18

total_pc_cost = monthly_payment * loan_time

print(f'the total cost of the computer is: {total_pc_cost}')

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
"""calculate the remainder of division for given numbers"""

a = 8019 % 8

b = 9907 % 9

c = 2789 % 5

d = 7248 % 6

e = 7128 % 5

f = 19224 % 9

print(f'remainders are: a={a}, b={b}, c={c}, d={d}, e={e}, f={f}')

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""

"""calculate the total cost of irinka`s birthday order """

big_pizza_quantity = 4

big_pizza_price = 274

medium_pizza_quantity = 2

medium_pizza_price = 218

juice_quantity = 4

juice_price = 35

cake_quantity = 1

cake_price = 350

water_quantity = 3

water_price = 21

"""calculate total cost"""
big_pizza = big_pizza_quantity * big_pizza_price
medium_pizza = medium_pizza_quantity * medium_pizza_price
juice = juice_quantity * juice_price
cake = cake_quantity * cake_price
water = water_quantity * water_price

total_cost = big_pizza + medium_pizza + juice + cake + water

print(f'total cost for irinka`s order is: {total_cost} грн')


# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""

"""calculate the number of pages needed for ihor`s photos"""
total_photos = 232

page_size = 8

pages_count = total_photos // page_size

if total_photos % page_size != 0:
    pages_count += 1

print(f'ihor will need {pages_count} pages to glue all his photos.')

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""

"""calculate the amount of fuel needed for the trip"""

total_distance = 1600

liters_per_100_km = 9

fuel_capacity = 48

fuel_for_trip = total_distance * (liters_per_100_km / 100)

print(f'The family will need {fuel_for_trip} liters of fuel')

stop_count = fuel_for_trip // fuel_capacity

if fuel_for_trip // fuel_capacity != 0:
    stop_count += 1

print(f'The family needs to stop for fuel at least {int(stop_count)} times')
