tarefas =[]

while True:
    print("\n1 - Adicionar tarefa")
    print("2 - Ver tarefas")
    print ("3 - Remover tarefa")
    print("4 - Sair")

    opcao = input("Escolha uma opção:")

    if opcao == "1":
        tarefa = input("Digite a tarefa:")
        tarefas.append(tarefa)
        print("Tarefa adicionada!")

    elif opcao == "2":
        print("\nLista de tarefas:")
        for i , t in enumerate(tarefas):
            print(f"{i} - {t}")

    elif opcao == "3":
        indice = int(input("Digite o numero da tarefa a ser removida:"))
        if 0 <= indice < len(tarefas):
            tarefas.pop(indice)
            print("Tarefa removida!")
        else:
            print("Indice inválido.")

    elif opcao == "4":
        print("Saindo...")
        break

    else:
        print("Opção inválida tente novamente.")