'''
Faça uma função calculadora que os números e as operações serão feitas pelo usuário.
 O código deve ficar rodando infinitamente até que o usuário escolha a opção de sair.
 No início, o programa mostrará a seguinte lista de operações:

1: Soma
2: Subtração
3: Multiplicação
4: Divisão
0: Sair

Digite o número para a operação correspondente e caso o usuário introduza qualquer outro,
 o sistema deve mostrar a mensagem “Essa opção não existe” e voltar ao menu de opções.

Após a seleção, o sistema deve pedir para o usuário inserir o primeiro e segundo valor,
 um de cada. Depois precisa executar a operação e mostrar o resultado na tela.
   Quando o usuário escolher a opção “Sair”, o sistema irá parar.

É necessário que o sistema mostre as opções sempre que finalizar uma operação e 
mostrar o resultado. 
'''


def calculadora():
  while True: # laço infinito
    print("1: Soma")
    print("2: Subtração")
    print("3: Multiplicação")
    print("4: Divisão")
    print("0: Sair")

    opcao = int(input("Digite o número para a operação: "))
    if opcao == 0: # sair do programa
      break

    elif opcao == 1: # soma
      numero1 = float(input("Digite o primeiro número: "))
      numero2 = float(input("Digite o segundo número: "))
      resultado = numero1 + numero2
      print(f"A soma é:  {resultado}")

    elif opcao == 2: # subtração
      numero1 = float(input("Digite o primeiro número: "))
      numero2 = float(input("Digite o segundo número: "))
      resultado = numero1 - numero2
      print(f"A subtração é: {resultado}")

    elif opcao == 3: # multiplicação
      numero1 = float(input("Digite o primeiro número: "))
      numero2 = float(input("Digite o segundo número: "))
      resultado = numero1 * numero2
      print(f"A multiplicação é: {resultado}")

    elif opcao == 4: # divisão
      numero1 = float(input("Digite o primeiro número: "))
      numero2 = float(input("Digite o segundo número: "))
      resultado = numero1 / numero2
      print(f"A divisão é: {resultado}")

    else: # opção inválida
      print("Essa opção não existe")

resultado = calculadora()
print(calculadora)