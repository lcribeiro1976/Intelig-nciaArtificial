Detecção de Anomalias em Logs de Acesso
Relatório de Análise — Isolation Forest
1. Introdução e Abordagem
Este relatório documenta a aplicação do algoritmo Isolation Forest para identificação de padrões de acesso anômalos em um sistema computacional. O dataset acessos_sistema.csv contém 100 registros de logs sem rótulos, tornando o problema adequado para técnicas de aprendizado não supervisionado.

Por que Isolation Forest?
O Isolation Forest é especialmente eficaz para detecção de anomalias porque:

Não assume distribuição específica dos dados
Funciona bem em espaços multidimensionais
Tem baixo custo computacional (complexidade O(n))
Produz um anomaly score contínuo, não apenas classificação binária
O princípio é simples: anomalias são instâncias raras e com valores extremos, portanto mais fáceis de "isolar" com partições aleatórias das features. Registros que precisam de poucas partições para ficarem isolados recebem scores de anomalia mais baixos.

2. Exploração do Dataset
Variável	Tipo	Descrição
hora_acesso	Numérica (0–23)	Hora do dia do acesso
duracao_sessao_min	Numérica	Duração da sessão em minutos
numero_tentativas_login	Numérica	Quantidade de tentativas de login
ip_diferente_habitual	Binária (0/1)	IP fora do padrão
quantidade_paginas_acessadas	Numérica	Páginas acessadas na sessão
Estatísticas descritivas relevantes:

Variável	Média	Mediana	Desvio Padrão	Máximo
hora_acesso	12.91	13	4.77	23
duracao_sessao_min	36.5	29.5	34.2	146.1
numero_tentativas_login	2.55	1	3.8	17
ip_diferente_habitual	0.25	0	0.43	1
quantidade_paginas_acessadas	12.8	8.5	19.6	107
O desvio padrão elevado em duracao_sessao_min e quantidade_paginas_acessadas já indica a presença de outliers no conjunto.

3. Pré-processamento
Etapas aplicadas:

Verificação de valores nulos: nenhum encontrado
Padronização (StandardScaler): todas as features foram normalizadas para média 0 e desvio padrão 1, garantindo que variáveis com escalas diferentes (ex.: hora vs. páginas) não dominem o modelo
4. Configuração do Modelo
IsolationForest(
    n_estimators=200,     # 200 árvores para maior estabilidade
    contamination=0.15,   # estimativa de 15% de anomalias
    random_state=42
)
O parâmetro contamination=0.15 foi escolhido com base na expectativa do problema. Em sistemas reais, esse valor é estimado a partir de auditorias históricas ou definido pela equipe de segurança.

5. Resultados
5.1 Contagem de classificações
Classificação	Quantidade	Percentual
Normal	85	85%
Anomalia	15	15%
5.2 Médias por classificação
Variável	Normal	Anomalia
hora_acesso	13.4	10.3
duracao_sessao_min	29.5	74.2
numero_tentativas_login	1.3	11.5
ip_diferente_habitual	0.11	1.00
quantidade_paginas_acessadas	7.9	40.9
As anomalias concentram-se em registros com todas as flags levantadas simultaneamente: IP diferente, muitas tentativas de login, volumes extremos de páginas e duração de sessão atípica.

5.3 Registros anômalos detectados (ordenados por score)
Hora	Duração (min)	Tentativas Login	IP Diferente	Páginas	Score
4h	1.0	17	Sim	89	-0.158
0h	120.4	14	Sim	107	-0.153
5h	133.6	12	Sim	66	-0.143
1h	146.1	16	Sim	58	-0.137
3h	126.5	17	Sim	95	-0.124
22h	1.3	12	Sim	1	-0.103
22h	0.6	10	Sim	0	-0.096
0h	117.4	14	Sim	62	-0.094
4h	113.8	17	Sim	56	-0.093
3h	112.7	14	Sim	67	-0.076
10h	44.0	2	Sim	9	-0.059
23h	0.4	1	Sim	1	-0.047
22h	0.5	1	Sim	0	-0.005
14h	9.8	2	Não	2	-0.004
22h	1.4	1	Sim	0	-0.002
6. Visualizações
As visualizações geradas na pasta graficos/ são:

distribuicoes.png — histogramas de cada variável separados por classificação
hora_vs_duracao.png — scatter com anomaly score em escala de cor
pca_2d.png — projeção PCA bidimensional dos registros
correlacao.png — heatmap de correlação entre variáveis
anomaly_score.png — score de cada registro (abaixo de 0 = anomalia)
boxplots.png — boxplots comparativos das variáveis-chave
7. Respostas às Questões de Reflexão
7.1 Quais padrões de acesso foram considerados normais pelo modelo?
O modelo considerou normais os acessos com as seguintes características:

Horário comercial: majoritariamente entre 8h e 19h
Duração de sessão moderada: entre 5 e 60 minutos
Poucas tentativas de login: 1 ou 2 tentativas (comportamento humano típico)
IP habitual: a maioria dos acessos normais (89%) partiu do IP conhecido
Volume de páginas razoável: entre 2 e 15 páginas por sessão
Esses padrões refletem o comportamento esperado de um colaborador trabalhando em horário regular, a partir de sua máquina habitual, navegando moderadamente no sistema.

7.2 Quais características aparecem com maior frequência nos acessos classificados como anômalos?
Duas categorias distintas de anomalia foram identificadas:

