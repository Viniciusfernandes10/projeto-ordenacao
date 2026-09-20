# Análise de Desempenho e Consumo Energético de Algoritmos de Ordenação em Python

**Universidade Federal do Rio Grande do Norte — Escola de Ciência e Tecnologia**
**ECT3707 — Tópicos Avançados em Computação IV**
**Professor:** Sérgio Queiroz de Medeiros

**Autores:** Antonélia da Silva Sabino, Vinícius Fernandes de Abreu

**Natal, 2026**

Uma investigação experimental sobre o tempo de execução, o consumo de energia
e a eficiência de diferentes algoritmos de ordenação implementados em Python.

---

## 1. Introdução

Você já pensou em por que comparamos algoritmos de ordenação?

Os algoritmos de ordenação desempenham um papel fundamental na computação,
pois permitem organizar conjuntos de dados de acordo com determinados
critérios. Essa organização facilita pesquisas, comparações, análises e o
processamento de informações em diferentes aplicações computacionais.

Apesar de apresentarem o mesmo objetivo geral, os algoritmos de ordenação
podem possuir diferenças significativas em relação à quantidade de operações
realizadas, ao tempo necessário para concluir a execução e aos recursos
computacionais consumidos.

Neste contexto, este trabalho apresenta um experimento desenvolvido com o
objetivo de comparar diferentes implementações de algoritmos de ordenação
utilizando a linguagem de programação Python. A investigação considera
aspectos relacionados ao desempenho computacional e ao consumo energético,
permitindo observar como as características dos algoritmos influenciam os
resultados obtidos.

Foram consideradas implementações dos algoritmos Bubble Sort, Insertion Sort
e Selection Sort, incluindo versões tradicionais e alternativas otimizadas. A
partir das medições realizadas, busca-se compreender como o aumento do
tamanho das entradas interfere no comportamento dos algoritmos e quais
diferenças podem ser observadas entre suas implementações.

## 2. Cenário do experimento

Para a realização dos testes, foi utilizado um ambiente computacional
composto por hardware e software específicos. A identificação dessas
características é importante porque o desempenho de um programa não depende
exclusivamente do algoritmo implementado, mas também das condições em que sua
execução ocorre.

Os experimentos foram realizados em um computador com a seguinte
configuração:

| Componente | Informação |
|---|---|
| Processador (CPU) | Intel® Core™ i5-3470 |
| Quantidade de núcleos | 4 |
| Quantidade de threads | 4 |
| Memória RAM | 8,0 GiB |
| Sistema operacional | Debian GNU/Linux |
| Versão do sistema operacional | 12 (bookworm) |
| Arquitetura | 64 bit |

*Tabela 1 — Fonte: autores*

A utilização de um mesmo ambiente computacional para a realização dos testes
permite reduzir diferenças relacionadas ao hardware e ao software. Entretanto,
fatores como processos executados em segundo plano, temperatura do
processador, frequência de operação e gerenciamento de energia ainda podem
interferir nas medições. Por esse motivo, as condições de execução precisam
ser consideradas durante a análise dos resultados.

## 3. Metodologia: como o experimento foi realizado?

O experimento foi desenvolvido por meio da implementação e execução de
diferentes algoritmos de ordenação em Python. A metodologia foi organizada de
maneira a permitir a comparação entre as implementações utilizando conjuntos
de dados de diferentes tamanhos.

### 3.1. Algoritmos avaliados

Foram analisadas seis implementações:

- **Bubble Sort tradicional:** algoritmo que percorre repetidamente o
  conjunto de dados, comparando elementos adjacentes e realizando trocas
  quando necessário, sempre executando o número máximo de passagens.
- **Bubble Sort otimizado:** versão que interrompe a execução assim que uma
  passagem completa não realiza nenhuma troca, e reduz o intervalo de
  comparação a cada passagem (já que os últimos elementos vão ficando
  ordenados progressivamente), buscando reduzir operações desnecessárias.
- **Insertion Sort tradicional:** algoritmo que organiza os elementos por
  meio da inserção de cada valor em sua posição adequada dentro da parte já
  ordenada, movendo elementos através de trocas sucessivas.
- **Insertion Sort otimizado:** versão que desloca os elementos maiores uma
  posição à frente (em vez de trocar par a par), reduzindo o número de
  escritas na memória a cada passo.
- **Selection Sort tradicional:** algoritmo que seleciona repetidamente o
  menor elemento da parte ainda não ordenada e o posiciona na posição
  correta.
