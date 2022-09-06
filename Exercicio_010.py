bordas = '\033[037m-=-\033[m' * 12
print(bordas)
print('{:^35}'.format('CONVERSOR DE MOEDAS'))
print(bordas)
print()
real = float(input('Digite o valor (em reais) a ser convertido: R$ '))
print(bordas)
print('USD -> Para converter para dólar')
print('EUR -> Para converter para euro')
print('JPY -> Para converter para iene')
print(bordas)

# Valores não atualizados

while True:
    convert = input('Digite a opção desejada: ').strip().upper()
    match convert:
        case 'USD':
            print(f'\nO valor corresponde a ${(real/5.54):.2f}')
            break
        case 'EUR':
            print(f'\nO valor corresponde a €{(real/6.34):.2f}')
            break
        case 'JPY':
            print(f'\nO valor corresponde a ¥{(real/0.048):.2f}')
            break
        case _:
            print('Por favor digite uma opção válida!')