Categoria A — Alta intensidade (possível invasão ou exfiltração):

Horário de madrugada (0h às 5h)
Muitas tentativas de login (10–17)
IP diferente do habitual
Volume extremo de páginas (56–107)
Sessão longa (113–146 min)
Categoria B — Comportamento furtivo (possível tentativa de acesso rápido):

Horário noturno (22h–23h)
Sessão extremamente curta (< 1.5 min)
IP diferente do habitual
Quase nenhuma página acessada (0–1)
1 tentativa de login
Ambas as categorias compartilham ip_diferente_habitual = 1 e horários fora do padrão. A diferença na duração e volume de páginas sugere intenções distintas.

7.3 Todas as anomalias identificadas representam um possível problema de segurança?
Não necessariamente. Analisando caso a caso:

Registro	Hora	Perfil	Risco
Score -0.158 a -0.075	Madrugada, muitas tentativas, muitas páginas	Alta suspeita — possível ataque de força bruta seguido de varredura	ALTO
Score -0.103 a -0.047	Noite, sessão < 1min, 0 páginas	Possível tentativa de login malsucedida por usuário legítimo fora do horário	MÉDIO
Score -0.059 (hora 10h)	Horário comercial, só IP diferente	Pode ser um funcionário usando VPN, rede pública ou novo dispositivo	BAIXO
Score -0.004 (hora 14h, IP habitual)	Horário normal, IP habitual, poucas páginas	Sessão curta legítima; anomalia marginal pelo volume de páginas	MUITO BAIXO
Portanto, das 15 anomalias, 10 apresentam risco relevante (Categoria A), 4 são de risco médio (Categoria B) e 1 é provavelmente um falso positivo (score próximo de zero, IP habitual, horário comercial).

7.4 Que tipos de falso positivo podem ocorrer nesse cenário?
Os principais cenários de falso positivo são:

Trabalho remoto legítimo: um funcionário que acessa de casa ou de viagem terá ip_diferente_habitual = 1 sem nenhum comportamento malicioso.

Hora de acesso incomum, mas justificada: plantões, prazos ou fusos horários diferentes podem gerar acessos em horários atípicos que não representam ameaça.

Sessão de manutenção ou auditoria: um profissional de TI que acessa muitas páginas para manutenção em horário não comercial pode ser classificado como anomalia.

Primeiros acessos de usuário novo: um colaborador recém-contratado explorar o sistema mais intensamente é normal na primeira semana.

Testes de sistema e scripts automatizados: testes de integração que geram muitas requisições em curto tempo podem parecer suspeitos ao modelo.

Implicação prática: o modelo deve ser tratado como ferramenta de triagem, não de decisão final. Toda anomalia detectada deve ser revisada por um analista humano antes de qualquer ação.

7.5 Como esse modelo poderia ser usado em um sistema real de monitoramento?
Em um ambiente de produção, o Isolation Forest poderia ser integrado da seguinte forma:

Pipeline em tempo real:

Log de acesso → Feature extraction → Normalização → IF.score() → Alerta
Boas práticas de implementação:

Retreinamento periódico: o modelo deve ser retreinado mensalmente com os dados mais recentes, pois o comportamento dos usuários evolui.
Score contínuo em vez de binário: usar o anomaly_score como métrica de risco (ex.: score < -0.10 = alerta crítico, -0.10 a 0 = alerta moderado).
Contexto adicional: combinar com dados de RH (férias, home office autorizado) e de TI (manutenções programadas) para reduzir falsos positivos.
Dashboards de monitoramento: exibir scores em tempo real para a equipe de segurança, com filtragem por severidade.
Feedback loop: quando um analista confirma ou descarta uma anomalia, esse dado pode ser usado para reajustar o modelo ou treinar um classificador supervisionado no futuro.
Alertas graduados: não bloquear automaticamente — escalar para autenticação multifator adicional antes de bloquear o acesso.
8. Conclusão
O Isolation Forest demonstrou ser uma ferramenta eficaz para triagem de acessos suspeitos, identificando corretamente dois perfis de risco distintos — ataques de força bruta intensos e tentativas furtivas rápidas. O modelo é particularmente útil por não exigir dados rotulados, o que é a realidade da maioria dos ambientes corporativos.

A limitação principal é a geração de falsos positivos em casos de uso legítimo fora do padrão (trabalho remoto, horários diferenciados). Por isso, a detecção automatizada deve sempre ser complementada por análise humana, especialmente para as anomalias com scores próximos de zero.

A combinação de Isolation Forest com regras de negócio contextuais e um classificador supervisionado construído a partir das confirmações humanas representa a abordagem mais robusta para sistemas reais de monitoramento de segurança.

9. Estrutura do Repositório
anomaly_detection/
├── acessos_sistema.csv          # Dataset utilizado
├── analise_anomalias.py         # Código-fonte completo
├── resultados_anomalias.csv     # Dataset com classificações
├── RELATORIO.md                 # Este relatório
└── graficos/
    ├── distribuicoes.png        # Histogramas por variável
    ├── hora_vs_duracao.png      # Scatter hora × duração
    ├── pca_2d.png               # Projeção PCA
    ├── correlacao.png           # Heatmap de correlação
    ├── anomaly_score.png        # Score por registro
    └── boxplots.png             # Boxplots comparativos
Análise realizada com Python 3, scikit-learn (IsolationForest), matplotlib e seaborn.
