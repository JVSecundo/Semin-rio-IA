# Seminário Inteligência Artificial na Gestão de Serviços de Redes de Computadores

## Implementação Prática
Instalação do Ambiente de Desenvolvimento
Instale a extensão Python para VS Code para facilitar o desenvolvimento: procure por "Python" na seção de extensões do VS Code e instale a extensão fornecida pela Microsoft.

## Instalando Dependências
Se você não tiver as bibliotecas necessárias, como numpy e scikit-learn para a Regressão Linear, instale-as usando o pip no terminal do VS Code:

**pip install numpy scikit-learn**

## Configuração do Ambiente Virtual (opcional)
É recomendável criar um ambiente virtual para o projeto usando virtualenv ou conda para manter as dependências do projeto isoladas. Isso pode ser feito pelo terminal do VS Code:

## Crie um ambiente virtual usando virtualenv

**python -m venv venv**

## Ative o ambiente virtual no Windows

**.\venv\Scripts\activate**

## Ative o ambiente virtual no macOS/Linux

**source venv/bin/activate**

## Instalando Dependências do Projeto (caso não houver)
Com o ambiente virtual ativado, instale as bibliotecas necessárias listadas no arquivo requirements.txt:

**pip install -r requirements.txt**

## Executando os Scripts
Agora você pode executar os scripts individualmente no VS Code. Certifique-se de estar no diretório correto (“src” e dentro da pasta “script”) ao executar esses comandos:

**python regression.py**

**python genetic_algorithm.py**

**python plot_results.py**

## Verificando a Saída

Cada script produzirá saídas diferentes:

**regression.py** pode imprimir o consumo de energia previsto para novos dados.

**genetic_algorithm.py** pode imprimir a configuração ótima encontrada pelo algoritmo genético.

**plot_results.py** deve exibir um gráfico mostrando a redução no consumo de energia antes e depois da implementação dos algoritmos.

## Verificando os Gráficos

Ao executar **plot_results.py**, ele deve exibir um gráfico de barras usando matplotlib mostrando a comparação antes e depois da otimização de energia.

## Observações Adicionais

Certifique-se de que todos os caminhos de arquivo e importações estão corretos nos seus scripts.
Verifique se você está utilizando a versão correta do Python no seu ambiente virtual (se estiver usando um).

Caso encontre erros ou problemas durante a execução, verifique a saída no terminal do VS Code para mensagens de erro detalhadas.

**Seguindo esses passos, você poderá executar e verificar os resultados dos seus scripts de forma eficiente no ambiente do Visual Studio Code.**




