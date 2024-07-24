# Opening and reading a file, then closing it
file = open('my-text.txt')
data = file.read()
print(data)
file.close()

# Using 'with' statement to open, read, and automatically close the file
with open('my-text.txt') as file:
    data = file.read()
    print(data)

# Reading all lines from a file and printing each line split into words
with open('my-text.txt') as f:
    data = f.readlines()
    print(data)
    for i in data:
        word = i.split()
        print(word)

# Writing to a new file
with open('new_text.txt', 'w') as file:
    file.write('Usama Abid')

# Reading and printing the content of the newly written file
with open('new_text.txt') as file:
    data = file.read()
    print(data)

# Writing multiple lines to the file, overwriting existing content
with open('new_text.txt', 'w') as file:
    file.write('Usama Abid\n')
    file.write('Data Scientist\n')
    file.write('Cyber Security Specialist\n')
    file.write('Devops Evangelist\n')

# Reading and printing the updated content of the file
with open('new_text.txt') as file:
    data = file.read()
    print(data)

# Appending a line to the existing content of the file
with open('new_text.txt', 'a') as file:
    file.write('Journey with Alnafi')

# Reading and printing the content of the file after appending
with open('new_text.txt') as file:
    data = file.read()
    print(data)

# Appending a line to another file and reading its content
with open('new_text_data.txt', 'a') as file:
    file.write('Journey with Alnafi')

with open('new_text_data.txt') as file:
    data = file.read()
    print(data)

# Writing a list of strings to a file, each on a new line
my_data = ['Python', 'Python 2', 'Python 3']
with open('mydatafile.txt', 'a') as file:
    for i in my_data:
        file.write(i + '\n')

with open('mydatafile.txt') as file:
    data = file.read()
    print(data)

# Writing multiple lines to a file using a loop
for i in range(11):
    with open('sam_text.txt', 'a') as file:
        file.write(f'This is line: {i} \n')

with open('sam_text.txt') as file:
    print(file.read())

# Working with JSON data
import json

# Reading JSON data and printing specific key-value pairs
with open('my_json.json', 'r') as jf:
    my_data = json.load(jf)
    for i in my_data:
        if i == 'password_apache':
            print(f'The username is Usama and server is apache with a password: {my_data[i]}')

# Reading JSON data and printing each dictionary key-value pair
with open('my_json1.json', 'r') as jf:
    my_data1 = json.load(jf)
    for i in my_data1:
        for k, v in i.items():
            print(k + ": " + str(v))

# Filtering and printing JSON data based on a specific value
with open('my_json1.json', 'r') as jf:
    my_data1 = json.load(jf)
    for i in my_data1:
        print('The dictionary is :', i)
        for k, v in i.items():
            if v == 'CentOS':
                print(f'The operating system is {v}')

# Creating and writing a JSON object to a file
my_dict = [
  {
    "Name": "CentOS",
    "Version": "7",
    "Install": "yum",
    "Owner": "Redhat",
    "Kernel": "3.10"
  },
  {
    "Name": "Ubuntu",
    "Version": "17.10",
    "Install": "apt",
    "Owner": "Canonical",
    "Kernel": "4.13"
  }
]

my_path = 'new_json_file.json'
with open(my_path, 'w') as jf:
    json.dump(my_dict, jf, indent=3)

# Processing JSON data based on a condition
with open('json_test.json') as jf:
    data = json.load(jf)
    total_fruits = 0
    fruit_names = ' '
    for i in data:
        if i['price'] > 1:
            print(len(i.keys()))

# Reading and processing a CSV file
my_path = r'C:\Users\06331913026.stuqau\PycharmProjects\PythonWithAlNafi\servershealth-220925-204801.csv'

with open(my_path, 'r') as file:
    data = file.read()
    print(data)

# Reading and splitting CSV file content by lines
with open(my_path, 'r') as file:
    data = file.readlines()
    for i in data:
        print(i.split())

# Reading CSV file using csv.reader
import csv
with open(my_path) as file:
    data = csv.reader(file)
    for row in data:
        print(row)

# Reading CSV file into a list
with open(my_path) as file:
    data = csv.reader(file, delimiter=',')
    data = list(data)
    print(data)

# Writing a single row to a CSV file
new_row = ['9', '10.226.17.103', 'RHEL', 'd6:60:7b:6e:f6:8c', '14 GB']
with open(my_path, 'w') as file:
    data_writer = csv.writer(file)
    data_writer.writerow(new_row)

with open(my_path) as file:
    data = csv.reader(file, delimiter=',')
    data = list(data)
    print(data)

# Writing multiple rows to a CSV file
new_row1 = ['1', '10.226.17.103', 'RHEL1', 'd6:60:7b:6e:f6:8c1', '14 GB2']
new_row2 = ['2', '10.226.17.104', 'RHEL2', 'd6:60:7b:6e:f6:8c2', '14 GB1']

import csv
with open('new_csv.csv', 'w') as file:
    data_write = csv.writer(file)
    data_write.writerow(new_row1)
    data_write.writerow(new_row2)

with open('new_csv.csv') as file:
    data = csv.reader(file, delimiter=',')
    data = list(data)
    print(data)

# Writing multiple rows to a CSV file using writerows
new_rows = [new_row1, new_row2]
with open('new_csv.csv', 'w', newline='') as file:
    data_write = csv.writer(file)
    data_write.writerows(new_rows)

with open('new_csv.csv') as file:
    data = csv.reader(file, delimiter=',')
    data = list(data)
    print(data)

# Filtering rows from a CSV file and writing to a new file
file_path = r'C:\Users\06331913026.stuqau\PycharmProjects\PythonWithAlNafi\servershealth-220930-214947.csv'

data = []
with open(file_path) as file:
    data_read = csv.reader(file)
    header = next(data_read)
    print(header)

    for row in data_read:
        if row[2] == 'RHEL':
            data.append(row)

with open('new_csvFile.csv', 'w', newline='') as file:
    data_write = csv.writer(file)
    data_write.writerows(data)

# Writing header and filtered data to a new CSV file
with open('new_csvFile.csv', 'w', newline='') as file:
    data_write = csv.writer(file)
    data_write.writerow(header)
    data_write.writerows(data)