#Exercicio de Estatísticas - Prof Edson Riberio Youtube

#Calcule a média, a mediana, a moda, a variancia e o desvio padrão dos numeros abaixo:

#Amostragem 
numeros = [9,7,10,5,9,7,9,8]

# soma= sum(numeros)
# print(soma)

#Organizando a lista em ordem crescente por conta da mediana (ROL) com função Sort 
# numeros.sort()
# print(numeros)

numeros_ordenados = sorted(numeros)
# print(f'Lista ordenada(sorted): {numeros_ordenados}')

#Para resolver os exercicios utilizei a biblioteca nativa do Python Statistics
from statistics import mode, median, mean, variance, pstdev
#média
media= mean(numeros_ordenados)
print(media)

#Moda
moda = mode(numeros_ordenados)
print(moda)

#Mediana
mediana = median(numeros)
print(mediana)

#Variancia
variancia = variance(numeros_ordenados)
print(variancia)

#Desvio padrão 
desvio_padrao = pstdev(numeros_ordenados)
print(desvio_padrao)