- **Selection Sort Melhorado (HeapSort):** versão com complexidade
  O(n log n), que constrói uma heap máxima a partir do vetor e extrai
  repetidamente o maior elemento, reorganizando a heap a cada extração — em
  contraste com a complexidade O(n²) da versão tradicional.

### 3.2. Tamanhos das entradas

Para observar o comportamento dos algoritmos diante do aumento da quantidade
de elementos, foram utilizados três tamanhos de entrada:

| Experimento | Quantidade de elementos |
|---|---|
| Entrada 1 | 10.000 |
| Entrada 2 | 20.000 |
| Entrada 3 | 50.000 |

*Tabela 2 — Fonte: autores*

Os conjuntos de dados foram gerados utilizando um programa em C++
(`geraEntrada.cpp`) que produz um vetor com números embaralhados
pseudoaleatoriamente. A utilização de diferentes tamanhos de entrada (10.000,
20.000 e 50.000 elementos) permite observar como o crescimento da quantidade
de elementos influencia o tempo de execução e o consumo de recursos.

### 3.3. Procedimento de execução

Os códigos foram interpretados e executados pelo ambiente de execução padrão
da linguagem Python 3. Cada implementação foi executada com os conjuntos de
dados definidos para o experimento, e a mesma entrada foi reutilizada por
todos os seis algoritmos em cada tamanho, garantindo que a comparação entre
eles não fosse afetada por vetores de dificuldade diferente.

Durante as execuções, foram coletadas informações referentes ao tempo de
execução, tempo de CPU e ao consumo energético, utilizando o `perf`
(ferramenta de profiling nativa do Linux) com os eventos
`power/energy-pkg/`, `duration_time`, `user_time` e `system_time`. Cada
algoritmo foi executado 10 vezes para cada tamanho de entrada, permitindo
calcular médias e analisar a distribuição dos dados estatísticos. As medições
foram organizadas em uma planilha para facilitar a comparação entre os
algoritmos.

### 3.4. Métricas avaliadas

As principais métricas consideradas foram:

- **Tempo de execução:** representa o intervalo de tempo necessário para a
  realização da tarefa de ordenação.
- **Tempo de usuário (user time):** corresponde ao tempo de CPU utilizado na
  execução do código em modo de usuário.
- **Tempo de sistema (system time):** corresponde ao tempo de CPU utilizado
  em operações executadas no contexto do sistema operacional.
- **Consumo de energia:** representa a quantidade de energia (em Joules)
  registrada durante a execução, conforme os recursos de medição disponíveis
  no ambiente experimental.

Essas métricas permitem analisar diferentes aspectos do comportamento dos
programas. Enquanto o tempo de execução fornece uma medida do desempenho
temporal, os tempos de usuário e de sistema ajudam a compreender como o
processamento foi distribuído. Já a medição energética permite investigar o
consumo de recursos durante a realização da tarefa. É importante destacar que
a interpretação do consumo energético depende do método de medição utilizado
e dos componentes efetivamente monitorados.

## 4. Resultados experimentais

Nesta seção, são apresentados os resultados obtidos durante a execução dos
algoritmos. Os dados foram organizados em tabelas e gráficos para facilitar a
identificação de diferenças entre as implementações.

### 4.1. Resultados de tempo de execução

*Tabela 3 — Tempo de execução dos algoritmos de ordenação (segundos)*

| Algoritmo | 10.000 | 20.000 | 50.000 |
|---|---|---|---|
| Bubble Sort | 18,23 | 74,93 | 455,56 |
| Bubble Sort Melhorado | 11,03 | 43,21 | 270,30 |
| Insertion Sort | 7,58 | 27,98 | 192,48 |
| Insertion Sort otimizado | 4,98 | 19,27 | 128,61 |
| Selection Sort | 1,86 | 7,43 | 47,11 |
| Selection Sort Melhorado (HeapSort) | 0,07 | 0,12 | 0,28 |

*Fonte: autores*

A partir dos dados apresentados, observa-se que as variações no tempo de
execução foram bastante acentuadas entre os diferentes algoritmos de
ordenação. Para N = 50.000, o **Bubble Sort** apresentou o maior tempo de
execução (455,56s), seguido do **Bubble Sort Melhorado** (270,30s) e do
**Insertion Sort** (192,48s). Em contraste, o **Selection Sort Melhorado
(HeapSort)** apresentou o menor tempo em todos os tamanhos testados, com
apenas 0,28 segundos em N = 50.000 — cerca de 1.600 vezes mais rápido que o
Bubble Sort tradicional no mesmo tamanho de entrada. O **Selection Sort**
tradicional também se destacou por um tempo relativamente baixo (47,11s),
mais rápido que as três implementações de Bubble e Insertion Sort.

