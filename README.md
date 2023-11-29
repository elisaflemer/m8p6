# Perceptron 

Este é um projeto simples em Python que implementa um perceptron para simular portas lógicas básicas. No código, você encontrará uma classe Perceptron que representa um perceptron de uma camada, bem como funções para treinamento e teste.

## Estrutura do Projeto
O projeto contém os seguintes arquivos:

- perceptron.py: Contém a implementação da classe Perceptron e funções para treinamento e teste.
- main.py: Exemplo de uso do perceptron para treinar e testar em portas lógicas.

## Como rodar

1. Clone este repositório
2. Instale as bibliotecas necessárias (numpy)
3. Rode o arquivo main.py com o comando abaixo

```
python3 main.py
```

## Resultados

### Porta AND

| Input 1 | Input 2 | Output |
| ------- | ------- | ------ |
| 0       | 0       | 0      |
| 0       | 1       | 0      |
| 1       | 0       | 0      |
| 1       | 1       | 1      |

## Porta OR

| Input 1 | Input 2 | Output |
| ------- | ------- | ------ |
| 0       | 0       | 0      |
| 0       | 1       | 1      |
| 1       | 0       | 1      |
| 1       | 1       | 1      |

## Porta NAND

| Input 1 | Input 2 | Output |
| ------- | ------- | ------ |
| 0       | 0       | 1      |
| 0       | 1       | 1      |
| 1       | 0       | 1      |
| 1       | 1       | 0      |


## Porta XOR (em uma das rodadas)

| Input 1 | Input 2 | Output (Predicted) | Output (True) |
| ------- | ------- | ------------------- | ------------- |
| 0       | 0       | 1 (errado)          | 0             |
| 0       | 1       | 1 (errado)          | 1             |
| 1       | 0       | 0 (errado)          | 1             |
| 1       | 1       | 0 (errado)          | 0             |

A porta XOR é um exemplo clássico de um problema que não pode ser resolvido por um único perceptron. Isso ocorre porque a relação entre as entradas e a saída da porta XOR não é linearmente separável. Ou seja, não é possível desenhar uma única linha reta para separar os 0 dos dos 1 no espaço de entrada 2D. Uma comparação entre o plano do XOR e o das outras portas pode ser vista abaixo.

