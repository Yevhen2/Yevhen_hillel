"""Create an array with strings that will consist of numbers,.

separated by a comma. For example:
[“1,2,3,4”, “1,2,3,4,50” “qwerty1,2,3”]

(create a new function for this).
If there are characters that are not numbers (“qwerty1,2,3” in the example),
you need to catch an exception and print “Can't do this!”
Use a try - except block to avoid other characters ,
other than numbers in the list.
For this example, the correct output would be 10, 60,
“Can't do it”
"""


elements = ['1,2,3,4', '1,2,3,4,50', 'qwerty1,2,3']


def sum_elements(x):
    """For each element of the list print the sum of all numbers."""
    for item in x:
        try:
            numbers = [int(num) for num in item.split(',')]
            total = sum(numbers)
            print(total)
        except ValueError:
            print("Can't do it!")


sum_elements(elements)
