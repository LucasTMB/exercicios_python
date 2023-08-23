import re
import sys

cpf_enviado = input('Insira o CPF: ')
cpf = re.sub(
    r'[^0-9]',
    '',
    cpf_enviado
)
entrada_e_sequencial = cpf == cpf[0] * len(cpf)

if entrada_e_sequencial:
    print('Você enviou dados sequenciais.')
    sys.exit()
    
nove_digitos = cpf[:9]

contador_regressivo_1 = 10
resultado_1 = 0

for digito in nove_digitos:
    resultado_1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1
    
digito_1 = (resultado_1 * 10) % 11

if digito_1 > 9:
    digito_1 = 0
    
print(f'O primeiro dígito é: {digito_1}')

cpf_com_digito = nove_digitos + str(digito_1)

contador_regressivo_2 = 11
resultado_2 = 0

for digito in cpf_com_digito:
    resultado_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1
    
digito_2 = (resultado_2 * 10) % 11

if digito_2 > 9:
    digito_2 = 0
    
print(f'O segundo dígito é: {digito_2}')

cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

if cpf == cpf_gerado_pelo_calculo:
    print(f'O CPF {cpf_enviado} é válido!')
else:
    print(f'O CPF {cpf_enviado} é inválido.')