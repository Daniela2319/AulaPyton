'''
Faça uma função calculadora de dois números com três parâmetros: 
os dois primeiros serão os números da operação e o terceiro será a 
entrada que definirá a operação a ser executada. Considera a seguinte definição:
1. Soma
2. Subtração
3. Multiplicação
4. Divisão

Caso seja inserido um número de operação que não exista, o resultado deverá ser 0.
'''
def calculadora(num1, num2, operador):
    if operador == '+':
        return num1 + num2
    elif operador == '-':
        return num1 - num2
    elif operador == '*':
        return num1 * num2
    elif operador == '/':
        return num1 / num2
    else:
        return 'Operador inválido'

numero1 = float(input('Digite o numero: '))
numero2 = float(input('Digite o numero: '))
operador = input('Digite o numero:(+, -, *, /) ')

resultado = calculadora(numero1, numero2, operador)
print(resultado)

    
