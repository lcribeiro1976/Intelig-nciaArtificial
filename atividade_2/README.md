# 🎓 Previsão de Evasão de Alunos

## 📌 Objetivo do Projeto
Desenvolver um pipeline completo de Inteligência Artificial para prever a evasão
de alunos, integrando um modelo de Machine Learning a uma aplicação web em Python.

## 📊 Dataset Utilizado
- **Arquivo**: `dataset_alunos_evasao.csv`  
- **Registros**: 1.000 alunos  
- **Features**: 14 atributos (acadêmicos, socioeconômicos e comportamentais)  
- **Variável alvo**: `status_curso` → Concluiu (0) / Evadiu (1)  
- **Distribuição**: 70% Concluiu / 30% Evadiu

### Atributos do Dataset
| Coluna | Tipo | Descrição |
|---|---|---|
| idade | Numérico | Idade do aluno |
| genero | Categórico | Feminino / Masculino / Outro |
| estado_civil | Categórico | Solteiro / Casado / Outro |
| tipo_escola_ensino_medio | Categórico | Pública / Privada |
| nota_enem | Numérico | Nota no ENEM (400–899) |
| renda_familiar | Numérico | Renda em salários mínimos |
| bolsa_estudos | Categórico | Sim / Não |
| mora_com_familia | Categórico | Sim / Não |
| trabalha | Categórico | Não trabalha / Meio período / Período integral |
| horas_estudo_semanal | Numérico | Horas de estudo por semana |
| tem_computador | Categórico | Sim / Não |
| distancia_campus_km | Numérico | Distância até o campus em km |
| recebe_assistencia_estudantil | Categórico | Sim / Não |
| primeira_opcao_curso | Categórico | Sim / Não |

## 🤖 Modelos Avaliados e Justificativa
Foram treinados e comparados 4 modelos:

| Modelo | Acurácia | AUC-ROC |
|---|---|---|
| Regressão Logística | ~0.75 | ~0.82 |
| **Random Forest** ← escolhido | ~0.83 | ~0.91 |
| Gradient Boosting | ~0.82 | ~0.90 |
| Rede Neural (MLP) | ~0.80 | ~0.87 |

**Justificativa**: O Random Forest apresentou o melhor AUC-ROC, é robusto a
outliers, oferece interpretabilidade via feature importance, e não exige
ajuste fino extensivo de hiperparâmetros.

## 📈 Métricas de Avaliação
| Métrica | Uso |
|---|---|
| **Acurácia** | % geral de previsões corretas |
| **AUC-ROC** | Capacidade de separar as classes |
| **CV 5-fold** | Verificação de generalização |
| **Precisão / Recall / F1** | Avaliação por classe |
| **Matriz de Confusão** | Visualização dos erros |

## 🚀 Como Executar

### Google Colab (recomendado)
1. Abra `previsao_evasao_alunos.ipynb` no Google Colab
2. Execute **Runtime → Run all**
3. Na célula 3, clique em **Escolher arquivos** e selecione o `dataset_alunos_evasao.csv`
4. Para a interface web: insira seu token ngrok (gratuito em https://ngrok.com)

### Local
```bash
# Com Docker (recomendado)
docker-compose up --build
# Acesse: http://localhost:5000

# Sem Docker
pip install -r requirements.txt
python app.py
# Acesse: http://localhost:5000
```

## 🌐 Utilizando a Aplicação Web
1. Acesse a URL (ngrok ou localhost:5000)
2. Preencha os 14 campos do formulário com os dados do aluno
3. Clique em **Prever Evasão**
4. Resultado: risco (Alto ⚠️ / Baixo ✅) + barra de probabilidade

## 📂 Estrutura do Repositório
```
├── previsao_evasao_alunos.ipynb   # Notebook principal (Colab)
├── app.py                          # Aplicação web Flask
├── Dockerfile                      # Imagem Docker
├── docker-compose.yml              # Orquestração Docker
├── requirements.txt                # Dependências Python
├── dataset_alunos_evasao.csv       # Dataset fornecido
├── README.md                       # Este arquivo
└── modelo/
    ├── modelo_evasao.pkl            # Modelo treinado
    ├── scaler.pkl                   # Normalizador
    ├── encoders.pkl                 # Encoders categóricos
    └── feature_names.pkl            # Lista de features
```
