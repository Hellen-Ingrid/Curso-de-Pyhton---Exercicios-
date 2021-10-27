preço = float(input('Preço das compras: R$'))
print('Escolha uma das formas de pagamento abaixo:')
print('\033[31m[ 1 ]\033[m À vista dinheiro/cheque')
print('\033[31m[ 2 ]\033[m À vista no cartão')
print('\033[31m[ 3 ]\033[m 2x no cartão')
print('\033[31m[ 4 ]\033[m 3x ou mais no cartão')
escolha = int(input('Sua escolha: \033[31m'))
if escolha == 1:
    desconto = preço - (preço * 10 / 100)
    print('\033[mSua compra de R${:.2f} custará R${:.2f} no final'.format(preço, desconto))
elif escolha == 2:
    desconto = preço - (preço * 5 / 100)
    print('\033[mSua compra de R${:.2f} custará R${:.2f} no final'.format(preço, desconto))
elif escolha == 3:
    parcela = preço / 2
    print('\033[mValor da compra: R${:.2f}'.format(preço))
    print('Parcelamento: 2x de R${:.2f} SEM JUROS'.format(parcela))
elif escolha == 4:
    vezes = int(input('\033[mQuantas parcelas? '))
    parcela = preço / vezes 
    PJ = parcela + (parcela * 20 / 100)
    juros = preço + (preço * 20 / 100)
    print('Parcelamento: {}x de R${:.2f} COM JUROS'.format(vezes, PJ))
    print('Sua compra de R${:.2f} custará R${:.2f} no final'.format(preço, juros))
elif escolha > 4:
    print('\033[31mOPÇÃO INVÁLIDA de pagamento. Tente novamente!\033[m')
    print('Sua compra de R${:.2f} custará R${:.2f} no final'.format(preço, preço))