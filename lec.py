import math

# Rodar o seguinte comando após modificaçoes no codigo:
# pyinstaller --onefile lec.py
# Isso ira gerar um novo executavel em /dist/lec

nomeProduto = input("Informe o nome do produto: ")

custoPedido = float(input("Custo de pedido (R$): "))
demanda = float(input("Demanda anual: "))
custoManutencao = float(input("Custo de armazenamento por unidade por ano (R$): "))

lec = math.sqrt((2*custoPedido*demanda) / custoManutencao)

print(f"A quantidade economica para {nomeProduto} é de aproximadamente {int(lec)} unidades")
