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
#Nesta função calculadora foi utilizado as estrutura condicional para qual opção o usuário vai escolher o operador.
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
        return '0'

#Aqui no main o teste aparece para o usuário.
numero1 = 10
numero2 = 5
operador = '+'

resultado = calculadora(numero1, numero2, operador)
print(resultado)

    
