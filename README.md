# Sistema de PDV — Nível 1

## O que o código faz

O programa simula um **Ponto de Venda (PDV)** para registrar compras de clientes. Ele recebe o valor da compra, a quantidade de itens, a idade do cliente e um possível cupom de fidelidade. A partir dessas informações, aplica os descontos correspondentes, calcula o valor final da compra e, ao encerrar o sistema, apresenta um resumo com todas as compras realizadas e salva essas informações no arquivo `resumo.txt`.

## Como ele faz

1. O código solicita o **valor da compra** e verifica se ele é válido e não é negativo.
2. Solicita a **quantidade de itens** e verifica se é um número inteiro válido.
3. Solicita a **idade do cliente** e verifica se ela é válida.
4. Solicita um **cupom de fidelidade**, caso o cliente possua um.
5. Aplica **20% de desconto** para clientes com 65 anos ou mais.
6. Verifica se o valor após o desconto é maior que **R$ 100,00**. Se for, aplica mais **10% de desconto**.
7. Verifica se o cliente possui mais de **3 itens**. Nesse caso, aplica mais **5% de desconto**.
8. Verifica se o cupom informado é `FIDELIDADE10`. Se for, aplica mais **10% de desconto**.
9. Calcula o valor final e o total de desconto concedido.
10. Guarda os valores bruto, final e o desconto de cada compra em **listas de histórico**.
11. Quando o usuário digita `0` no valor da compra, o programa encerra o cadastro.
12. Ao final, calcula a quantidade de compras, o total bruto, o total de descontos e o total arrecadado.
13. Exibe o **resumo no console** e salva o mesmo relatório no arquivo `resumo.txt`.

## Como rodar

Entre na pasta `nivel_1` pelo terminal e execute:

```bash
python3 pdv.py
```
## Tabela de testes 

![Tabela de teste do PDV](nivel_1 /imagem/tabela-teste.png)
