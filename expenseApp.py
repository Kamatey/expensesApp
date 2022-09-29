from datetime import date
import csv

dt = date.today()
dt = dt.strftime("%d/%m/%y")
filename = "test1.csv"
exp = []
stopped = False

with open(filename, 'w') as file:
    csvwriter = csv.writer(file)
    while not stopped:
        xp = int(input("what is the expense(type 0 to stop): "))
        if xp ==0:
            stopped = True
        else:
            csvwriter.writerow([dt, xp])
            exp.append(xp)
file.close()
print('your expenses today are, ', exp)
print("your total is", sum(exp))