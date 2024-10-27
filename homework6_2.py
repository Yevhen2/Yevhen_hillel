"""loop that waits until user write a word with letter "h"."""

user_h = input('Enter a word with letter "h" in it: ')

while 'h' not in user_h.lower():
    user_h = input('Please make sure its a word with letter "h" in it: ')
