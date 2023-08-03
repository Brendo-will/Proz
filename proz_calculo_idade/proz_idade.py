import datetime

def obter_ano_nascimento():
    while True:
        try:
            ano_nascimento = int(input("Digite o ano de nascimento (entre 1922 e 2021): "))
            if 1922 <= ano_nascimento <= 2021:
                return ano_nascimento
            else:
                print("Ano de nascimento inválido. Digite novamente.")
        except ValueError:
            print("Valor inválido. Digite novamente.")

def calcular_idade(ano_nascimento):
    ano_atual = datetime.datetime.now().year
    return ano_atual - ano_nascimento

def main():
    nome = input("Digite o seu nome completo: ")
    ano_nascimento = obter_ano_nascimento()
    idade = calcular_idade(ano_nascimento)

    print(f"Nome: {nome}")
    print(f"Idade em 2022: {idade}")

if __name__ == "__main__":
    main()
