#---------------------------------------Enunciado---------------------------------------------

#3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, 
# faça um programa, na linguagem que desejar, que calcule e retorne:
#   • O menor valor de faturamento ocorrido em um dia do mês;
#   • O maior valor de faturamento ocorrido em um dia do mês;
#   • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

#IMPORTANTE:
#a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
#b) Podem existir dias sem faturamento, como nos finais de semana e feriados. 
#Estes dias devem ser ignorados no cálculo da média;

#--------------------------------------Resposta------------------------------------------------

import json

#abrindo o arquivo json e inserindo numa variavel dados do tipo lista contendo dicionarios
# dados = [{'dia': 1, 'valor': y}, {'dia': 2, 'valor': z}...{'dia': 30, 'valor': w}]
with open('C:/Users/julia/Downloads/dados.json', 'r') as json_file:
    dados = json.load(json_file)

#transformando a lista de dicionarios em lista do tipo 'dict_values'
valorVec = []
for i in dados:
    valor = i.values()
    valorVec.append(valor)

#transformando a lista de 'dict_values' em numeros

numero= []
for i in valorVec:
    for j in i:
        numero.append(j)

#dividindo a lista em duas: dias e faturamentos (já retirando os dias com faturamento 0)

faturamento = []
dia = []
for i in numero:
    if (0<i<32):
        dia.append(i)
    elif (i>31):
        faturamento.append(i)

#operações com o faturamento
media = sum(faturamento)/len(faturamento)
maximo = max(faturamento)
minimo = min(faturamento)

#contagem dos dias com faturamento maior que a média
contaDias = 0
for i in faturamento:
    if (i > media):
        contaDias += 1

print(f"Valor médio: R$ {media:.2f}")
print(f"Valor máximo: R$ {maximo:.2f}")
print(f"Valor mínimo: R$ {minimo:.2f}")
print(f"Numero de dias com faturamento maior que a media: {contaDias}")


