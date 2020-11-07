import tablib as tablib

data = tablib.Dataset(headers=['First Name', 'Last Name', 'Age'])
for i in [('Kenneth', 'Reitz', 22), ('Bessie', 'Monke', 21)]:
    data.append(i)

print(data.export("json"))
print(data.export("yaml"))

print(data.export('xlsx'))