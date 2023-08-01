def calculadora(num1, num2, operacao):
    if operacao == 1:  # Soma
        return num1 + num2
    elif operacao == 2:  # Subtração
        return num1 - num2
    elif operacao == 3:  # Multiplicação
        return num1 * num2
    elif operacao == 4:  # Divisão
        if num2 != 0:  # Verificar se o divisor não é zero
            return num1 / num2
        else:
            print("Erro: Divisão por zero não é permitida.")
            return 0
    else:
        print("Operação inválida. Escolha uma operação válida (1, 2, 3 ou 4).")
        return 0

# Solicitar os números e a operação ao usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = int(input("Digite o número da operação (1 para soma, 2 para subtração, 3 para multiplicação, 4 para divisão): "))

# Chamar a função calculadora e imprimir o resultado
resultado = calculadora(num1, num2, operacao)
print("O resultado da operação é:", resultado)

