import math


def calcular_lec(demanda_anual, custo_pedido, custo_manutencao):
    return math.sqrt((2 * custo_pedido * demanda_anual) / custo_manutencao)


while True:
    try:
        print("")
        nome_produto = input("Informe o nome do produto: ")

        demanda_anual = float(input("Demanda anual: "))
        custo_pedido = float(input("Custo de pedido(R$): "))
        custo_manutencao = float(input("Custo de armazenamento por unidade(R$): "))

        lec = calcular_lec(demanda_anual, custo_pedido, custo_manutencao)

        print("=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=")
        print(f"A quantidade economica para {nome_produto} é de aproximadamente {int(lec)} unidades")
        print("")
        print("=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=")
        print("")

        continuar = input("Deseja calcular o LEC de outro produto?[s/n] ")

        if continuar.startswith("n"):
            break
    except ValueError:
        print("")
        print("Erro! Por favor, insira os dados corretamente.")
