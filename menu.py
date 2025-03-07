def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Não é possível dividir por zero!"

def menu():
    while True:
        print("\nEscolha uma operação:")
        print("1. Somar")
        print("2. Subtrair")
        print("3. Multiplicar")
        print("4. Dividir")
        print("0. Sair")

        escolha = input("Digite o número da operação desejada: ")

        if escolha == '0':
            print("Saindo do programa.")
            break

        elif escolha in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
            except ValueError:
                print("Por favor, insira números válidos.")
                continue

            if escolha == '1':
                print(f"O resultado da soma é: {somar(num1, num2)}")
            elif escolha == '2':
                print(f"O resultado da subtração é: {subtrair(num1, num2)}")
            elif escolha == '3':
                print(f"O resultado da multiplicação é: {multiplicar(num1, num2)}")
            elif escolha == '4':
                print(f"O resultado da divisão é: {dividir(num1, num2)}")
        else:
            print("Opção inválida. Tente novamente.")

menu()
