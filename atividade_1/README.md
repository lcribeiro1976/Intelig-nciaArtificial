# README.md.
readme_content = """# Previsão de Séries Temporais Financeiras com LSTM

> Projeto acadêmico de aprendizado de máquina para previsão de preços de ações
> utilizando redes neurais Long Short-Term Memory (LSTM).

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.13%2B-orange?logo=tensorflow)
![yfinance](https://img.shields.io/badge/yfinance-0.2%2B-green)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3%2B-orange)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## Sumário

1. [Objetivo](#-objetivo)
2. [Critérios de Avaliação Atendidos](#-critérios-de-avaliação-atendidos)
3. [Estrutura do Repositório](#-estrutura-do-repositório)
4. [Ativos Analisados](#-ativos-analisados)
5. [Caracterização do Problema — Séries Temporais](#-caracterização-do-problema--séries-temporais)
6. [Dados Financeiros — Coleta e Justificativa](#-dados-financeiros--coleta-e-justificativa)
7. [Pré-processamento das Sequências Temporais](#-pré-processamento-das-sequências-temporais)
8. [Modelo Neural — Arquitetura LSTM](#-modelo-neural--arquitetura-lstm)
9. [Avaliação do Desempenho](#-avaliação-do-desempenho)
10. [Organização do Código](#-organização-do-código)
11. [Como Executar](#-como-executar)
12. [Resultados Esperados](#-resultados-esperados)
13. [Tecnologias](#-tecnologias)
14. [Limitações e Melhorias Futuras](#-limitações-e-melhorias-futuras)

---

## Objetivo

Desenvolver um sistema completo de previsão de preços de ações utilizando
redes neurais LSTM, cobrindo todo o pipeline de ciência de dados:
coleta → pré-processamento → modelagem → avaliação → previsão futura.

---

## Critérios de Avaliação Atendidos

| # | Critério | Como foi atendido | Módulo |
|---|----------|-------------------|--------|
| 1 | Correta caracterização do problema de séries temporais | Definição formal de séries temporais financeiras, autocorrelação, não-estacionariedade, janela deslizante e fundamentação do split cronológico | [`02_preprocessamento.py`](#-pré-processamento-das-sequências-temporais) |
| 2 | Uso adequado dos dados financeiros | yfinance com `auto_adjust=True`, 6 anos de dados, 5 ativos de setores e mercados distintos, cache em CSV | [`01_coleta_dados.py`](#-dados-financeiros--coleta-e-justificativa) |
| 3 | Preparação correta das sequências temporais | Scaler fitado **apenas no treino**, janela de 60 dias, split cronológico **sem shuffle**, reshape 3D para LSTM | [`02_preprocessamento.py`](#-pré-processamento-das-sequências-temporais) |
| 4 | Escolha e implementação do modelo neural | Arquitetura LSTM 128→64 com justificativa detalhada, Dropout, L2, 3 callbacks de controle | [`03_modelo.py`](#-modelo-neural--arquitetura-lstm) |
| 5 | Avaliação coerente do desempenho | 5 métricas complementares (RMSE, RMSE%, MAE, MAPE, R²) avaliadas **exclusivamente no conjunto de teste** | [`04_avaliacao.py`](#-avaliação-do-desempenho) |
| 6 | Clareza e organização do código | 6 módulos independentes, `config.py` central, docstrings completas em todas as funções, comentários explicativos | [Todos os módulos](#-organização-do-código) |
| 7 | Qualidade da documentação | README com fundamentos teóricos, arquitetura, métricas, exemplos e instruções detalhadas | Este arquivo |

---

## Estrutura do Repositório

```
previsao-acoes-lstm/
│
├── previsao_acoes_lstm.ipynb   # Notebook orquestrador — executa os 6 módulos em sequência
│
├── src/
│   ├── config.py               # Configurações centrais (ativos, datas, hiperparâmetros)
│   ├── 01_coleta_dados.py      # Coleta via yfinance + cache em CSV
│   ├── 02_preprocessamento.py  # Feature engineering + normalização + janela deslizante
│   ├── 03_modelo.py            # Arquitetura LSTM + treinamento + callbacks
│   ├── 04_avaliacao.py         # Métricas + gráficos de avaliação
│   ├── 05_previsoes.py         # Previsão futura (30 dias úteis)
│   └── 06_visualizacoes.py     # Gráficos EDA + curvas de aprendizado
│
├── requirements.txt            # Dependências com versões mínimas
├── README.md                   # Esta documentação
│
├── dados/                      # (gerado automaticamente)
│   ├── PETR4_SA.csv
│   ├── VALE3_SA.csv
│   ├── ITUB4_SA.csv
│   ├── AAPL.csv
│   ├── MSFT.csv
│   └── _resumo_coleta.csv
│
├── modelos/                    # (gerado automaticamente)
│   ├── lstm_PETR4_SA.keras
│   ├── lstm_VALE3_SA.keras
│   ├── lstm_ITUB4_SA.keras
│   ├── lstm_AAPL.keras
│   ├── lstm_MSFT.keras
│   ├── log_treinamento.csv
│   └── historico_<TICKER>.csv  # curvas loss/val_loss por ativo
│
├── graficos/                   # (gerado automaticamente)
│   ├── 01_desempenho_base100.png
│   ├── 02_precos_bollinger.png
│   ├── 03_retornos_correlacao.png
│   ├── 04_volatilidade_historica.png
│   ├── 05_divisao_treino_teste.png
│   ├── 06_curvas_aprendizado.png
│   ├── 07_previsao_vs_real.png
│   ├── 08_residuos_dispersao.png
│   ├── 09_comparacao_metricas.png
│   ├── 10_heatmap_metricas.png
│   ├── 11_previsoes_futuras_individuais.png
│   └── 12_previsoes_comparativas_base100.png
│
└── resultados/                 # (gerado automaticamente)
    ├── metricas_avaliacao.csv
    ├── relatorio_final.csv
    ├── config.json
    ├── resumo_previsoes_futuras.csv
    ├── previsoes_teste_<TICKER>.csv
    └── previsao_futura_<TICKER>.csv
```

> Cada módulo em `src/` pode ser executado de forma independente
> (`python src/01_coleta_dados.py`). O notebook os orquestra em sequência.

---

## Ativos Analisados

| Ticker | Empresa | Mercado | Setor | Moeda |
|--------|---------|---------|-------|-------|
| PETR4.SA | Petrobras | B3 (Brasil) | Energia / Petróleo | BRL |
| VALE3.SA | Vale S.A. | B3 (Brasil) | Mineração | BRL |
| ITUB4.SA | Itaú Unibanco | B3 (Brasil) | Financeiro | BRL |
| AAPL | Apple Inc. | NASDAQ (EUA) | Tecnologia | USD |
| MSFT | Microsoft Corp. | NASDAQ (EUA) | Tecnologia | USD |

A diversidade de setores, moedas e mercados permite avaliar a
**generalização** do modelo em diferentes regimes econômicos.

---

## Caracterização do Problema — Séries Temporais

### O que é uma série temporal financeira?

Uma série temporal é uma sequência de observações ordenadas no tempo,
onde a **posição relativa de cada ponto importa**.

Séries financeiras possuem propriedades específicas que determinam
as decisões de modelagem:

| Propriedade | Descrição | Impacto no modelo |
|-------------|-----------|-------------------|
| **Autocorrelação** | O valor de amanhã depende dos dias anteriores | Justifica o uso de modelos recorrentes (LSTM) |
| **Não-estacionariedade** | Média e variância mudam ao longo do tempo | Justifica a normalização por janela |
| **Heteroscedasticidade** | Volatilidade varia (clusters) | Justifica o indicador de volatilidade rolling |
| **Dependências não-lineares** | Relações complexas entre indicadores | Justifica o uso de redes neurais vs. modelos lineares |
| **Dependências de longo prazo** | Tendências que duram semanas/meses | Justifica o LSTM (vs. RNN simples) |

### Formulação como aprendizado supervisionado

O problema é transformado em **regressão supervisionada** pela técnica
de **janela deslizante** (sliding window):

```
Entrada X[t]: [Close_{t-60}, Close_{t-59}, …, Close_{t-1}]   shape (60, n_features)
              "Os últimos 60 dias como contexto"

Saída   y[t]: Close_t                                         escalar
              "O preço de fechamento do próximo dia"
```

Para cada posição `t ≥ 60` na série, extraímos uma janela de 60 dias
como entrada e o dia seguinte como alvo — criando o dataset supervisionado
que alimenta a rede LSTM.

### Por que o split deve ser cronológico?

```
ERRADO — com shuffle:
   [dia_500, dia_3, dia_1200, dia_800, ...]  → treino
   [dia_2, dia_950, dia_1500, ...]           → teste
   Problema: o modelo aprende com dados do futuro!
   As métricas ficam artificialmente otimistas.

CORRETO — cronológico:
   [dia_1, dia_2, …, dia_1200]  → treino  (80% — mais antigos)
   [dia_1201, …, dia_1500]      → teste   (20% — mais recentes)
   O modelo só vê o passado. O teste simula produção real.
```

---

## Dados Financeiros — Coleta e Justificativa

### Fonte e período

- **Biblioteca:** `yfinance >= 0.2` — API gratuita do Yahoo Finance
- **Período:** 01/01/2019 → 31/12/2024 (~6 anos de pregões)
- **Tipo:** OHLCV diário ajustado

### Por que `auto_adjust=True`?

Sem ajuste, a série histórica contém **saltos artificiais** nas datas de:
- **Split de ações** — ex: Apple 7:1 em 2014 → preço histórico cai 7×
- **Pagamento de dividendos** — ex: queda no preço ex-dividendo

Com `auto_adjust=True`, esses eventos são **retroativamente corrigidos**,
produzindo uma série contínua e matematicamente comparável ao longo do tempo.

```python
df = yf.download(ticker, start=inicio, end=fim,
                 auto_adjust=True,    # ← preços ajustados
                 progress=False)
```

### Por que 6 anos de dados (2019–2024)?

O período cobre intencionalmente diferentes **regimes de mercado**:

| Período | Evento | Característica |
|---------|--------|----------------|
| 2019 | Mercado em alta | Baixa volatilidade, tendência clara |
| 2020 | COVID-19 | Crash de março, recuperação em V |
| 2021 | Recuperação pós-COVID | Alta volatilidade, rally tecnológico |
| 2022 | Alta de juros global | Mercado de baixa (bear market) |
| 2023 | Normalização | IA generativa, recuperação seletiva |
| 2024 | Consolidação | Múltiplos regimes |

Expor o modelo a essas variações é essencial para **generalização**.

---

## Pré-processamento das Sequências Temporais

### Pipeline de 5 etapas

```
Dados OHLCV brutos
      ↓
① Feature Engineering   — 8 indicadores técnicos calculados
      ↓
② Corte treino/teste    — n_treino determinado ANTES do scaler
      ↓
③ Normalização Min-Max  — fit EXCLUSIVO no conjunto de treino
      ↓
④ Janela Deslizante     — pares (X, y) supervisionados
      ↓
⑤ Split Cronológico     — arrays finais sem shuffle
      ↓
X_treino (80%), X_teste (20%) — prontos para o modelo
```

### Feature Engineering — 8 Indicadores Técnicos

| Feature | Cálculo | Captura |
|---------|---------|---------|
| `retorno_1d` | `Close.pct_change() × 100` | Momentum de curto prazo |
| `mm_7` | Média móvel 7 dias | Tendência semanal |
| `mm_21` | Média móvel 21 dias (~1 mês) | Tendência mensal |
| `volatilidade` | `std(retornos, 21d) × √252` | Risco/incerteza anualizado |
| `amplitude` | `(High−Low)/Close × 100` | Variação intradiária |
| `rsi_14` | RSI de Wilder (14 períodos) | Sobrecompra/sobrevenda (0–100) |
| `macd` | `EMA(12) − EMA(26)` | Momentum e mudança de tendência |
| `macd_signal` | `EMA(9) do MACD` | Linha de sinal do MACD |

### Normalização — Por que apenas no treino?

**Problema:** Se o `MinMaxScaler` fosse fitado em **todos os dados**,
seus parâmetros (min e max globais) incluiriam valores do **futuro**
(conjunto de teste). Isso é chamado de **data leakage**.

**Consequência:** O modelo "veria" o futuro indiretamente durante
o treino → métricas irrealisticamente boas → modelo inútil em produção.

**Solução correta:**
```python
scaler_X = MinMaxScaler(feature_range=(0, 1))

# Fit SOMENTE no treino (80% mais antigos)
scaler_X.fit(df.values[:n_treino])

# Transform em treino + teste (usando os parâmetros do treino)
dados_norm = scaler_X.transform(df.values)
```

### Janela Deslizante — Reshape 3D para LSTM

```python
for i in range(janela, len(dados_norm)):
    X.append(dados_norm[i - janela : i])   # shape (60, 13)
    y.append(dados_norm[i, close_idx])      # escalar

X = np.array(X)  # shape: (n_amostras, 60, 13)
#                           ↑           ↑   ↑
#                        amostras   timesteps  features
```

O formato `(n_amostras, timesteps, features)` é o esperado
pela camada `LSTM` do Keras.

---

## Modelo Neural — Arquitetura LSTM

### Por que LSTM e não outros modelos?

| Modelo | Capacidade temporal | Dependências longas | Escolhido? |
|--------|--------------------|--------------------|-----------|
| MLP (rede densa) | Não | Não | Não — ignora ordem dos dias |
| RNN simples | Sim | Vanishing gradient | Não — esquece padrões longos |
| **LSTM** | Sim | Gates controlam memória | **Sim** |
| Transformer | Sim | Attention | Alternativa para etapa futura |

O LSTM (Hochreiter & Schmidhuber, 1997) resolve o **problema do gradiente
que desaparece** em RNNs através de três gates:

- **Gate de entrada** (`iₜ`) — controla o que da entrada atual memorizar
- **Gate de esquecimento** (`fₜ`) — controla o que da memória apagar
- **Gate de saída** (`oₜ`) — controla o que da memória expor

Isso permite ao modelo capturar padrões de **tendência, suporte e resistência**
ao longo de toda a janela de 60 dias.

### Arquitetura implementada

```
Input  (60 timesteps, 13 features)
  ↓
LSTM   128 unidades  return_sequences=True   ← extrai padrões de alto nível
  ↓                  + L2(1e-4) nos pesos    ← regularização
Dropout 0.20                                  ← descarta 20% das unidades
  ↓
LSTM    64 unidades  return_sequences=False  ← comprime em um único vetor
  ↓                  + L2(1e-4) nos pesos
Dropout 0.20
  ↓
Dense   32 unidades  ativação ReLU           ← representação não-linear final
  ↓
Dense    1 unidade   linear                  ← previsão do próximo preço
```

### Hiperparâmetros e justificativas

| Parâmetro | Valor | Justificativa |
|-----------|-------|---------------|
| Janela (lookback) | 60 dias | ~2 meses de pregão; captura ciclos mensais/bimestrais |
| LSTM camada 1 | 128 unidades | Capacidade suficiente para padrões complexos |
| LSTM camada 2 | 64 unidades | Compressão progressiva da representação |
| Dropout | 0.20 | Regularização moderada; evita overfitting sem underfitting |
| L2 | 1e-4 | Penaliza pesos muito grandes; melhora generalização |
| Otimizador | Adam lr=0.001 | Adaptativo; padrão eficaz para LSTM |
| Loss | MSE | Regressão; penaliza erros grandes |
| Batch size | 32 | Balança velocidade e generalização |
| EarlyStopping | patience=15 | Para quando val_loss estagna; restaura melhores pesos |
| ReduceLROnPlateau | factor=0.5, patience=7 | Reduz lr pela metade; permite convergência fina |

### Callbacks de treinamento

```python
EarlyStopping(monitor='val_loss', patience=15,
              restore_best_weights=True)
# Para o treino 15 épocas após o último mínimo de val_loss.
# Restaura automaticamente os pesos da melhor época.

ReduceLROnPlateau(monitor='val_loss', factor=0.5,
                  patience=7, min_lr=1e-6)
# Reduz o learning rate × 0.5 quando val_loss estagna por 7 épocas.
# Permite ajustes finos na fase final de convergência.

ModelCheckpoint(save_best_only=True)
# Salva o modelo em disco APENAS quando val_loss atinge novo mínimo.
# Garante que o arquivo salvo seja sempre o melhor treinado.
```

---

## Avaliação do Desempenho

### Princípio fundamental

> A avaliação é realizada **exclusivamente no conjunto de teste** —
> os 20% mais recentes dos dados, **nunca utilizados durante o treino**.
> Avaliar no treino produziria métricas infladas e sem valor preditivo.

### As 5 métricas e por que usamos todas

| Métrica | Fórmula | Unidade | Interpreta | Limitação |
|---------|---------|---------|------------|-----------|
| **RMSE** | `√(Σ(ŷ−y)²/n)` | Preço (R$/\$) | Penaliza erros grandes | Depende da escala do ativo |
| **RMSE (%)** | `RMSE/média(y)×100` | % | Compara ativos de escalas diferentes | — |
| **MAE** | `Σ\|ŷ−y\|/n` | Preço (R$/\$) | Erro médio absoluto; robusto a outliers | Depende da escala |
| **MAPE (%)** | `Σ\|ŷ−y\|/\|y\|×100` | % | Padrão em finanças; independente de escala | Instável perto de zero |
| **R²** | `1 − SS_res/SS_tot` | — | Variância explicada (1.0 = perfeito) | Pode ser alto com bias |

**Por que 5 métricas?** Uma única métrica pode mascarar problemas.
Por exemplo: R² alto com MAPE alto indica que o modelo acerta a tendência
mas erra a magnitude. Usar todas as 5 garante **diagnóstico robusto**.

### Referência para interpretação

| RMSE (%) / MAPE (%) | Qualidade |
|--------------------|-----------|
| < 2% | Excelente |
| 2% – 5% | Muito bom |
| 5% – 10% | Bom |
| > 10% | Requer melhoria |

---

## Organização do Código

### Responsabilidade única por módulo

Cada arquivo tem uma responsabilidade bem definida e pode ser
executado **independentemente**:

```
config.py            → Única fonte de verdade para configurações
01_coleta_dados.py   → ÚNICO responsável por download e cache
02_preprocessamento.py → ÚNICO responsável pelo pipeline de features
03_modelo.py         → ÚNICO responsável pela arquitetura e treino
04_avaliacao.py      → ÚNICO responsável por métricas e diagnóstico
05_previsoes.py      → ÚNICO responsável pela projeção futura
06_visualizacoes.py  → ÚNICO responsável por gráficos EDA
```

### Padrões de qualidade aplicados

- **Docstrings completas** em todas as funções (parâmetros, retorno, notas)
- **Anotações de tipo** (`ticker: str`, `janela: int = JANELA`)
- **Comentários explicativos** a cada decisão técnica não óbvia
- **Separação de configuração e lógica** — `config.py` centraliza tudo
- **Funções com responsabilidade única** (máx. ~50 linhas cada)
- **Ponto de entrada** (`if __name__ == "__main__"`) em cada módulo
- **Reprodutibilidade** — `SEED=42` em numpy e TensorFlow

---

## Como Executar

### Opção 1 — Google Colab (recomendado)

```
1. Crie um novo repositório no GitHub e faça upload de todos os arquivos
2. Acesse: https://colab.research.google.com
3. File → Open notebook → GitHub → cole a URL do repositório
4. Abra o arquivo previsao_acoes_lstm.ipynb
5. Runtime → Run all  (≈ 20–40 min dependendo do hardware)
```

### Opção 2 — Execução local

```bash
# 1. Clone o repositório
git clone https://github.com/SEU_USUARIO/previsao-acoes-lstm.git
cd previsao-acoes-lstm

# 2. Crie e ative um ambiente virtual
python -m venv venv
source venv/bin/activate          # Linux/macOS
# venv\Scripts\activate           # Windows

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Execute os módulos em sequência (ou abra o notebook)
python src/01_coleta_dados.py
python src/02_preprocessamento.py
python src/03_modelo.py
python src/04_avaliacao.py
python src/05_previsoes.py

# Ou abra o notebook no Jupyter
jupyter notebook previsao_acoes_lstm.ipynb
```

### Personalizar ativos ou período

Edite **apenas** o arquivo `src/config.py`:

```python
# Adicionar ou substituir ativos
ACOES = {
    "PETR4.SA": "Petrobras",
    "BBAS3.SA": "Banco do Brasil",   # ← novo ativo
    "AAPL":     "Apple Inc.",
}

# Alterar período
DATA_INICIO = "2020-01-01"
DATA_FIM    = "2024-12-31"

# Alterar janela temporal
JANELA = 30   # de 60 para 30 dias
```

---

## Resultados Esperados

Após a execução completa, serão gerados **~35 arquivos** em 4 pastas:

| Pasta | Arquivos | Descrição |
|-------|----------|-----------|
| `dados/` | 5 CSVs + resumo | Séries históricas dos ativos |
| `modelos/` | 5 `.keras` + logs | Modelos treinados e históricos |
| `graficos/` | 12 PNGs | EDA, avaliação e previsões |
| `resultados/` | ~15 CSVs + JSON | Métricas, previsões e relatório final |

---

## Tecnologias

| Biblioteca | Versão mín. | Função |
|-----------|-------------|--------|
| Python | 3.10+ | Linguagem base |
| yfinance | 0.2.36 | Coleta de dados do Yahoo Finance |
| TensorFlow / Keras | 2.13 | Construção e treinamento do LSTM |
| NumPy | 1.24 | Operações matriciais |
| pandas | 2.0 | Manipulação de séries temporais |
| scikit-learn | 1.3 | MinMaxScaler, métricas de avaliação |
| Matplotlib | 3.7 | Gráficos e visualizações |
| seaborn | 0.12 | Heatmaps e gráficos estatísticos |

---

## Limitações e Melhorias Futuras

### Limitações conhecidas

- **Mercado estocástico** — preços de ações contêm componente aleatório que nenhum modelo pode prever perfeitamente
- **Sem dados exógenos** — notícias, taxa de juros, câmbio e eventos macroeconômicos não são considerados
- **Previsão iterativa acumula erro** — a incerteza cresce a cada passo além do primeiro dia previsto
- **Modelo treinado offline** — não se atualiza com novos dados automaticamente

### Possíveis melhorias

- [ ] Incorporar dados macroeconômicos (SELIC, USD/BRL, VIX)
- [ ] Comparar LSTM vs. GRU vs. Transformer
- [ ] Otimização de hiperparâmetros com Optuna ou Keras Tuner
- [ ] Intervalos de confiança com Monte Carlo Dropout
- [ ] Pipeline de atualização automática com novos dados
- [ ] Análise de sentimento de notícias como feature adicional

---

"""
