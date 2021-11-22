import matplotlib.pyplot as plt
import csv

x = []
t = []
p = []

with open('koeleskab.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        t.append(int(row[1]))
        p.append(int(row[2]))

plt.plot(x,t, label='Loaded from file!')
plt.xlabel('tid')
plt.ylabel('temperatur')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()
