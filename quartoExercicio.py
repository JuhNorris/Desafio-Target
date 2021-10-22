#---------------------------------------Enunciado---------------------------------------------

#4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:

#SP – R$67.836,43
#RJ – R$36.678,66
#MG – R$29.229,88
#ES – R$27.165,48
#Outros – R$19.849,53

#Escreva um programa na linguagem que desejar onde calcule o percentual de representação 
# que cada estado teve dentro do valor total mensal da distribuidora.


#--------------------------------------Resposta------------------------------------------------

def faturamento ():
    sp = 67836.43
    rj = 36678.66
    mg = 29229.88
    es = 27165.48
    outros = 19849.53

    total = sp + mg + rj + es + outros
    print (f"O valor total foi de {total}")

    def percentual (estado, total):
        percentualEstado = (estado*100) / total
        return percentualEstado

    percentualSP = percentual(sp, total)
    percentualRJ = percentual(rj, total)
    percentualMG = percentual(mg, total)
    percentualES = percentual(es, total)

    print(f"O percentual de SP foi de {percentualSP:.1f}%.")
    print(f"O percentual de RJ foi de {percentualRJ:.1f}%.")
    print(f"O percentual de MG foi de {percentualMG:.1f}%.")
    print(f"O percentual de ES foi de {percentualES:.1f}%.")

faturamento()

    
    


