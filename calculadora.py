from math import sqrt


def raiz_quad(a):
    return sqrt(a)


def factorial(num):
    final = 1
    for i in range(num):
        final *= num - i
    return final


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
        return "Erro! Divisão por zero."


def exibir_calculadora():
    print(" _____________________")
    print("|  _________________  |")
    print("| | PythonCalc  Arc | |")
    print("| |_________________| |")
    print("|  ___ ___ ___   ___  |")
    print("| | 7 | 8 | 9 | | + | |")
    print("| |___|___|___| |___| |")
    print("| | 4 | 5 | 6 | | - | |")
    print("| |___|___|___| |___| |")
    print("| | 1 | 2 | 3 | | x | |")
    print("| |___|___|___| |___| |")
    print("| | . | 0 | = | | ÷ | |")
    print("| |___|___|___| |___| |")
    print("|_____________________|")


def exibir_menu():
    exibir_calculadora()
    print("\nEscolha uma operação:")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Factorial")
    print("6. Raíz Quadrada")
    print("7. Sair")


while True:
    exibir_menu()
    escolha = input("Escolha uma opção (1-7): ")

    if escolha == "7":
        print("Obrigado por usar a calculadora!")
        break

    if escolha in ["1", "2", "3", "4", "5", "6"]:
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Por favor, insira apenas números.")
            continue

        if escolha == "1":
            print("Resultado:", somar(num1, num2))
        elif escolha == "2":
            print("Resultado:", subtrair(num1, num2))
        elif escolha == "3":
            print("Resultado:", multiplicar(num1, num2))
        elif escolha == "4":
            print("Resultado:", dividir(num1, num2))
        elif escolha == "5":
            print("Resultado 1:", factorial(num1))
            print("Resultado 2:", factorial(num2))
        elif escolha == "6":
            print("Resultado 1:", raiz_quad(num1))
            print("Resultado 2:", raiz_quad(num2))
    else:
        print("Opção inválida! Tente novamente.")
