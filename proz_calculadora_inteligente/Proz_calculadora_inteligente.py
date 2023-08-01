def calculadora_inteligente():
    while True:
        print("Operações disponíveis:")
        print("1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("0: Sair")

        operacao = int(input("Digite o número para realizar a operação: "))

        if operacao == 0:
            print("Encerrando a calculadora.")
            break
        elif operacao not in [1, 2, 3, 4]:
            print("Essa opção não existe.")
        else:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if operacao == 1:  # Soma
                resultado = num1 + num2
                print("Resultado da soma:", resultado)
            elif operacao == 2:  # Subtração
                resultado = num1 - num2
                print("Resultado da subtração:", resultado)
            elif operacao == 3:  # Multiplicação
                resultado = num1 * num2
                print("Resultado da multiplicação:", resultado)
            elif operacao == 4:  # Divisão
                if num2 != 0:
                    resultado = num1 / num2
                    print("Resultado da divisão:", resultado)
                else:
                    print("Erro: Divisão por zero não é permitida.")
            print("\n")  # Mostra uma linha em branco após o resultado

# Executar a calculadora
calculadora_inteligente()


