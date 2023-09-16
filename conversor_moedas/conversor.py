def conversor(opcao):
    valor_convertido = 0
    menu_valor = True
    
    while menu_valor:
        valor = input('\nInforme o valor a ser convertido: ')
    
        try:
            valor_float = float(valor)
            
            if valor_float > 0:
                if opcao == 1:
                    valor_convertido = valor_float * 0.19
                    return f'R$ {valor_float} equivale a USD {round(valor_convertido, 2)}'
                elif opcao == 2:
                    valor_convertido = valor_float * 0.18
                    return f'R$ {valor_float} equivale a € {round(valor_convertido, 2)}'
                elif opcao == 3:
                    valor_convertido = valor_float / 5.17
                    return f'USD {valor_float} equivale a R$ {round(valor_convertido, 2)}'
                elif opcao == 4:
                    valor_convertido = valor_float * 5.61
                    return f'€ {valor_float} equivale a R$ {round(valor_convertido, 2)}'
                elif opcao == 5:
                    valor_convertido = valor_float * 0.85
                    return f'USD {valor_float} equivale a € {round(valor_convertido, 2)}'
                elif opcao == 6:
                    valor_convertido = valor_float * 1.18
                    return f'€ {valor_float} equivale a USD {round(valor_convertido, 2)}'
                    
                menu_valor = False
            else:
                print('[ERRO] Insira um valor maior que zero.')
        except:
            print('[ERRO] Isso não é um valor válido.')

menu = True
while menu:
    print("\nMenu de conversão de moedas\n")
    
    print("1. REAL para DOLAR")
    print("2. REAL para EURO")
    print("3. DOLAR para REAL")
    print("4. EURO para REAL")
    print("5. DOLAR para EURO")
    print("6. EURO para DOLAR")
    
    print("0. Sair")
    
    opcao = input('\nEscolha uma opção: ')
    
    try:
        opcao_int = int(opcao)
        
        if opcao_int in [1, 2, 3, 4, 5, 6]:
            print(conversor(opcao_int))
        elif opcao_int == 0:
            print('Saindo...')
            menu = False
        else:
            print('Escolha uma opção válida!')
    except:
        print('[ERRO] Isso não é um número inteiro. Insira uma opção válida!')