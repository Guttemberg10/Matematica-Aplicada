# riângulo de Pascal com Python

Este projeto apresenta uma implementação automatizada do Triângulo de Pascal, utilizando a fórmula da **combinação simples (Cₙ,ₚ)**. O objetivo é tornar mais intuitivo o entendimento da construção do triângulo e mostrar como a programação pode ser usada para facilitar esse processo.

---

## Origem matemática: Combinação Simples

A base do Triângulo de Pascal é a **fórmula da combinação simples**, que calcula quantas formas diferentes podemos escolher `p` elementos de um conjunto com `n` elementos, **sem considerar a ordem**.

A fórmula é dada por:

<p align="center"><strong>
C<sub>n,p</sub> = n! / [p! × (n - p)!]
</strong></p>

Onde:

- `n!` é o fatorial de `n` (produto de todos os inteiros de 1 até `n`)
- `p!` é o fatorial de `p`
- `(n - p)!` é o fatorial da diferença entre `n` e `p`

🔹 **Exemplo**:  
C(4,2) = 4! / (2! × 2!) = (24) / (2 × 2) = **6**

Essa fórmula é a base para calcular os valores do Triângulo de Pascal.

---

## O que é o Triângulo de Pascal?

O Triângulo de Pascal é uma estrutura triangular composta por números inteiros que representam as combinações simples de `n` elementos tomados de `p` em `p`. Cada linha do triângulo representa os coeficientes binomiais para um valor de `n`.

### Como ele funciona:

- A primeira linha é o caso base: `1`
- Cada número interno da linha é a **soma dos dois números acima dele** na linha anterior.
- As bordas do triângulo são sempre `1`

### Exemplo até a 5ª linha:

1
1 1
1 2 1
1 3 3 1
1 4 6 4 1


Cada valor pode ser obtido por `C(n, p)`, onde `n` é o número da linha (começando do 0) e `p` é a posição na linha.

---

## 🤖 Como o algoritmo automatiza o triângulo

O algoritmo em Python desenvolvido faz o seguinte:

1. **Recebe a quantidade de linhas** que o usuário deseja ver no Triângulo de Pascal.
2. Usa a **fórmula da combinação simples (Cₙ,ₚ)** para calcular cada valor.
3. Imprime o triângulo linha por linha, com os valores calculados dinamicamente.

### 🔍 Principais funções:

- `combinacaoSimples(n, p)`: Calcula o valor de C(n, p) usando laços `while` para obter fatoriais.
- Um laço principal percorre as linhas e colunas, aplicando a fórmula para cada posição.

### 🧪 Exemplo de execução:
Digite a quantidade de linhas que deseja ver: 5
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1


---

## Benefícios da Automação

- Torna o processo mais **eficiente** e **didático**
- Permite **explorar quantas linhas quiser**, sem cálculos manuais
- Ideal para **estudantes de matemática**, **professores** ou curiosos da programação

---

## 🧑‍💻 Autor

Gabriel Novais  
📅 Projeto criado em 16/09/2025

---

## Arquivo principal

- `trianguloDePascal.py`: contém todo o código necessário para rodar o algoritmo.

---

## Como executar

1. Instale o Python (se ainda não tiver).
2. Salve o código em um arquivo `.py`.
3. Execute no terminal:

```bash
python trianguloDePascal.py
