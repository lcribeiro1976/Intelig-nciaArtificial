Market Basket Analysis — Supermercado
Análise de padrões de compra com o algoritmo Apriori para geração de insights gerenciais em um supermercado de médio porte.

Sobre o Projeto
Este projeto foi desenvolvido como atividade prática da disciplina de Inteligência Artificial do Instituto Federal do Triângulo Mineiro (IFTM). O objetivo é aplicar técnicas de Market Basket Analysis para identificar associações relevantes entre produtos e transformá-las em recomendações estratégicas para o supermercado.

Objetivos
Carregar e explorar o dataset de compras (formato market basket)
Aplicar o algoritmo Apriori para identificar conjuntos frequentes de produtos
Gerar regras de associação e analisar métricas: suporte, confiança e lift
Selecionar as regras mais relevantes para o contexto do negócio
Responder às questões orientadoras com base nos dados
Estrutura do Repositório
market-basket-analysis/
│
├── basket_supermercado_1000.csv   # Dataset com 1000 transações e 20 produtos
├── market_basket_analysis.ipynb   # Notebook principal (Google Colab)
├── regras_associacao.csv          # Regras geradas pelo Apriori (saída)
│
├── visualizacoes/
│   ├── freq_produtos.png          # Frequência de compra por produto
│   ├── coocorrencia.png           # Heatmap de co-ocorrência
│   ├── metricas_regras.png        # Suporte x Confiança x Lift
│   └── top_regras_lift.png        # Top 15 regras por Lift
│
└── README.md
Dataset
Arquivo: basket_supermercado_1000.csv

1.000 transações de clientes
20 produtos: pao, leite, cafe, manteiga, acucar, arroz, feijao, macarrao, carne, frango, peixe, ovos, queijo, presunto, cerveja, refrigerante, vinho, hortifruti, doces, limpeza
Cada coluna assume valor 0 (não comprado) ou 1 (comprado)
Tecnologias Utilizadas
Biblioteca	Finalidade
pandas	Manipulação e exploração do dataset
numpy	Operações numéricas
mlxtend	Algoritmo Apriori e geração de regras
matplotlib	Visualizações gráficas
seaborn	Heatmap de co-ocorrência
Como Executar
Acesse colab.research.google.com
Faça upload do arquivo market_basket_analysis.ipynb
Faça upload do arquivo basket_supermercado_1000.csv no painel lateral
Execute todas as células: Runtime → Run all
As dependências são instaladas automaticamente na primeira célula.

Abordagem Adotada
Pré-processamento
O dataset já estava no formato binário (0/1), sendo necessário apenas converter as colunas para tipo bool antes de aplicar o Apriori.

Parâmetros do Apriori
Parâmetro	Valor	Justificativa
Suporte mínimo	15%	Captura produtos comprados juntos em pelo menos 150 transações
Confiança mínima	40%	Garante regras com relevância estatística razoável
Lift mínimo (filtro)	> 1.2	Elimina associações espúrias causadas por produtos populares
Principais Resultados
Regras mais fortes encontradas
SE compra...	ENTÃO compra...	Lift	Confiança
arroz	feijao	~1.7	~72%
feijao	arroz	~1.7	~72%
pao + presunto	queijo	~1.8	~65%
cafe	acucar	~1.5	~60%
cafe	leite	~1.4	~55%
carne	arroz	~1.5	~68%
Valores aproximados — os resultados exatos são exibidos no notebook.

Insights e Interpretações de Negócio
Q1 — Quais produtos apresentam maior associação entre si?
Arroz e Feijão formam o par com maior lift do dataset, refletindo um padrão cultural forte da alimentação brasileira. O par Pão + Manteiga e Café + Açúcar também se destacam como combinações do café da manhã.

Q2 — Existem produtos que funcionam como “âncora” para outras compras?
Pão é o principal produto âncora: aparece como antecedente em diversas regras fortes, puxando compras de manteiga, presunto, queijo e leite. Arroz também funciona como âncora para feijão, carne e frango.

Q3 — Quais regras possuem maior potencial para ações promocionais?
Regras com alta confiança (≥ 50%) e lift > 1.2 indicam os melhores candidatos a promoções combinadas:

Combo Café da Manhã: Pão + Manteiga + Café + Leite
Combo Almoço Brasileiro: Arroz + Feijão + Carne
Combo Lanche: Pão + Presunto + Queijo
Q4 — Alguma regra encontrada pode ser considerada enganosa ou pouco útil? Por quê?
Sim. Produtos com altíssima frequência individual (pão, leite, ovos) geram regras com confiança aparentemente alta, mas com lift próximo de 1, indicando que a associação não é mais forte do que o esperado pelo acaso. Essas regras devem ser descartadas para fins promocionais.

Q5 — Como os resultados podem impactar o layout do supermercado ou estratégias de venda?
PROXIMIDADE DE GONDOLAS:

Arroz e Feijao -> manter na mesma secao (alta co-ocorrencia)
Pao, Manteiga, Presunto e Queijo -> agrupar em secao de cafe da manha
Cafe, Acucar e Leite -> exposicao conjunta na secao de bebidas quentes
Carne/Frango -> proximo ao Arroz (complemento de refeicao)
ESTRATEGIAS PROMOCIONAIS:

Combo "Cafe da manha": Pao + Manteiga + Cafe + Leite
Combo "Almoco brasileiro": Arroz + Feijao + Carne
Combo "Lanche": Pao + Presunto + Queijo
Desconto progressivo: compre 2 itens do combo, 10% no 3o
GESTAO DE ESTOQUE:

Monitorar reposicao conjunta dos pares de alta associacao
Falta de Arroz pode reduzir vendas de Feijao e vice-versa
Arquivos de Saída
Ao executar o notebook, os seguintes arquivos são gerados automaticamente:

regras_associacao.csv — todas as regras com suporte, confiança, lift e leverage
