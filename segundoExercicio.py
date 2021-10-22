#---------------------------Enunciado------------------------------------------

#2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será 
# a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), 
# escreva um programa na linguagem que desejar onde, informado um número, 
# ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o 
# número informado pertence ou não a sequência.

#IMPORTANTE:
#Esse número pode ser informado através de qualquer entrada de sua preferência ou pode 
# ser previamente definido no código;
#print("oi")

#--------------------------Resposta--------------------------------------------

def fibonacci ():
    anterior = 0
    proximo = 0
    numero = int(input("Digite o numero que gostaria de identificar se está na sequencia de Fibonacci: "))
    while(proximo <= numero):
        print(proximo)
        proximo = proximo + anterior
        anterior = proximo - anterior
        if(proximo == 0):
            proximo = proximo + 1
    if (anterior == numero):
        print(f"O numero {numero} pertence a sequencia de Fibonacci")
    else:
        print(f"O numero {numero} não pertence a sequencia de Fibonacci")

fibonacci()