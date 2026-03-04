
---


# Modelo de Regressão Gama aplicado a Dados Globais de Energia Sustentável

## 🔎 Visão Geral

Este projeto apresenta a aplicação de um **Modelo Linear Generalizado (MLG) com distribuição Gamma** utilizando o conjunto de dados *Global Data on Sustainable Energy (2000–2020)*, disponível na plataforma Kaggle.

O objetivo central é modelar uma variável energética contínua e estritamente positiva com base em indicadores econômicos e energéticos de aproximadamente 175 países ao longo de 20 anos.

O projeto enfatiza boas práticas em:

* Limpeza e preparação de dados
* Análise Exploratória de Dados (EDA)
* Modelagem estatística aplicada
* Diagnóstico e avaliação de modelos
* Interpretação técnica de resultados

---

## 🎯 Objetivo

Aplicar regressão Gamma para:

* Modelar uma variável contínua relacionada à eficiência ou desempenho energético;
* Identificar fatores socioeconômicos associados à variável resposta;
* Avaliar a qualidade do ajuste do modelo;
* Demonstrar a aplicação prática de Modelos Lineares Generalizados em dados reais.

---

## ⚙️ Estrutura do Projeto

### 1. Preparação dos Dados

* Importação do dataset
* Tratamento de valores ausentes
* Seleção de variáveis relevantes
* Organização dos dados no formato país-ano

### 2. Análise Exploratória

* Estatísticas descritivas
* Avaliação da distribuição da variável resposta
* Análise de correlação entre variáveis
* Identificação de assimetria e possíveis outliers

### 3. Modelagem Estatística

* Definição da variável resposta
* Seleção das covariáveis
* Ajuste do Modelo Linear Generalizado
* Família: Gamma
* Função de ligação: log
* Estimação por máxima verossimilhança

### 4. Avaliação e Diagnóstico

* Significância estatística dos coeficientes
* Critério de Informação de Akaike (AIC)
* Análise de resíduos (Pearson e Deviance)
* Avaliação da adequação do modelo

---

## 📊 Principais Resultados

* Identificação de variáveis com associação estatisticamente significativa com a variável resposta;
* Modelo com bom desempenho segundo critérios de informação;
* Evidência de relações consistentes entre indicadores econômicos e energéticos;
* Interpretação multiplicativa dos coeficientes devido ao uso do link log.

---

## 🛠️ Tecnologias Utilizadas

* Python
* pandas
* numpy
* statsmodels
* matplotlib
* seaborn

---

## 👨‍💻 Sobre o Projeto

Este projeto demonstra domínio em:

* Modelos Lineares Generalizados
* Análise estatística aplicada
* Manipulação e tratamento de dados
* Diagnóstico de modelos
* Comunicação técnica de resultados

Desenvolvido como prática avançada em Ciência de Dados aplicada ao contexto energético global.

---

# Gamma Regression Model Applied to Global Sustainable Energy Data

## 🔎 Overview

This project presents the application of a **Generalized Linear Model (GLM) with Gamma distribution** using the *Global Data on Sustainable Energy (2000–2020)* dataset available on Kaggle.

The main objective is to model a continuous and strictly positive energy-related variable based on economic and energy indicators from approximately 175 countries over a 20-year period.

The project highlights best practices in:

* Data cleaning and preprocessing
* Exploratory Data Analysis (EDA)
* Applied statistical modeling
* Model diagnostics and evaluation
* Technical interpretation of results

---

## 🎯 Project Objective

To apply Gamma regression in order to:

* Model a continuous energy efficiency or performance variable;
* Identify socioeconomic factors associated with the response variable;
* Evaluate model goodness-of-fit;
* Demonstrate a practical application of Generalized Linear Models on real-world data.

---

## ⚙️ Project Structure

### 1. Data Preparation

* Dataset import
* Missing value handling
* Relevant feature selection
* Country-year panel organization

### 2. Exploratory Data Analysis

* Descriptive statistics
* Distribution analysis of the response variable
* Correlation analysis
* Skewness and outlier assessment

### 3. Statistical Modeling

* Response variable definition
* Covariate selection
* Generalized Linear Model fitting
* Family: Gamma
* Link function: log
* Maximum Likelihood Estimation (MLE)

### 4. Model Evaluation and Diagnostics

* Statistical significance of coefficients
* Akaike Information Criterion (AIC)
* Residual analysis (Pearson and Deviance residuals)
* Overall model adequacy assessment

---

## 📊 Key Findings

* Identification of statistically significant predictors;
* Model demonstrating good fit according to information criteria;
* Evidence of consistent relationships between economic and energy indicators;
* Multiplicative interpretation of coefficients due to the log link function.

---

## 🛠️ Technologies Used

* Python
* pandas
* numpy
* statsmodels
* matplotlib
* seaborn

---

## 👨‍💻 About This Project

This project demonstrates proficiency in:

* Generalized Linear Models
* Applied statistical modeling
* Data preprocessing and cleaning
* Model diagnostics
* Technical communication of analytical results

It was developed as an advanced applied data science project focused on global energy indicators.

---
