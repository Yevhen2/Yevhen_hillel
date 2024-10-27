"""homework 6.1."""

user_info = input('Введіть данні: ')

user_set = set(user_info)

len_ten = len(user_set) > 10


print(f' Унікальних символів більше 10: {len_ten}')
