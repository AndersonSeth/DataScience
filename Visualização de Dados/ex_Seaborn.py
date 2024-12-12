import seaborn as sns
import matplotlib.pyplot as plt

# Configuração de estilo para gráficos mais bonitos
sns.set_theme(style="darkgrid")

# Dados de exemplo
import pandas as pd
import numpy as np

# Criando um DataFrame de exemplo
df = pd.DataFrame({
    'x': np.random.rand(50),
    'y': np.random.rand(50),
    'categoria': np.random.choice(['A', 'B', 'C'], size=50)
})

# Criar o gráfico de dispersão
sns.scatterplot(x='x', y='y', hue='categoria', data=df, palette='deep')

# Exibir o gráfico
plt.title('Gráfico de Dispersão com Seaborn')
plt.show()
