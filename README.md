Análise de Acidentes de Trânsito com KNN
Descrição do Projeto

Este repositório apresenta a aplicação do algoritmo K-Nearest Neighbors (KNN) para análise de dados de acidentes de trânsito. O estudo foi desenvolvido com o objetivo de explorar padrões nos dados, identificar relações entre variáveis e realizar a classificação da gravidade dos acidentes a partir das características observadas.

A implementação completa da análise está disponível no notebook:
👉 https://github.com/Fabiano01EST/KNN-aplication/blob/main/GLM2.ipynb

Base de Dados

Os dados utilizados correspondem a registros de acidentes de trânsito, contendo informações sobre características dos envolvidos, condições do acidente e variáveis associadas à severidade.

O conjunto de dados reúne variáveis como idade, sexo, tipo de envolvido, tipo de acidente e outras características relevantes, permitindo analisar fatores associados à classificação dos acidentes.

Estrutura da Análise

A análise foi conduzida de forma sequencial, contemplando as seguintes etapas:

1. Preparação dos Dados

Inicialmente, foi realizada a organização da base, incluindo:

Tratamento de valores ausentes;

Ajuste de tipos das variáveis;

Codificação de variáveis categóricas;

Padronização dos dados para aplicação do modelo.

2. Análise Exploratória

Na etapa exploratória, foram utilizadas medidas descritivas e visualizações gráficas com o objetivo de compreender o comportamento das variáveis e a distribuição das classes.

Essa etapa permitiu identificar possíveis padrões e desequilíbrios entre categorias, contribuindo para uma melhor compreensão do problema de classificação.

3. Modelagem

A modelagem foi realizada utilizando o algoritmo KNN, que classifica as observações com base na similaridade entre os dados. O modelo foi ajustado a partir de um conjunto de treinamento, utilizando variáveis selecionadas na etapa exploratória.

Adicionalmente, foi realizada a escolha do parâmetro 
𝑘
k, responsável por definir o número de vizinhos considerados na classificação, buscando melhorar o desempenho do modelo.

4. Avaliação

Após o ajuste do modelo, foram analisados:

A matriz de confusão;

Métricas de desempenho, como acurácia;

O comportamento das classificações realizadas pelo modelo.

Essa etapa permitiu avaliar a capacidade preditiva do modelo e identificar possíveis limitações na classificação.

Organização do Repositório

GLM2.ipynb: contém toda a implementação da análise, incluindo preparação dos dados, modelagem e avaliação dos resultados.

Considerações

Este projeto possui caráter aplicado, com foco na utilização de técnicas de aprendizado de máquina para análise de dados reais. A abordagem adotada permite identificar padrões relevantes em acidentes de trânsito e fornece uma base estruturada para aplicações futuras em problemas de classificação.