Esse resultado está de acordo com o esperado teoricamente: enquanto as
demais implementações têm complexidade O(n²), o HeapSort tem complexidade
O(n log n), e essa diferença assintótica se torna cada vez mais evidente
conforme o tamanho da entrada cresce.

### 4.2. Resultados de consumo energético

*Tabela 4 — Consumo energético das implementações (Joules)*

| Algoritmo | 10.000 | 20.000 | 50.000 |
|---|---|---|---|
| Bubble Sort | 554,94 | 2.356,34 | 14.340,36 |
| Bubble Sort Melhorado | 341,23 | 1.339,82 | 8.355,18 |
| Insertion Sort | 234,29 | 951,97 | 5.982,53 |
| Insertion Sort otimizado | 152,47 | 591,73 | 4.071,90 |
| Selection Sort | 58,76 | 234,88 | 1.505,11 |
| Selection Sort Melhorado (HeapSort) | 2,26 | 3,90 | 9,23 |

*Fonte: autores*

Os resultados de consumo energético indicam um crescimento diretamente
proporcional ao tempo de execução e ao tamanho da entrada N para todos os
algoritmos. O **Bubble Sort** apresentou o maior consumo acumulado para
N = 50.000 (14.340,36 J), seguido pelo Bubble Sort Melhorado e pelo
Insertion Sort. Em contrapartida, o **Selection Sort Melhorado (HeapSort)**
apresentou, de forma consistente, o menor consumo energético em todos os
tamanhos de entrada testados (apenas 9,23 J em N = 50.000) — quase 1.600
vezes menos energia que o Bubble Sort no mesmo cenário.

Vale destacar um ponto de atenção nos dados de potência instantânea: o
Insertion Sort registrou, em N = 20.000, uma potência (Potência Exe) de
aproximadamente 58,90 W — valor destoante das demais medições da própria
implementação, que ficaram na faixa de 30 W. Isso pode indicar interferência
momentânea de outro processo no ambiente de teste durante essa execução
específica, sendo um ponto a se considerar como possível ruído de medição.

A comparação entre o consumo energético e o tempo de execução permite
investigar se as implementações que concluíram a ordenação em menor tempo
também apresentaram menor consumo de energia. Neste experimento, essa
correspondência se confirmou de forma consistente: o algoritmo mais rápido
(HeapSort) foi também o mais econômico energeticamente, e o mais lento
(Bubble Sort) foi também o de maior consumo — sugerindo que, para algoritmos
de mesma natureza (sequenciais, sem paralelismo ou I/O relevante), tempo de
execução e consumo energético estão fortemente correlacionados.

*Tabela 5 — Tempo de CPU (user_time + system_time, em segundos)*

| Algoritmo | 10.000 | 20.000 | 50.000 |
|---|---|---|---|
| Bubble Sort | 18,21 | 74,92 | 455,50 |
| Bubble Sort Melhorado | 11,01 | 43,19 | 270,25 |
| Insertion Sort | 7,57 | 30,73 | 192,43 |
| Insertion Sort otimizado | 4,97 | 19,25 | 128,58 |
| Selection Sort | 1,84 | 7,42 | 47,09 |
| Selection Sort Melhorado (HeapSort) | 0,06 | 0,11 | 0,26 |

*Fonte: autores*

A análise das métricas de tempo de CPU em relação ao tempo de execução total
permite observar uma equivalência quase direta entre as duas medidas em
todos os algoritmos e tamanhos de entrada — o tempo de CPU corresponde a
praticamente 100% do tempo de execução total (`system_time` é sempre uma
fração muito pequena do tempo total). Isso é esperado para programas
sequenciais em Python que não realizam operações de entrada/saída
significativas durante a ordenação, como é o caso destas implementações.

## 5. Análise e discussão dos resultados

A análise dos resultados deve considerar conjuntamente o comportamento
temporal, o consumo energético e as características teóricas dos algoritmos.
De maneira geral, algoritmos com complexidade temporal quadrática, como as
versões tradicionais do Bubble Sort e do Selection Sort, apresentam
crescimento potencialmente elevado do número de operações conforme o tamanho
da entrada aumenta. O Insertion Sort também possui complexidade quadrática
no caso médio e no pior caso.

