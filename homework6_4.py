"""find a sum of all even numbers."""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

sum_num = 0

for num in numbers:
    if num % 2 == 0:
        sum_num += num

print(sum_num)
