#usado para criar visualizações gráficas em Python

import matplotlib.pyplot as plt

from regression import run_regression # executa uma regressão linear.
from genetic_algorithm import run_genetic_algorithm  # executa um algoritmo genético

# Executar a regressão linear, as funções importadas

X, y, new_data, predicted_energy = run_regression()

# retorna a melhor solução encontrada pelo algoritmo genético
best_solution = run_genetic_algorithm()

# Dados de exemplo para plotagem
antes = [100, 90, 95, 105]  # Consumo de energia antes da implementação

depois = [80, 70, 75, 85]  # Consumo de energia depois da implementação 

#número de testes realizados
numeros_teste = range(len(antes))

# Criar um gráfico de barras
plt.bar(numeros_teste, antes, color='b', alpha=0.5, label='Antes')
plt.bar(numeros_teste, depois, color='r', alpha=0.5, label='Depois')

# Adicionar rótulos e título
plt.xlabel('Teste')
plt.ylabel('Consumo de Energia (Watts)')
plt.title('Redução no Consumo de Energia')
plt.xticks(numeros_teste, ['Teste 1', 'Teste 2', 'Teste 3', 'Teste 4'])
plt.legend()

# Mostrar gráfico
plt.tight_layout()
plt.show()
