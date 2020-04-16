import matplotlib.pyplot as plt
import math

def DOS_PLOTY():
    x=list()
    y=list()
    data=list()
    DOS=open('casos_ma.py','r')
    for line in DOS:
        x.append(float(line.split()[0]))
        y.append(float(line.split()[1]))

    plt.xlabel('E/eV', fontsize=16)
    plt.ylabel('DOS*eV', fontsize=16)

    plt.axis([-10, 10, 0, 300])
    plt.plot(x,y,'k-',linewidth=0.5) # plot
    plt.axvline(x=0, ymin=0, ymax=1000,color='c', linestyle='--')
    plt.savefig('dos_-10_10.png', format='png')
    plt.show()


data = open('Ma.dat', 'r')
for line in data:




