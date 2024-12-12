import matplotlib.pyplot as plt

# Dados para o gráfico
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Criar o gráfico de linha
plt.plot(x, y, label='Números primos', color='blue', linestyle='--', marker='o')

# Personalização do gráfico
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.title('Exemplo de Gráfico de Linha com Matplotlib')
plt.legend()

# Exibir o gráfico
plt.show()