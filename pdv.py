# Listas para guardar o histórico do dia
historico_bruto = []
historico_final = []
historico_descontos = []

print("=== SISTEMA DE CAIXA INICIADO ===")
print("(Digite 0 no valor da compra para encerrar e ver o resumo)\n")

while True:
    # 1. Entrada e Validação do Valor da Compra
    try:
        valor_bruto = float(input("Digite o valor da compra em reais: R$ "))
    except ValueError:
        print("Erro: Digite apenas números válidos (use ponto para decimais, ex: 50.50).\n")
        continue
    
    if valor_bruto == 0:
        break  # Encerra o loop se o valor for 0
        
    if valor_bruto < 0:
        print("Erro: O valor da compra não pode ser negativo. Tente novamente.\n")
        continue

    # 2. Entrada e Validação da Quantidade de Itens
    try:
        quantidade = int(input("Digite a quantidade de itens: "))
    except ValueError:
        print("Erro: A quantidade deve ser um número inteiro válido.\n")
        continue
        
    if quantidade <= 0:
        print("Erro: A quantidade deve ser maior que zero. Tente novamente.\n")
        continue

    # 3. Entrada e Validação da Idade
    try:
        idade = int(input("Digite a idade do cliente: "))
    except ValueError:
        print("Erro: A idade deve ser um número inteiro válido.\n")
        continue
    
    if idade < 0:
        print("Erro: A idade não pode ser negativa. Tente novamente.\n")
        continue

    # 4. Entrada do Cupom de Fidelidade
    cupom = input("Digite o cupom de fidelidade (Deixe em branco se não houver): ").strip().upper()

    # --- PROCESSAMENTO DOS DESCONTOS SEQUENCIAIS ---
    valor_atual = valor_bruto

    # Regra 1: Desconto por idade (65 anos ou mais = 20% de desconto)
    if idade >= 65:
        valor_atual = valor_atual * 0.80

    # Regra 2: Desconto por valor acumulado (Maior que R$ 100 = +10% de desconto)
    if valor_atual > 100:
        valor_atual = valor_atual * 0.90

    # Nova Regra 3: Desconto por quantidade (Mais que 3 itens = +5% de desconto)
    if quantidade > 3:
        valor_atual = valor_atual * 0.95

    # Nova Regra 4: Cupom de fidelidade (+10% de desconto se for "FIDELIDADE10")
    if cupom == "FIDELIDADE10":
        valor_atual = valor_atual * 0.90

    valor_final = valor_atual
    desconto_concedido = valor_bruto - valor_final

    # Exibição do resultado da compra atual
    print(f"Valor final desta compra: R$ {valor_final:.2f}\n")

    # Salvando os dados no histórico (append)
    historico_bruto.append(valor_bruto)
    historico_final.append(valor_final)
    historico_descontos.append(desconto_concedido)

# --- GERANDO O RESUMO E SALVANDO NO ARQUIVO ---
total_compras = len(historico_bruto)
soma_bruto = sum(historico_bruto)
soma_descontos = sum(historico_descontos)
soma_final = sum(historico_final)

# Criando o conteúdo do texto do resumo
linhas_resumo = [
    "================ RESUMO DO DIA ================\n",
    f"Quantidade de compras registradas : {total_compras}\n",
    f"Total bruto (sem descontos)        : R$ {soma_bruto:.2f}\n",
    f"Total de descontos concedidos     : R$ {soma_descontos:.2f}\n",
    f"Total final arrecadado            : R$ {soma_final:.2f}\n",
    "===============================================\n",
    "\n--- DETALHES POR COMPRA ---\n"
]

# Usando um loop 'for' para listar cada compra realizada no histórico
for i in range(total_compras):
    detalhe = f"Compra #{i+1} | Bruto: R$ {historico_bruto[i]:.2f} | Desconto: R$ {historico_descontos[i]:.2f} | Final: R$ {historico_final[i]:.2f}\n"
    linhas_resumo.append(detalhe)

# Exibindo o resumo no console
print("\n")
for linha in linhas_resumo:
    print(linha, end="")

# Gravando tudo no arquivo resumo.txt usando open(..., "w")
with open("resumo.txt", "w", encoding="utf-8") as arquivo:
    for linha in linhas_resumo:
        arquivo.write(linha)

print("\n[Sucesso] O programa foi encerrado e o relatório foi salvo em 'resumo.txt'!")
