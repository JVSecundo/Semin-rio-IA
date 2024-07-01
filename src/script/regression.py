# importando o módulo "numpy" com o nome "np", usado para operações numéricas eficientes em Python, para trabalhar com arrays multidimensionais

import numpy as np

# Importando a classe "LinearRegression" do módulo "sklearn.linear_model" para executar a regressão linear
# classe usada para realizar regressão linear, um método estatístico para modelar a relação entre variáveis dependentes e independentes.

from sklearn.linear_model import LinearRegression

# função run_regression define um exemplo de dados para realizar uma regressão linear, X é uma matriz NumPy com quatro linhas e duas colunas, 
# representando dados de entrada que é otráfego de rede, y é um array NumPy com os valores alvo, representando o consumo de energia correspondente 

def run_regression():

 # Dados de exemplo: consumo de energia (X) e tráfego de rede (y)

    X = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])  # exemplo de dados de entrada
    y = np.array([10, 20, 30, 40])  # Exemplo de consumo de energia

    # criando uma instância do modelo de regressão linear
    model = LinearRegression()

# Treinando o modelo de regressão linear com os dados de entrada e os valores alvo 
# ajusta o modelo aos dados, encontrando os coeficientes que minimizam o erro quadrático médio entre as previsões do modelo e os valores reais

    model.fit(X, y)

# Predizendo o consumo de energia para novos dados

    # usando o modelo treinado para fazer previsões sobre novos dados, que consistem em um array NumPy com uma linha e duas colunas
    new_data = np.array([[5, 6]])  

    #retorna as previsões do modelo para os novos dados, estimando o consumo de energia com base no tráfego de rede fornecido
    predicted_energy = model.predict(new_data)

# função retorna os dados de entrada X, os valores alvo y, os novos dados e as previsões feitas pelo modelo

    return X, y, new_data, predicted_energy

#teste
print("deu certooo, executando script de Regressão Linear")
