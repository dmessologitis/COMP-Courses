import os

# 5.	Create a file called accounts.txt and enter the following information in the file
entry = ['100 Mary 34.58', '200 Alison 345.67', '300 Marc 3.00', '400 Zoltar -32.16', '500 Kathleen 24.32']

with open('accounts.txt', 'w') as accounts:
    for a in entry:
        accounts.write(a + '\n')

# 6.a.	update the name 'Zoltar' to 'Robert'
old = "Zoltar"
new = "Robert"

with open('accounts.txt', 'r') as file:
    data = file.read()
    data = data.replace(old, new)

with open('accounts.txt', 'w') as file:
    file.write(data)

try:
    os.remove('myaccounts.txt')
except:
    pass

# 6.b. create a tempfile with the new data
with open('tempfile.txt', 'w') as tempfile:
    with open('accounts.txt') as accounts:
        lines = accounts.readlines()

        for i in lines:
            tempfile.write(i)

with open('tempfile.txt') as temp:
    tf = temp.readlines()

# print(tf)

# 6.c. remove accounts.txt file from the directory
os.remove('accounts.txt')

# 6.d. rename the tempfile to a new file called myaccounts.txt
os.rename('tempfile.txt', 'myaccounts.txt')

