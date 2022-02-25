with open('inputFile.txt', 'w') as inputFile:
    inputFile.write((input("Enter text into the file: ")))

with open('inputFile.txt') as inputFile:
    contents = inputFile.readlines()
    c = contents[0]
    contentsList = c.split()

    count = 0
    for i in contentsList:
        if len(i) == 5:
            count += 1

    scount = str(count)

    with open('inputFile.txt', 'a') as inputFileUpdated:
        inputFileUpdated.write('\nThere are ' + scount + ' five-letter words in this file.')

print(count)

# There is text in this input file