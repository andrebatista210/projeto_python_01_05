import csv

caminho: str = "../arquivos/transacoes_estudo.csv"

arquivo_csv: list = []

# with open(file=caminho, mode='r', encoding= 'utf-8') as arquivo:
#     leitor_csv = csv.reader(arquivo)
#     cabecalho = next(leitor_csv)  # Lê a primeira linha (cabeçalho)
#     print("Cabeçalho:", cabecalho)

#     # Lendo as linhas do arquivo
#     for linha in leitor_csv:
#         print(linha)  # Cada linha é uma lista


with open(file=caminho, mode="r", encoding="utf-8") as arquivo:
    leitor_csv = csv.DictReader(arquivo)
    for linha in leitor_csv:
        arquivo_csv.append(linha)
        # print(f"ID: {linha['ID_Transacao']}, Categoria: {linha['Categoria']}, Valor: {linha['Valor']}")
print(arquivo_csv)