No experimento realizado, os resultados demonstraram que o **Selection Sort
Melhorado (HeapSort)** obteve, de forma clara, o melhor desempenho temporal e
energético entre os seis algoritmos avaliados, com tempos entre 250 e 1.600
vezes menores que o Bubble Sort tradicional, dependendo do tamanho da
entrada. Essa vantagem cresce à medida que N aumenta, exatamente como
esperado pela diferença entre as complexidades O(n log n) e O(n²).

A comparação entre as versões tradicionais e otimizadas dos métodos O(n²)
também traz um resultado consistente: em todos os três métodos (Bubble,
Insertion e, de forma menos acentuada, entre Selection tradicional e o
próprio Selection Sort clássico), a versão otimizada consumiu sistematicamente
menos tempo e energia que a versão tradicional, mesmo mantendo a mesma
complexidade assintótica O(n²). Isso demonstra que otimizações de constante
(reduzir o número de comparações, trocas ou escritas de memória) têm impacto
real e mensurável no consumo energético, mesmo quando não mudam a classe de
complexidade do algoritmo.

É importante evitar conclusões baseadas exclusivamente em um único tamanho
de entrada, pois variações sutis no código ganham proporções maiores em
volumes maiores de dados. Além disso, fatores relacionados ao ambiente
computacional, como variações na frequência do processador ou trocas de
contexto pelo sistema operacional, podem interferir nas medições. Dessa
forma, os resultados devem ser interpretados como evidências experimentais
obtidas nas condições específicas em que os testes foram realizados.

## 6. Limitações do experimento

Apesar de permitir uma comparação entre diferentes algoritmos, o experimento
apresenta algumas limitações que devem ser consideradas. A primeira está
relacionada às características do ambiente computacional utilizado, pois os
resultados podem variar quando os mesmos códigos são executados em
computadores com processadores, quantidades de memória RAM ou sistemas
operacionais diferentes.

Outra limitação diz respeito ao método de geração dos dados, visto que o
comportamento de alguns algoritmos depende da disposição inicial dos
elementos — vetores já ordenados ou invertidos podem produzir resultados
bastante diferentes dos observados aqui com entradas totalmente aleatórias
(por exemplo, a otimização de parada antecipada do Bubble Sort tende a ter
efeito bem mais expressivo em entradas parcialmente ordenadas do que no
cenário testado).

Também é necessário considerar a quantidade de repetições realizadas: 10
execuções por configuração permitem calcular uma média razoável, mas um
número maior de repetições ajudaria a reduzir ainda mais a influência de
ruído nas medições — especialmente relevante para o caso do HeapSort, cujas
execuções são tão curtas que ficam mais sensíveis a interferências pontuais
do sistema.

## 7. Conclusão

O experimento permitiu investigar o comportamento de diferentes
implementações de algoritmos de ordenação desenvolvidas em Python,
considerando o tempo de execução, o consumo energético e outras métricas
relacionadas à utilização da CPU. A comparação entre as seis implementações
mostrou de forma clara que o **Selection Sort Melhorado (HeapSort)**
apresentou o melhor tempo de execução e o menor consumo total de energia em
todos os tamanhos de entrada testados, seguido pelo Selection Sort
tradicional — confirmando experimentalmente a vantagem teórica de um
algoritmo O(n log n) sobre implementações O(n²).

Em relação ao crescimento do tamanho das entradas, verificou-se um aumento
acentuado do tempo de execução e da energia consumida para 10.000, 20.000 e
50.000 elementos em todas as implementações O(n²), especialmente no Bubble
Sort. A análise energética indicou que o consumo total acumulado acompanha
diretamente o tempo de execução, enquanto a avaliação dos tempos de usuário
e de sistema demonstrou que quase a totalidade do tempo de execução é
concentrada no processamento ativo de CPU.

Os resultados também permitiram discutir a importância das otimizações de
implementação: mesmo mantendo a mesma complexidade assintótica, pequenas
mudanças no código (reduzir escritas de memória, evitar comparações
desnecessárias) geraram economias de energia mensuráveis e consistentes em
todos os métodos O(n²) testados. Como possibilidade de trabalhos futuros,
sugere-se ampliar a quantidade de repetições, testar diferentes distribuições
de dados (incluindo vetores parcialmente ordenados), avaliar outros tamanhos
de entrada e realizar os experimentos em ambientes computacionais distintos.

## Repositório

```
├── src/                    → código-fonte dos 6 algoritmos + gerador de entradas
├── dados/                  → entradas de teste e resultados brutos do perf
└── planilha_experimento    → planilha com todas as medições e gráficos
```

