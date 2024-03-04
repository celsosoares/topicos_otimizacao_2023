import math

def calcular_lec(demanda_anual, custo_pedido, custo_manutencao):
    if demanda_anual <= 0 or custo_pedido <= 0 or custo_manutencao <= 0:
        raise ValueError("Todos os valores devem ser maiores que zero.")
    return math.sqrt((2 * custo_pedido * demanda_anual) / custo_manutencao)

while True:
    try:
        print("")
        nome_produto = input("Informe o nome do produto: ")

        demanda_anual = float(input("Demanda anual: "))
        custo_pedido = float(input("Custo de pedido(R$): "))
        custo_manutencao = float(input("Custo de armazenamento por unidade(R$): "))

        lec = calcular_lec(demanda_anual, custo_pedido, custo_manutencao)

        print("=" * 70)
        print(f"A quantidade economica para {nome_produto} é de aproximadamente {int(lec)} unidades")
        print("=" * 70)

        continuar = input("Deseja calcular o LEC de outro produto?[s/n] ").strip().lower()
        while continuar not in ('s', 'n'):
            print("Por favor, responda apenas com 's' para sim ou 'n' para não.")
            continuar = input("Deseja calcular o LEC de outro produto? [s/n] ").strip().lower()

        if continuar == "n":
            break
    except ValueError as ve:
        print("")
        print(f"\nErro: {ve}. Por favor, insira os dados corretamente.")