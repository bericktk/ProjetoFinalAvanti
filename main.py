usuarios = []

while(True):
    print('''
    ------------------- BEM VINDO --------------------
    |        PROGRAMA ESTILO DE VIDA SAÚDAVEL         |
    --------------------------------------------------
        ''')
    
    print('''
    --------------------- OPÇÕES ---------------------
    1- Perfil do Usuário
    2- Plano Alimentar com Base no IMC
    3- Rotina de Exercicios com Base no IMC
    4- Cadastrar Progresso
    5- Ver Usuários Cadastrados
    0- Sair
    --------------------------------------------------''')

    opcao = input("")

    if opcao == "1":
        print("VAMOS CRIAR SEU PERFIL\n")
        novoUsuario = {
            "nome": input("Digite seu nome: "),
            "idade": int(input("Digite sua idade: ")),
            "peso": float(input("Digite seu peso: ")),
            "altura": float(input("Digite sua altura: ")),
            "restricoesAlimentares": [],
            "atividadesFisicas": [],
            "planoAlimentar": [],
            "rotinaExercicios": []
        }

        atividades = input("Você pratica alguma atividade física? (s/n) ")
        if atividades == "s":
            qtdAtividades = int(input("Quantas atividades físicas você pratica? "))
            for i in range(qtdAtividades):
                atividade = input("Digite sua atividade física: ")
                novoUsuario["atividadesFisicas"].append(atividade)
            print("Atividades cadastradas com sucesso!")
        
        else:
            print("Sem atividades físicas cadastradas")

        restricoes = input("Você possui alguma restrição alimentar? (s/n) ")
        if restricoes == "s":
            qtdRestricoes = int(input("Quantas restrições alimentares você possui? "))
            for i in range(qtdRestricoes):
                restricao = input("Digite sua restrição alimentar: ")
                novoUsuario["restricoesAlimentares"].append(restricao)
            print("Restrições cadastradas com sucesso!")
        
        else:
            print("Sem restrições alimentares")

        usuarios.append(novoUsuario)
        print("----------------------------------------------------------------------------------")
        print(f"Usuário cadastrado com sucesso! {novoUsuario["nome"]}")
        print("----------------------------------------------------------------------------------")

    elif opcao == "2":
        nome = input("Digite seu nome: ")
        print("VAMOS CALCULAR SEU IMC\n")
        for usuario in usuarios:
            if usuario["nome"] == nome:
                peso = usuarios[0]["peso"]
                altura = usuarios[0]["altura"]
                imc = peso / (altura * altura)
                usuario["planoAlimentar"].append(imc)
                print(f"Seu IMC é: {imc:.2f} e você está:")

                if imc < 18.5:
                    print("Você está abaixo do peso\n\n")
                    print("Plano Alimentar para Ganho de Peso:")
                    print("Café da Manhã:")
                    print("- 1 copo de leite integral")
                    print("- 2 fatias de pão integral com manteiga")
                    print("- 1 fruta (banana ou maçã)")
                    print("\nLanche da Manhã:")
                    print("- 1 iogurte natural com granola")
                    print("\nAlmoço:")
                    print("- 1 porção de arroz integral")
                    print("- 1 porção de feijão")
                    print("- 1 filé de frango grelhado")
                    print("- Salada de folhas verdes com azeite")
                    print("- 1 fruta (laranja ou mamão)")
                    print("\nLanche da Tarde:")
                    print("- 1 sanduíche de pão integral com queijo e presunto")
                    print("- 1 suco natural de frutas")
                    print("\nJantar:")
                    print("- 1 porção de macarrão integral com molho de tomate")
                    print("- 1 porção de carne moída")
                    print("- Salada de legumes cozidos")
                    print("\nCeia:")
                    print("- 1 copo de leite integral ou iogurte")
                    print("- 1 fruta (pera ou uva)\n\n")

                elif imc >= 18.5 and imc < 24.9:
                    print("Peso normal\n\n")
                    print("Plano Alimentar para Manutenção de Peso:")
                    print("Café da Manhã:")
                    print("- 1 copo de leite desnatado")
                    print("- 2 fatias de pão integral com queijo branco")
                    print("- 1 fruta (maçã ou pera)")
                    print("\nLanche da Manhã:")
                    print("- 1 barra de cereal")
                    print("\nAlmoço:")
                    print("- 1 porção de arroz integral")
                    print("- 1 porção de feijão")
                    print("- 1 filé de peixe grelhado")
                    print("- Salada de folhas verdes com azeite")
                    print("- 1 fruta (laranja ou mamão)")
                    print("\nLanche da Tarde:")
                    print("- 1 iogurte desnatado")
                    print("\nJantar:")
                    print("- 1 porção de sopa de legumes")
                    print("- 1 porção de frango desfiado")
                    print("\nCeia:")
                    print("- 1 copo de leite desnatado\n\n")

                elif imc >= 25 and imc < 29.9:
                    print("Sobrepeso\n\n")
                    print("Plano Alimentar para Perda de Peso:")
                    print("Café da Manhã:")
                    print("- 1 copo de leite desnatado")
                    print("- 1 fatia de pão integral com queijo cottage")
                    print("- 1 fruta (maçã ou pera)")
                    print("\nLanche da Manhã:")
                    print("- 1 fruta (banana ou maçã)")
                    print("\nAlmoço:")
                    print("- 1 porção de arroz integral")
                    print("- 1 porção de feijão")
                    print("- 1 filé de frango grelhado")
                    print("- Salada de folhas verdes com azeite")
                    print("\nLanche da Tarde:")
                    print("- 1 iogurte desnatado")
                    print("\nJantar:")
                    print("- 1 porção de sopa de legumes")
                    print("- 1 porção de peixe grelhado")
                    print("\nCeia:")
                    print("- 1 copo de leite desnatado\n\n")

                elif imc >= 30 and imc < 34.9:
                    print("Obesidade Grau 1\n\n")
                    print("Plano Alimentar para Obesidade:")
                    print("Café da Manhã:")
                    print("- 1 copo de leite desnatado")
                    print("- 1 fatia de pão integral com queijo cottage")
                    print("- 1 fruta (maçã ou pera)")
                    print("\nLanche da Manhã:")
                    print("- 1 fruta (banana ou maçã)")
                    print("\nAlmoço:")
                    print("- 1 porção de arroz integral")
                    print("- 1 porção de feijão")
                    print("- 1 filé de frango grelhado")
                    print("- Salada de folhas verdes com azeite")
                    print("\nLanche da Tarde:")
                    print("- 1 iogurte desnatado")
                    print("\nJantar:")
                    print("- 1 porção de sopa de legumes")
                    print("- 1 porção de peixe grelhado")
                    print("\nCeia:")
                    print("- 1 copo de leite desnatado\n\n")

                elif imc >= 35 and imc < 39.9:
                    print("Obesidade Grau 2\n\n")
                    print("Plano Alimentar para Obesidade:")
                    print("Café da Manhã:")
                    print("- 1 copo de leite desnatado")
                    print("- 1 fatia de pão integral com queijo cottage")
                    print("- 1 fruta (maçã ou pera)")
                    print("\nLanche da Manhã:")
                    print("- 1 fruta (banana ou maçã)")
                    print("\nAlmoço:")
                    print("- 1 porção de arroz integral")
                    print("- 1 porção de feijão")
                    print("- 1 filé de frango grelhado")
                    print("- Salada de folhas verdes com azeite")
                    print("\nLanche da Tarde:")
                    print("- 1 iogurte desnatado")
                    print("\nJantar:")
                    print("- 1 porção de sopa de legumes")
                    print("- 1 porção de peixe grelhado")
                    print("\nCeia:")
                    print("- 1 copo de leite desnatado\n\n")

                else:
                    print("Obesidade Grau 3\n\n")
                    print("Plano Alimentar para Obesidade:")
                    print("Café da Manhã:")
                    print("- 1 copo de leite desnatado")
                    print("- 1 fatia de pão integral com queijo cottage")
                    print("- 1 fruta (maçã ou pera)")
                    print("\nLanche da Manhã:")
                    print("- 1 fruta (banana ou maçã)")
                    print("\nAlmoço:")
                    print("- 1 porção de arroz integral")
                    print("- 1 porção de feijão")
                    print("- 1 filé de frango grelhado")
                    print("- Salada de folhas verdes com azeite")
                    print("\nLanche da Tarde:")
                    print("- 1 iogurte desnatado")
                    print("\nJantar:")
                    print("- 1 porção de sopa de legumes")
                    print("- 1 porção de peixe grelhado")
                    print("\nCeia:")
                    print("- 1 copo de leite desnatado\n\n")

    elif opcao == "3":
        nome = input("Digite seu nome: ")
        for usuario in usuarios:
            if usuario["nome"] == nome:
                peso = usuarios[0]["peso"]
                altura = usuarios[0]["altura"]
                imc = peso / (altura * altura)
                usuario["rotinaExercicios"].append(imc)
                print("VAMOS CALCULAR SEU IMC\n")
                print(f"Seu IMC é: {imc:.2f} e você está:")

                if imc < 18.5:
                    print("Você está abaixo do peso\n\n")
                    print("Rotina de Treino para Ganho de Peso:")
                    print("Segunda-feira: Treino de Força")
                    print("- Agachamento: 3 séries de 8-12 repetições")
                    print("- Levantamento Terra: 3 séries de 8-12 repetições")
                    print("- Supino: 3 séries de 8-12 repetições")
                    print("- Remada Curvada: 3 séries de 8-12 repetições")
                    print("\nQuarta-feira: Treino de Força")
                    print("- Agachamento: 3 séries de 8-12 repetições")
                    print("- Levantamento Terra: 3 séries de 8-12 repetições")
                    print("- Supino: 3 séries de 8-12 repetições")
                    print("- Remada Curvada: 3 séries de 8-12 repetições")
                    print("\nSexta-feira: Treino de Força")
                    print("- Agachamento: 3 séries de 8-12 repetições")
                    print("- Levantamento Terra: 3 séries de 8-12 repetições")
                    print("- Supino: 3 séries de 8-12 repetições")
                    print("- Remada Curvada: 3 séries de 8-12 repetições\n\n")

                elif imc >= 18.5 and imc < 24.9:
                    print("Peso normal\n\n")
                    print("Rotina de Treino para Manutenção de Peso:")
                    print("Segunda-feira: Treino de Força")
                    print("- Agachamento: 3 séries de 8-12 repetições")
                    print("- Supino: 3 séries de 8-12 repetições")
                    print("- Remada Curvada: 3 séries de 8-12 repetições")
                    print("\nQuarta-feira: Treino de Cardio")
                    print("- Corrida: 30 minutos")
                    print("- Bicicleta: 30 minutos")
                    print("\nSexta-feira: Treino de Força")
                    print("- Agachamento: 3 séries de 8-12 repetições")
                    print("- Supino: 3 séries de 8-12 repetições")
                    print("- Remada Curvada: 3 séries de 8-12 repetições\n\n")

                elif imc >= 25 and imc < 29.9:
                    print("Sobrepeso\n\n")
                    print("Rotina de Treino para Perda de Peso:")
                    print("Segunda-feira: Treino de Cardio")
                    print("- Corrida: 30 minutos")
                    print("- Bicicleta: 30 minutos")
                    print("\nQuarta-feira: Treino de Força")
                    print("- Agachamento: 3 séries de 8-12 repetições")
                    print("- Supino: 3 séries de 8-12 repetições")
                    print("- Remada Curvada: 3 séries de 8-12 repetições")
                    print("\nSexta-feira: Treino de Cardio")
                    print("- Corrida: 30 minutos")
                    print("- Bicicleta: 30 minutos\n\n")

                elif imc >= 30 and imc < 34.9:
                    print("Obesidade Grau 1\n\n")
                    print("Rotina de Treino para Obesidade:")
                    print("Segunda-feira: Treino de Cardio")
                    print("- Caminhada: 30 minutos")
                    print("- Bicicleta: 30 minutos")
                    print("\nQuarta-feira: Treino de Força Leve")
                    print("- Agachamento: 3 séries de 8-12 repetições")
                    print("- Supino: 3 séries de 8-12 repetições")
                    print("- Remada Curvada: 3 séries de 8-12 repetições")
                    print("\nSexta-feira: Treino de Cardio")
                    print("- Caminhada: 30 minutos")
                    print("- Bicicleta: 30 minutos\n\n")

                elif imc >= 35 and imc < 39.9:
                    print("Obesidade Grau 2\n\n")
                    print("Rotina de Treino para Obesidade:")
                    print("Segunda-feira: Treino de Cardio")
                    print("- Caminhada: 30 minutos")
                    print("- Bicicleta: 30 minutos")
                    print("\nQuarta-feira: Treino de Força Leve")
                    print("- Agachamento: 3 séries de 8-12 repetições")
                    print("- Supino: 3 séries de 8-12 repetições")
                    print("- Remada Curvada: 3 séries de 8-12 repetições")
                    print("\nSexta-feira: Treino de Cardio")
                    print("- Caminhada: 30 minutos")
                    print("- Bicicleta: 30 minutos\n\n")

                else:
                    print("Rotina de Treino para Obesidade:")
                    print("Segunda-feira: Treino de Cardio")
                    print("- Caminhada: 30 minutos")
                    print("- Bicicleta: 30 minutos")
                    print("\nQuarta-feira: Treino de Força Leve")
                    print("- Agachamento: 3 séries de 8-12 repetições")
                    print("- Supino: 3 séries de 8-12 repetições")
                    print("- Remada Curvada: 3 séries de 8-12 repetições")
                    print("\nSexta-feira: Treino de Cardio")
                    print("- Caminhada: 30 minutos")
                    print("- Bicicleta: 30 minutos\n\n")

    elif opcao == "4":
        print('''
        -------------------- CADASTRO DE PROGRESSO --------------------
        1- Peso
        2- Atividade Física
        ''')

        opcao = input("")
        if(opcao == "1"):
            nome = input("Digite seu nome: ")
            for usuario in usuarios:
                if usuario["nome"] == nome:
                    peso = float(input("Digite seu peso atual: "))
                    usuario["peso"] = peso
                    print("Peso cadastrado com sucesso!")
                
                else:
                    print("Usuário não encontrado")

        elif(opcao == "2"):
            nome = input("Digite seu nome: ")
            for usuario in usuarios:
                if usuario["nome"] == nome:
                    qtdAtividades = int(input("Quantas atividades físicas você pratica? "))
                    for i in range(qtdAtividades):
                        atividade = input("Digite a atividade que deseja cadastrar: ")
                        usuario["atividadesFisicas"].append(atividade)
                    print("Atividades fisica cadastradas com sucesso!")
                
                else:
                    print("Usuário não encontrado")

    elif(opcao == "5"):
        print("Usuários Cadastrados:")
        for usuario in usuarios:
            print(f'''
            |----------------- USUÁRIO -----------------|
            | Nome: {usuario["nome"]} | 
            | Idade: {usuario["idade"]} | 
            | Peso: {usuario["peso"]} | 
            | Altura: {usuario["altura"]} | 
            | Restrições Alimentares: {usuario["restricoesAlimentares"]} | 
            | Atividades Físicas: {usuario["atividadesFisicas"]} |
            |--------------------------------------------|
            ''')

    elif opcao == "0":
        print("Saindo do programa...")
        print("Obrigado por usar nosso programa!")
        break
