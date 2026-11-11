while True:
    print("=========================")
    n1 = int(input("Digite o primeiro número: "))
    print("=========================")
    n2 = int(input("Digite o segundo número: "))

    while True:
        print("=========================")
        multi = int(input("1 - Soma\n" 
        "2 - Subtração\n"
        "3 - Multiplicação\n"
        "4 - Divisão\n"
        "5 - Sair\n"
        "Escolha uma das opção: "))

    
        if multi == 1:
            n3 = n1 + n2
        elif multi == 2:
            n3 = n1 - n2
        elif multi == 3:
            n3 = n1 * n2
        elif multi == 4:
            n3 = n1 / n2
        elif multi == 5:
         break
        else:
            print("\nNão existe essa opção\n")
            continue
        break
    print("=========================")
    print(f"O Resultado é: {n3}")