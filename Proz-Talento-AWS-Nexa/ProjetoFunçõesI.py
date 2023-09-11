'''
Problema: João precisa calcular seu Índice de Massa Corporal (IMC)
para avaliar seu peso ideal. Sabendo que a fórmula para calcular o
IMC é: peso ÷ altura², crie um programa que calcule e informe a classificação do IMC.
'''
def calcular_imc(peso, altura):
    imc = peso/(altura*altura)
    if (imc <= 18.5): return 'Magreza'
    elif(imc > 18.5) and (imc <= 24.9): return 'Saudavel'
    elif(imc >= 25) and (imc <= 29.9): return 'Sobrepeso'
    elif(imc > 30) and (imc <= 34.9): return 'Obesidade 1°'
    elif(imc > 35) and (imc <= 39.9): return 'Obesidade severa 2°'
    else: return 'Obesidade morbida 3°'

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

resultado = calcular_imc(peso, altura)
print(resultado)


def aprovacao(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3)/3
    if (media >= 7):
     res = 'Aprovado'
    else:
       res = 'Reprovado'
    return res

media = aprovacao(5, 4, 3)
print(media)

def operacao(num_lim, incre):
   contador = 0
   for i in range(0, num_lim, incre):
      contador = contador + 1
      return contador
   
   
num_lim = operacao(1, 10)
print(num_lim)




