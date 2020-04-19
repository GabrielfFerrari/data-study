import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv('ma.csv')


plt.plot(dados['Data'],dados['Casos'], 'k-', label='maranhão')
plt.scatter(dados['Data'],dados['Casos'], color='red')

plt.xticks(dados['Data'],[ str(a) for a in dados['Data'] ],rotation=45, fontsize = 10)

plt.xlabel('dias de contagio', fontsize=16)
plt.ylabel('casos confirmados de COVID-19', fontsize=16)
plt.legend(bbox_to_anchor=(1.1, 1), loc='upper right', borderaxespad=0.)
plt.grid()
plt.show()


