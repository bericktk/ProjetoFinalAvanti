# Programa Estilo de Vida Saudável

## Descrição
Este é um programa em Python que auxilia os usuários a manter um estilo de vida saudável, fornecendo planos alimentares e rotinas de exercícios com base no Índice de Massa Corporal (IMC). O programa permite cadastrar usuários, acompanhar o progresso e visualizar perfis cadastrados.

## Funcionalidades
- Cadastro de usuários com nome, idade, peso, altura e atividades físicas.
- Cálculo do IMC e recomendação de planos alimentares adequados.
- Sugestões de rotinas de exercícios com base no IMC.
- Registro do progresso do usuário, incluindo peso e atividades físicas.
- Listagem de usuários cadastrados.

## Como Executar
1. Certifique-se de ter o Python instalado (versão 3.13.0 recomendada).
2. Baixe ou clone este repositório.
3. Execute o script no terminal ou prompt de comando:
   ```sh
   python main.py
   ```
4. Siga as instruções exibidas no terminal para interagir com o programa.

## Menu Principal
Ao iniciar o programa, o usuário verá as seguintes opções:
```
------------------- BEM VINDO --------------------
|        PROGRAMA ESTILO DE VIDA SAÚDAVEL         |
--------------------------------------------------

--------------------- OPÇÕES ---------------------
1- Perfil do Usuário
2- Plano Alimentar com Base no IMC
3- Rotina de Exercícios com Base no IMC
4- Cadastrar Progresso
5- Ver Usuários Cadastrados
0- Sair
--------------------------------------------------
```

## Fluxo do Programa
1. **Cadastro de Usuário:** O programa solicita informações como nome, idade, peso, altura, restrições alimentares e atividades físicas.
2. **Cálculo do IMC:** Com base nos dados informados, o programa calcula o IMC e sugere um plano alimentar.
3. **Rotina de Exercícios:** Sugestão de exercícios específicos conforme o IMC do usuário.
4. **Cadastro de Progresso:** Atualização de peso e inclusão de novas atividades físicas.
5. **Exibição de Usuários Cadastrados:** Lista todos os usuários registrados e suas informações.
6. **Saída:** O programa encerra a execução ao escolher a opção `0`.

## Exemplo de Uso
Exemplo de cálculo do IMC:
```
Digite seu nome: João
Digite seu peso: 70
Digite sua altura: 1.75
Seu IMC é: 22.86 e você está: Peso normal
Plano Alimentar para Manutenção de Peso:
- Café da Manhã: 1 copo de leite desnatado, 2 fatias de pão integral com queijo branco, 1 fruta (maçã ou pera)
...
```

## Requisitos
- Python 3.13.0

## Contribuição
Se deseja contribuir, faça um fork do repositório, crie uma branch com sua alteração e envie um pull request.

## Licença
Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---
# Este programa é um recurso educativo e não substitui aconselhamento profissional de nutricionistas ou educadores físicos.