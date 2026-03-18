# Análise de Acidentes de Trânsito com Regressão Logística

## Descrição do Projeto

Este repositório apresenta a aplicação do modelo de Regressão Logística para análise de dados de acidentes de trânsito. O estudo foi desenvolvido com o objetivo de explorar padrões nos dados, identificar relações entre variáveis e realizar a classificação da gravidade dos acidentes a partir das características observadas.

A implementação completa da análise está disponível no notebook:
👉 [https://github.com/Fabiano01EST/generalized-linear-models/blob/main/logistic_model.ipynb](https://github.com/Fabiano01EST/generalized-linear-models/blob/main/GLM2.ipynb)

---

## Base de Dados

Os dados utilizados correspondem a registros de acidentes de trânsito, contendo informações sobre características dos envolvidos, condições do acidente e variáveis associadas à severidade.

O conjunto de dados reúne variáveis como idade, sexo, tipo de envolvido, tipo de acidente e outras características relevantes, permitindo analisar fatores associados à classificação dos acidentes.

---

## Estrutura da Análise

A análise foi conduzida de forma sequencial, contemplando as seguintes etapas:

### 1. Preparação dos Dados

Inicialmente, foi realizada a organização da base, incluindo:

* Tratamento de valores ausentes;
* Ajuste de tipos das variáveis;
* Codificação de variáveis categóricas;
* Padronização dos dados para aplicação do modelo.

### 2. Análise Exploratória

Na etapa exploratória, foram utilizadas medidas descritivas e visualizações gráficas com o objetivo de compreender o comportamento das variáveis e a distribuição das classes.

Essa etapa permitiu identificar possíveis padrões e desequilíbrios entre categorias, contribuindo para uma melhor compreensão do problema de classificação.

### 3. Modelagem

A modelagem foi realizada utilizando o modelo de Regressão Logística, apropriado para problemas de classificação. O modelo foi ajustado a partir de um conjunto de treinamento, considerando variáveis explicativas selecionadas com base na análise exploratória.

O ajuste foi conduzido buscando representar adequadamente a relação entre as características observadas e a probabilidade de ocorrência das classes da variável resposta.

### 4. Avaliação

Após o ajuste do modelo, foram analisados:

* A matriz de confusão;
* Métricas de desempenho, como acurácia;
* O comportamento das probabilidades estimadas.

Essa etapa permitiu avaliar a capacidade preditiva do modelo e verificar a consistência das classificações realizadas.

---

## Organização do Repositório

* `GLM2.ipynb`: contém toda a implementação da análise, incluindo preparação dos dados, modelagem e avaliação dos resultados.

---

## Considerações

Este projeto possui caráter aplicado, com foco na utilização de métodos estatísticos para análise de dados reais. A abordagem adotada permite identificar fatores associados à gravidade dos acidentes de trânsito e fornece uma base estruturada para aplicações futuras em problemas de classificação.

---
