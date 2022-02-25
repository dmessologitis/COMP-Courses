with open('file.txt', 'w') as myfile:
    myfile.write('This is a test file\nHello Student\nTesting 1,2,3 - testing !\nPython rocks !')

count = 0
with open('file.txt') as file:
    for line in file:
        count += 1

    scount = str(count)

    with open('file.txt', 'a') as fileUpdated:
        fileUpdated.write('\n'
                          'There are ' + scount + ' lines in this file.')

print(count)