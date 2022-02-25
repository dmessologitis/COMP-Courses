import random
import string

def random_letters(y):
    return ''.join(random.choice(string.ascii_lowercase) for x in range(y))

random_string = random_letters(10)

random_list = list(random_string)

print('Random Letters\n', random_list)

random_list.sort() #sort ascending

print('Sort the list in ascending order.\n', random_list)

random_list.sort(reverse=True) #sort descending

print('Sort the list in descending order.\n', random_list)

unique_random_list = list(set(random_list)) #get unique values by converting to set and back to list because sets cannot be sorted.

unique_random_list.sort()

print('Unique values sorted in as ascending order\n', unique_random_list)

