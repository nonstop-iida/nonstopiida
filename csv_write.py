import os

path = "../test/test.csv"

file_exist = os.path.isfile(path)

if file_exist:
    with open (path, "a", encoding='shift-jis') as f:
        f.write("追記" + "\n")
        
else:
    with open(path, "w", encoding="shift-jis") as f:
        f.write("新規" + "\n")
