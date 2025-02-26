while(True):
    print('''------------------- BEM VINDO --------------------
        PROGRAMA ESTILO DE VIDA SAÚDAVEL''')
    
    print("OPÇÕES: \n 1 - Perfil do Usuário\n 2- Plano Alimenta com Base no IMC\n 3- Rotina de Exercicios com Base no IMC\n 4- Cadastrar Progresso\n 0- Sair")
    opcao = input("")

    if opcao == "1":
        usuarios = []
        
        novoUsuario = {
            "nome": input("Digite seu nome: "),
            "idade": int(input("Digite sua idade: ")),
            "sexo": input("Digite seu sexo: "),
            "peso": float(input("Digite seu peso: ")),
            "altura": input("Digite sua altura: "),
            "restricoesAlimentares": input("Digite suas restrições alimentares: "),
            "nivelAtividadeFisica": input("Digite seu nível de atividade fisica: ")
        }

        usuarios.append(novoUsuario)
        print(f"Usuário cadastrado com sucesso! {novoUsuario["nome"]}")

    elif opcao == "2":
        print("Digite seu IMC: ")
        imc = float(input(""))
        if imc < 18.5:
            print("Abaixo do peso")
        elif imc >= 18.5 and imc < 24.9:
            print("Peso normal")
        elif imc >= 25 and imc < 29.9:
            print("Sobrepeso")
        elif imc >= 30 and imc < 34.9:
            print("Obesidade Grau 1")
        elif imc >= 35 and imc < 39.9:
            print("Obesidade Grau 2")
        else:
            print("Obesidade Grau 3")


    elif opcao == "0":
        break
