""".

Задача: надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити або доповнити.

"""


def multiplication_table(number):
    """task1."""
    # Initialize the appropriate variable
    multiplier = 1
    # Complete the while loop condition.
    while True:
        result = number * multiplier
        # десь тут помила, а може не одна
        if result > 25:
            # Enter the action to take if the result is greater than 25
            break
        print(str(number) + 'x' + str(multiplier) + '=' + str(result))

        # Increment the appropriate variable
        multiplier += 1


multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15

iii = '-'

print(iii * 20)

# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""


def sumoftwo(a, b):
    """Find sum of 2 number."""
    return a + b


# task 3


"""Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""

numlists = [1, 2, 3, 4, 5, 6]


def avar_num(numlists):
    """Task 3."""
    return sum(numlists) / len(numlists)


# task 4


"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""


def rev_str(a):
    """Reverse of the string."""
    return a[::-1]


# task 5


"""Написати функцію, яка приймає список слів та повертає найдовше
слово у списку.
"""
b = ['hello', 'world', 'hellooooo']


def long_word(b):
    """Longest word from list."""
    return max(b, key=len)


# task 6


"""  Написати функцію, яка приймає два рядки та повертає
 індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого
 рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""


def find_substring(str1, str2):
    """task6."""
    return -1


str1 = 'Hello, world!'
str2 = 'world'

print(find_substring(str1, str2))  # поверне 7

str1 = 'The quick brown fox jumps over the lazy dog'
str2 = 'cat'
print(find_substring(str1, str2))  # поверне -1

"""Answer to task 6."""


def find_str(str1, str2):
    """Str2 in str1, or -1 if not found."""
    return str1.find(str2)


print(find_str('Hello, world!', 'world'))
print(find_str('The quick brown fox jumps over the lazy dog', 'cat'))

"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""


# task 7


def calculate_total_area():
    """Calculate the total area of Black and Azov Seas."""
    s_black_sea = 436402
    s_azov_sea = 37800
    s_total = s_black_sea + s_azov_sea
    return {s_total}


# task 8


def products():
    """Calculate the number of products in each warehouse."""
    total_products = 375291
    first_and_second_products = 250449
    second_and_third_products = 222950

    first_products = total_products - second_and_third_products
    third_products = total_products - first_and_second_products
    second_products = total_products - (first_products + third_products)

    return (f'In the first: {first_products}, '
            f'in the second: {second_products}, '
            f'in the third: {third_products}')


# task 9


def total_pc_costs():
    """Calculate the total cost of a computer."""
    monthly_payment = 1179
    loan_time = 18  # months
    total_pc_cost = monthly_payment * loan_time
    return f'total cost of the computer is: {total_pc_cost} '


# task 10


def calculate_some():
    """Calculate the remainder of division for given numbers."""
    a = 8019 % 8
    b = 9907 % 9
    c = 2789 % 5
    d = 7248 % 6
    e = 7128 % 5
    f = 19224 % 9

    return f'Remainders are: a={a}, b={b}, c={c}, d={d}, e={e}, f={f}'
