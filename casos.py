import numpy as np
import matplotlib.pyplot as plt
i=0

cases=[[],[]]
deaths=[[],[]]
suspects=[[],[]]
discarded=[[],[]]
cod_day=[[],[]]
date=[[],[]]

color = ['k-', 'r-']
data_Ma = open('Pa.dat', 'r')
data_Pa = open('Ma.dat', 'r')

estados = [ data_Ma, data_Pa ]

plt.axis([0,29,0,1000])
#x = np.linspace(1, len(cases), len(cases))

for i in range(0,2,1): 
        for line in estados[i]:
            if line.strip() != '' and '#' not in line.strip():
                cases[i].append(float(line.split()[0]))
                cod_day[i].append(float(line.split()[4]))
                deaths[i].append(float(line.split()[1]))
                date[i].append(line.split()[5])


arrayx = np.arange(cod_day[1][0], cod_day[1][len(cod_day[1]) -1 ] + 3)
arrayy = np.arange(0,1000,100)
plt.xticks(arrayx,[str(a) for a in date[1]],rotation=45)
plt.yticks(arrayy,[str(b) for b in arrayy])

##axis properties and generator
plt.xlabel('dias de contagio', fontsize=16)
plt.ylabel('casos confirmados de COVID-19', fontsize=16)

plt.plot(cod_day[0], cases[0],'b-', label = 'Pará')
plt.scatter(cod_day[0],cases[0],color ='red')

plt.plot(cod_day[1], cases[1],'k-', label = 'Maranhão')
plt.scatter(cod_day[1],cases[1],color='red')

plt.legend(bbox_to_anchor=(0.112, 1), loc='upper right', borderaxespad=0.)


plt.grid()
plt.show()
