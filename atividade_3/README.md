### Pré-visualização do Conteúdo do README

Aqui tem uma visão geral de como o ficheiro está estruturado internamente:

```markdown
# 🚢 Projeto Titanic: Aprendizado de Máquina & Explainable AI (XAI)

Este repositório contém a resolução da atividade prática de modelagem preditiva utilizando o clássico dataset **Titanic**, com foco especial em **Explainable AI (XAI)** através da biblioteca **SHAP (SHapley Additive exPlanations)**. 

O objetivo principal deste projeto é ir além da precisão das métricas tradicionais, compreendendo detalhadamente os critérios e o impacto de cada variável nas decisões tomadas pelo modelo preditivo.

---

## Objetivo da Atividade

Aplicar, de forma prática, técnicas de Machine Learning e Inteligência Artificial Explicável (XAI) para mapear o fluxo completo de um projeto de ciência de dados:
1. **Preparação e Exploração dos Dados**
2. **Treinamento e Validação do Modelo**
3. **Análise de Importância de Variáveis Global**
4. **Interpretação Local e Global usando SHAP**

---

## Estrutura e Etapas de Desenvolvimento

O projeto está estruturado em um único notebook Python (`.ipynb`), dividido rigorosamente nas seguintes etapas:

### 1. Coleta e Carregamento dos Dados
* Importação e leitura do arquivo `titanic.csv`.
* Inspeção inicial dos dados: visualização das primeiras linhas, tipos das variáveis, identificação de valores nulos e análise de distribuição da variável alvo (`Survived`).

### 2. Preparação dos Dados (Pipeline de Preprocessamento)
* **Tratamento de valores ausentes:** Imputação da mediana para a variável `Age` e da moda para `Embarked`.
* **Codificação de variáveis categóricas:** Transformação de variáveis como `Sex` e `Embarked` em representações numéricas apropriadas (ex: *Label Encoding* ou *One-Hot Encoding*).
* **Seleção de Atributos:** Filtro de colunas irrelevantes para a modelagem direta (ex: `PassengerId`, `Name`, `Ticket`, `Cabin`).
* **Divisão de Dados:** Separação inequívoca entre variáveis preditoras ($X$) e variável alvo ($y$), seguida pela divisão em conjuntos de **Treino** e **Teste**.

### 3. Treinamento do Modelo
* Instanciação e treinamento do algoritmo supervisionado **`RandomForestClassifier`** utilizando a biblioteca `scikit-learn`.

### 4. Validação do Modelo
* Avaliação do desempenho preditivo no conjunto de testes com base nas seguintes métricas:
  * **Accuracy** (Acurácia)
  * **Matriz de Confusão**
  * **Precision, Recall e F1-Score**

### 5. Análise de Feature Importance (Global)
* Geração do gráfico nativo de importância de atributos do Random Forest.
* Breve análise identificando quais variáveis exerceram maior influência na redução de impureza dos nós da árvore e quais tiveram menor relevância.

### 6. Explainable AI (XAI) com SHAP
* Utilização da biblioteca `shap` para extrair os valores Shapley baseados no modelo treinado.
* Geração e análise do **SHAP Summary Plot**, detalhando:
  * Quais variáveis causam maior impacto nas previsões.
  * Como valores altos ou baixos de cada variável afetam positiva ou negativamente a probabilidade de sobrevivência.

### 7. Explicação de uma Previsão Individual (Local)
* Seleção pontual de um passageiro específico do dataset.
* Apresentação do gráfico de força (**Force Plot / Waterfall Plot**) para demonstrar os fatores exatos que empurraram a previsão para cima (sobrevivência) ou para baixo (óbito).

---

## Tecnologias e Bibliotecas Utilizadas

O projeto foi construído utilizando o ecossistema científico do Python:
* **Python 3.x**
* **Pandas & NumPy** — Manipulação, limpeza e análise de dados.
* **Matplotlib & Seaborn** — Visualizações gráficas estatísticas.
* **Scikit-Learn** — Preprocessamento, divisão de dados, treino do `RandomForestClassifier` e métricas de validação.
* **SHAP** — Computação dos valores Shapley e geração dos gráficos de interpretabilidade local e global.

---

## Como Executar o Projeto

1. Certifique-se de ter o arquivo `titanic.csv` no mesmo diretório do notebook.
2. Instale as dependências necessárias utilizando o gerenciador de pacotes `pip`:
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn shap
