ano = int(input('Digite o ano para descobrir se ele é um ano bissexto ou não:'))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é um ano bissexto!'.format(ano))
else:
    print('O ano {} não é bissexto.'.format(ano))
