import random

def gerador_cpf(range_cpf):
    for _ in range(range_cpf):
        nove_digitos = ''
        for i in range(9):
            nove_digitos += str(random.randint(0, 9))

        contador_regressivo = 10
        resultado_1 = 0

        for digito in nove_digitos:
            resultado_1 += int(digito) * contador_regressivo
            contador_regressivo -= 1 

        primeiro_digito = (resultado_1 * 10) % 11

        if primeiro_digito > 9:
            primeiro_digito = 0

        cpf_com_digito = nove_digitos + str(primeiro_digito)

        contador_regressivo = 11
        resultado_2 = 0

        for digito in cpf_com_digito:
            resultado_2 += int(digito) * contador_regressivo
            contador_regressivo -= 1
            
        segundo_digito = (resultado_2 * 10) % 11

        if segundo_digito > 9:
            segundo_digito = 0

        cpf_gerado_pelo_calculo = f'{nove_digitos}{primeiro_digito}{segundo_digito}'

        print(cpf_gerado_pelo_calculo)

condicao = True
while condicao: 
    range_cpf = input('Quantos CPFs você quer gerar?: ')

    try:
        range_int = int(range_cpf)
        gerador_cpf(range_int)
        
        print('\nDeseja inserir mais CPFs?\n')
        opcao = input('[S]im ou [N]ão?: ')
        
        if opcao == 's' or opcao == 'S':
            condicao = True
        else:
            print('Encerrando programa...')
            condicao = False
    except:
        print('Por favor, insira um número inteiro.')