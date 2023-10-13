import matplotlib.pyplot as plt
import os 



# Crescimento da população brasileira 1980 - 2016

# Encontrando o diretório do arquivo e abrindo o mesmo
dir_path = os.path.dirname(os.path.realpath(__file__))
dados = open(dir_path + '/' + 'populacao_brasileira.csv').readlines()

# Definição dos eixos

years = []
population = []

# Definição do título e legendas
title = 'Crescimento Populacional do Brasil (1980-2016)'
subtitle_years = 'Anos'
subtitle_population = 'População x100.000.000'
plt.title(title)
plt.xlabel(subtitle_years)
plt.ylabel(subtitle_population)

# Adicionando valores nas listas criadas
for i in range(len(dados)):
    if i != 0:
        line = dados[i].split(';')
        years.append(int(line[0]))
        population.append(int(line[1]))

# Plotando e mostrando o gráfico
plt.bar(years,population, color='#e4e4e4')
plt.plot(years,population, color='k', linestyle='--')
plt.show()