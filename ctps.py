cadastro = {}

cadastro["Nome"] = str(input("Nome: ")).capitalize()
ano_nascimento = int(input("Ano de Nascimento: "))
idade = 2024 - ano_nascimento
cadastro["Idade"] = idade
cadastro["Ctps"] = int(input("Carteira de Trabalho (0 não tem): "))
if cadastro["Ctps"] != 0:
    cadastro["Ano Contratação"] = int(input("Ano de Contração: "))
    cadastro["Salário"] = float(input("Salário: R$"))
    cadastro["Aposentadoria"] = idade + (cadastro["Ano Contratação"] + 35) - 2024
    for k, v in cadastro.items():
        print(f"{k}: {v}")
else:
    for k, v in cadastro.items():
        print(f"{k}: {v}")
