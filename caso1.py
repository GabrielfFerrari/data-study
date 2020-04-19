import numpy as np
import matplotlib.pyplot as plt

#estado = ['AC','AL','AP','AM','BA','CE','DF','ES','GO','MA','MT','MS','MG','PA','PB','PR','PE','PI','RJ','RN','RS','RO','RR','SC','SP','SE','TO'] #
# for brasil

estado = ['MA']
date        = []
obitosNovos = []
obitosAcumulados = []
casosNovos  = []
casosAcumulados  = []
    
limit=len(estado)

for i in range(0,limit):
    arquivo = open('dados.csv','r')
    date.append([])
    casosNovos.append([])
    casosAcumulados.append([])
    obitosNovos.append([])
    obitosAcumulados.append([])
    for line in arquivo:
        if line.strip() !='' and '#' not in line.strip() and estado[i] in line.strip():
            date[i].append(line.split(';')[1])
            casosNovos[i].append(float(line.split(';')[2]))
            casosAcumulados[i].append(float(line.split(';')[3]))
            obitosNovos[i].append(float(line.split(';')[4]))
            obitosAcumulados[i].append(float(line.split(';')[5]))
    arquivo.close()


plt.axis([0,len(date[0]) + 2,0,2000])
x = np.arange(0, len(date[0]))
plt.xticks(x,[str(a) for a in date[0]],rotation=65, fontsize = 8)

for k in range(0,limit,1):
    plt.plot(x, casosAcumulados[k],label = estado[k])
    plt.scatter(x, casosAcumulados[k],color = 'r')

plt.xlabel('dias de contagio', fontsize=16)
plt.ylabel('casos confirmados de COVID-19', fontsize=16)
plt.legend(bbox_to_anchor=(1.1, 1), loc='upper right', borderaxespad=0.)
plt.grid()
plt.show()
