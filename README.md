# Análise de Dados de Energia Sustentável com Modelo Gamma

## Descrição do Projeto

Este repositório apresenta a aplicação de um modelo estatístico para análise de dados globais relacionados à energia sustentável. O estudo foi desenvolvido a partir de um conjunto de dados público, com o objetivo de explorar padrões, identificar relações entre variáveis e ajustar um modelo capaz de descrever adequadamente o comportamento da variável de interesse.

A implementação completa da análise está disponível no notebook:
👉 [https://github.com/Fabiano01EST/generalized-linear-models/blob/main/Gamma_model.ipynb](https://github.com/Fabiano01EST/generalized-linear-models/blob/main/Gamma_model.ipynb)

## Base de Dados

Os dados utilizados são provenientes do seguinte repositório:
👉 [https://www.kaggle.com/datasets/anshtanwar/global-data-on-sustainable-energy](https://www.kaggle.com/datasets/anshtanwar/global-data-on-sustainable-energy)

O conjunto de dados reúne informações de diversos países ao longo dos anos, contemplando indicadores associados ao contexto energético e ambiental. Entre as variáveis disponíveis, destacam-se medidas relacionadas ao consumo de energia, emissões, acesso à eletricidade e uso de fontes renováveis.

## Estrutura da Análise

A análise foi conduzida de forma sequencial, contemplando as seguintes etapas:

### 1. Preparação dos Dados

Inicialmente, foi realizada a organização da base, incluindo:

* Tratamento de valores ausentes;
* Ajuste de tipos das variáveis;
* Padronização de formatos para viabilizar a modelagem.

### 2. Análise Exploratória

Na etapa exploratória, foram utilizadas medidas descritivas e visualizações gráficas para compreender o comportamento das variáveis.

Adicionalmente, foi construída uma matriz de correlação de Spearman, com o objetivo de identificar associações entre os preditores e a variável resposta. Essa matriz tem como principal característica **descrever as relações observadas nos dados**, permitindo evidenciar padrões relevantes e auxiliar na escolha das variáveis utilizadas no modelo.

### 3. Modelagem

A modelagem foi realizada utilizando um modelo Gamma, considerando a natureza da variável resposta. Foram selecionadas variáveis explicativas com base nos padrões identificados na análise exploratória.

O ajuste do modelo foi conduzido diretamente sobre a base tratada, buscando representar de forma adequada a relação entre a variável de interesse e os fatores explicativos.

### 4. Avaliação

Após o ajuste, foram analisados:

* Os coeficientes estimados;
* O comportamento dos resíduos;
* A consistência geral do modelo em relação aos dados observados.

Essa etapa permitiu verificar a qualidade do ajuste e a adequação da especificação adotada.

## Organização do Repositório

* `Gamma_model.ipynb`: contém toda a implementação da análise, desde o tratamento dos dados até a modelagem e avaliação dos resultados.

## Considerações

Este projeto tem caráter aplicado, com foco na exploração e modelagem de dados reais. A abordagem adotada permite identificar padrões relevantes no contexto da energia sustentável e fornece uma base estruturada para análises futuras com dados de natureza semelhante.

---
