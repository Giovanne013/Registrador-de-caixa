def registrar_compra(compras): #função para definir produtos
    nome_produto = input("Digite o nome do produto:")#pegar nome do produto
    quantidade = int(input("Digite a quantidade comprada:"))#pegar quantidade comprada
    valor_unitario = float(input("Digite o valor unitário:"))#digitar o valor para cadastro
    compras.append({"nome_produto": nome_produto, "quantidade": quantidade, "valor_unitario": valor_unitario})
    print("Compra registrada com sucesso!")

def registrar_venda(vendas):# função para registrar as vendas.
    nome_produto = input("Digite o nome do produto:")
    quantidade = int(input("Digite a quantidade vendida:"))
    valor_unitario = float(input("Digite o valor unitário:"))
    vendas.append({"nome_produto": nome_produto, "quantidade": quantidade, "valor_unitario": valor_unitario})
    print("Venda registrada com sucesso!")

def verificar_saldo(compras, vendas):
    total_compras = sum([c["quantidade"] * c["valor_unitario"] for c in compras])
    total_vendas = sum([v["quantidade"] * v["valor_unitario"] for v in vendas])
    lucro = total_vendas - total_compras
    print(f"Saldo total das vendas: R$ {lucro:.2f}")

def main():
    compras = []
    vendas = []

    while True: # estrutura de repetição
        print("\nMenu:")
        print("1. Registrar uma compra")
        print("2. Registrar uma venda")
        print("3. Verificar o saldo total das vendas")
        print("4. Sair")

        opcao = input("Escolha uma opção (1-4): ")

        if opcao == "1":
            registrar_compra(compras)
        elif opcao == "2":
            registrar_venda(vendas)
        elif opcao == "3":
            verificar_saldo(compras, vendas)
        elif opcao == "4":
            print("Programa encerrado. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

