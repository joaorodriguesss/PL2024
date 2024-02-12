import os
from Entrada import Entrada

os.chdir("C:/Users/35193/Desktop/3ANO_2S/PL/Sets")

with open("emd.csv", "r", encoding="utf-8") as file:
    lines = file.readlines()

# saltar a primeira linha
header = lines.pop(0)

listaEntradas = []
listaModalidades = []
nr_aptos = 0
nr_inaptos = 0
distribuicao_por_escalao = {}

for line in lines:
    tokens = line.split(",")
    id = tokens[0]
    index = tokens[1]
    dataEMD = tokens[2]
    primeiro_nome = tokens[3]
    ultimo_nome = tokens[4]
    idade = int(tokens[5])
    genero = tokens[6]
    morada = tokens[7]
    modalidade = tokens[8]
    clube = tokens[9]
    email = tokens[10]
    federado = tokens[11]
    resultado = tokens[12]

    entrada = Entrada(id,index,dataEMD,primeiro_nome,ultimo_nome,idade,genero,morada,modalidade,clube,email,federado,resultado)

    listaEntradas.append(entrada)

for e in listaEntradas:
    if e.modalidade not in listaModalidades:
        listaModalidades.append(e.modalidade)

    if e.resultado.strip() == "true":
        nr_aptos += 1
    if e.resultado.strip() == "false":
        nr_inaptos += 1

    escalao_etario = e.idade // 5 * 5  # Calcula o escalão etário arredondando para baixo
    chave = f"[{escalao_etario}-{escalao_etario + 4}]"  # Cria a chave do dicionário com o intervalo de idade
    if chave not in distribuicao_por_escalao:
        distribuicao_por_escalao[chave] = 0
    distribuicao_por_escalao[chave] += 1
    
print(f"APTOS: {nr_aptos} , N_APTOS: {nr_inaptos}")

# modalidades
listaModalidades_ordenada = sorted(listaModalidades)
print(f"Lista de Modalidades ordenada: {', '.join(listaModalidades_ordenada)}")

# aptos
nr_total_participantes = nr_aptos + nr_inaptos
percentagem_aptos = (nr_aptos / nr_total_participantes) * 100
percentagem_inaptos = (nr_inaptos / nr_total_participantes) * 100

print(f"Percentagem de Atletas Aptos: {percentagem_aptos} %")
print(f"Percentagem de Atletas Inaptos: {percentagem_inaptos} %")
    
# escalao
for chave, num_entradas in distribuicao_por_escalao.items():
    print(f"Escalão etário {chave}: {num_entradas} entradas")