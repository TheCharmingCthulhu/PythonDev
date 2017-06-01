import csv, os

if not os.path.exists(os.getcwd() + "\\input\\"):
    os.mkdir(os.getcwd() + "\\input\\")

if not os.path.exists(os.getcwd() + "\\output\\"):
    os.mkdir(os.getcwd() + "\\output\\")

rows = []

def HasDuplicate(item):
    for row in rows:
        if row == item:
            return True

    return False

for root, dirs, files in os.walk(os.getcwd() + "\\input"):
    for f in files:
        with open(os.getcwd() + "\\input\\" + f, 'rb') as fl:
            reader = csv.reader(fl, delimiter=';')
            for row in reader:
                if not HasDuplicate(row):
                    rows.append(row)
    with open(os.getcwd() + "\\output\\output.csv", "wb") as fl:
        writer = csv.writer(fl, delimiter=";")
        for row in rows:
            writer.writerow(row)
                
