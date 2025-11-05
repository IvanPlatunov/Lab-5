import re
import pandas as pd
#Task 1
f = open('task1-en.txt', errors='ignore').read()

r = r'[a-zA-Z]+,'
match = re.findall(r, f)
print(match)
print()

r2 = r'\[[^\[]+\]'
match2 = re.findall(r2, f)
print(match2)
print()

#Task 2
f2 = open('task2.html', errors='ignore').read()
r3 = r'#[0-9A-Fa-f]{6}'
match3 = re.findall(r3,f2)
print(match3)
print()

#Task 3
f4 = open('task3.txt', errors='ignore').read()
id = r' \d{1,3}\b'
surname = r'\b[A-Z][a-z]+\b'
email = r'[a-zA-Z0-9]+\@[a-zA-Z0-9-]+\.[a-z]{3}'
date = r'\d+\-\d+\-\d+'
site = r'(?:http|https)://(?:www\.|)[a-zA-Z-]+\.[a-z]+'

arr_id = re.findall(id,f4)
arr_sur = re.findall(surname, f4)
arr_em = re.findall(email,f4)
arr_date = re.findall(date,f4)
arr_site = re.findall(site, f4)

header = ['Id', 'Surname', 'Email', 'Date', 'Site']
table = []
for i in range(len(arr_id)):
    table.append((arr_id[i], arr_sur[i], arr_em[i], arr_date[i], arr_site[i]))
df = pd.DataFrame(table, columns=header)
df.to_csv('result.csv', index=False)

#Additional task
f5 = open('task_add.txt', errors='ignore').read()
email = r'[a-zA-Z0-9]+\@[a-zA-Z0-9-]+\.[a-z]{2,}'
date = r'(\d+\-\d+\-\d+)|(\d+\/\d+\/\d+)|(\d+\.\d+\.\d+)'
site = r'(?:http|https)://(?:www\.|)[a-zA-Z-]+\.[a-z]+'
match_e = re.findall(email, f5)
match_d = re.findall(date, f5)
for i in range(len(match_d)):
    for j in match_d[i]:
        if j != '':
            match_d[i] = j
match_s = re.findall(site, f5)
print('Email', match_e)
print('Date', match_d)
print('Site', match_s)