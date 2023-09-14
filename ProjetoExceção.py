'''
1- Quais são os dados de entradas necessários?
Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja
entre 1922 e 2021.

2- O que devo fazer com estes dados?
A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou,
ou completará, no ano atual (2022).

3- Se existe restrições neste problema?
Caso o usuário não digite um número ou apareça um inválido no campo do ano,
o sistema informará o erro e continuará perguntando até que um valor correto seja
preenchido.

4- Qual é o resultado esperado?
Mostra para usuário o nome e a idade que completou, e caso aconteça erro no codigo ao 
digitar o programa informa ao usuário, e volta ao inicio.
'''
# Função para obter o ano de nascimento do usuário
def obter_ano_de_nascimento():
    while True:
        try:
            ano = int(input("Digite o seu ano de nascimento (entre 1922 e 2021): "))
            # Verifica se o ano está dentro do intervalo desejado
            if 1922 <= ano <= 2021:
                return ano
            else:
                print("Erro: Por favor, digite um ano entre 1922 e 2021.")
        except:
            print("Erro: Por favor, digite um número válido para o ano de nascimento.")

# Função para calcular a idade com base no ano de nascimento
def calcular_idade(ano_nascimento):
    ano_passado = 2022
    idade = ano_passado - ano_nascimento
    return idade

# Função principal do programa
nome = input("Insira o seu nome completo: ")
idade = calcular_idade(obter_ano_de_nascimento())  

    # Exibe o nome do usuário e a idade
print(f"{nome}, sua idade é {idade} anos em 2022.")


