
#-------------------------------------Enunciado----------------------------------------

#1) Observe o trecho de código abaixo:

#   int INDICE = 13, SOMA = 0, K = 0;
#   enquanto K < INDICE faça
#   {
#      K = K + 1;
#      SOMA = SOMA + K;
#   }
#imprimir(SOMA);

#Ao final do processamento, qual será o valor da variável SOMA?


#--------------------------------------Resposta-------------------------------------

def primeiroExercicio ():
    indice = 13
    soma = 0
    k = 0

    while (k < indice):
        k += 1
        soma += 1
    
    print(soma)

primeiroExercicio()

#De acordo com o enunciado, o resultado final será o número 13, onde K=13.