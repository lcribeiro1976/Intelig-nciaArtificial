# - Classificação de Dígitos Manuscritos com Rede Neural (MNIST)

**Trabalho Final – Disciplina de Inteligência Artificial**

---

## - Descrição do Problema

O problema consiste em **reconhecer automaticamente dígitos escritos à mão** (0 a 9) a partir de imagens em escala de cinza de 28×28 pixels.

Esse é um problema clássico de **classificação multiclasse** em Visão Computacional e Aprendizado Profundo, com diversas aplicações reais, como:

- Leitura automática de cheques bancários
- Reconhecimento de CEPs nos Correios
- Digitalização de formulários manuscritos
- Sistemas de reconhecimento de placas e documentos

---

## - Descrição da Solução Proposta

Foi treinada uma **Rede Neural Artificial (RNA)** do tipo **Feedforward Multilayer Perceptron (MLP)** utilizando o dataset **MNIST**, composto por 70.000 imagens de dígitos manuscritos já rotulados.

### Arquitetura da Rede Neural

```
Entrada         → 784 neurônios (28×28 pixels achatados)
Camada Oculta 1 → 256 neurônios (ativação ReLU)
Dropout 1       → 30% (regularização)
Camada Oculta 2 → 128 neurônios (ativação ReLU)
Dropout 2       → 20% (regularização)
Saída           → 10 neurônios (ativação Softmax — um por dígito)
```

### Conceitos de IA Aplicados

| Conceito | Descrição |
|---|---|
| MLP (Multilayer Perceptron) | Rede neural com múltiplas camadas totalmente conectadas |
| ReLU | Função de ativação que introduz não-linearidade |
| Softmax | Converte saídas em probabilidades por classe |
| Dropout | Regularização para evitar overfitting |
| Otimizador Adam | Algoritmo adaptativo de gradiente descendente |
| Early Stopping | Interrupção antecipada baseada na perda de validação |
| Normalização | Padronização dos pixels para o intervalo [0, 1] |

### Resultados Obtidos

| Métrica | Valor |
|---|---|
| **Acurácia no Teste** | ~98% |
| Total de parâmetros | ~236.554 |
| Épocas de treinamento | Até 30 (com Early Stopping) |
| Dataset | MNIST – 70.000 imagens |

---

## - Tecnologias e Bibliotecas Utilizadas

| Biblioteca | Versão | Função |
|---|---|---|
| Python | 3.10+ | Linguagem de programação base |
| TensorFlow / Keras | 2.x | Construção e treinamento da rede neural |
| NumPy | 1.x | Manipulação de arrays numéricos |
| Matplotlib | 3.x | Visualização de gráficos e imagens |
| Seaborn | 0.12+ | Matriz de confusão estilizada |
| Scikit-learn | 1.x | Relatório de classificação |

---

## - Como Executar o Projeto

### Opção 1 – Google Colab

1. Acesse o [Google Colab](https://colab.research.google.com)
2. Clique em **Arquivo > Fazer upload de notebook**
3. Selecione o arquivo `classificacao_digitos_mnist.ipynb`
4. Clique em **Ambiente de execução > Executar tudo** (`Ctrl + F9`)
5. Aguarde a execução de todas as células (≈ 2–3 minutos)

> - Nenhuma instalação adicional é necessária no Colab — todas as bibliotecas já estão disponíveis.

### Opção 2 – Execução Local

#### Pré-requisitos

- Python 3.10 ou superior
- pip (gerenciador de pacotes do Python)

#### Passo a Passo

```bash
# 1. Clone o repositório
git clone https://github.com/seu-usuario/mnist-classificacao.git
cd mnist-classificacao

# 2. Instale as dependências
pip install -r requirements.txt

# 3. Inicie o Notebook
notebook classificacao_digitos_mnist.ipynb
```

---

## - Requisitos de Ambiente

### Para Google Colab
- Conta Google (gratuita)
- Navegador atualizado (Chrome, Firefox, Edge)
- Nenhuma instalação adicional necessária

### Para Execução Local

```
python>=3.10
tensorflow>=2.12
numpy>=1.23
matplotlib>=3.6
seaborn>=0.12
scikit-learn>=1.2
jupyter>=1.0
```

Arquivo `requirements.txt` disponível na raiz do repositório.

---

## - Estrutura do Repositório

```
mnist-classificacao/
│
├── classificacao_digitos_mnist.ipynb   # Notebook principal (Google Colab)
├── requirements.txt                    # Dependências para execução local
└── README.md                           # Este arquivo
```

---

## - Autor

Desenvolvido como **Trabalho Final** da Disciplina de Inteligência Artificial.

