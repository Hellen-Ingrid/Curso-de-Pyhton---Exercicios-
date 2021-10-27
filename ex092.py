from datetime import date
pessoa = {}
pessoa['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
pessoa['idade'] = date.today().year - nasc
pessoa['ctpf'] = int(input('Carteira de trabalho (0 para nenhum): '))
if pessoa['ctpf'] != 0:
	pessoa['contratação'] = int(input('Ano de contratação: '))
	pessoa['salário'] = float(input('Salário: R$'))
	pessoa['aposentadoria'] = pessoa['contratação'] + 35 - nasc
print(20*'<>')
for k, v in pessoa.items():
	print(f' -- {k} tem o valor {v}')
