def verificar_categoria_habilitacao(rodas, peso, pessoas):
    if rodas == 2 or rodas == 3:
        return "Categoria A"
    elif rodas == 4 and pessoas <= 8 and peso <= 3500:
        return "Categoria B"
    elif rodas >= 4 and peso > 3500 and peso <= 6000:
        return "Categoria C"
    elif rodas >= 4 and pessoas > 8:
        return "Categoria D"
    elif rodas >= 4 and peso > 6000:
        return "Categoria E"
    else:
        return "Categoria não definida"

# Entrada de dados
quantidade_rodas = int(input("Digite a quantidade de rodas do veículo: "))
peso_bruto = float(input("Digite o peso bruto em quilogramas do veículo: "))
quantidade_pessoas = int(input("Digite a quantidade de pessoas no veículo: "))

# Verificar a categoria de habilitação
categoria = verificar_categoria_habilitacao(quantidade_rodas, peso_bruto, quantidade_pessoas)

# Exibir a categoria de habilitação
print("A melhor categoria de habilitação para o veículo informado é:", categoria)
