tabela = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio',
	         'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
          'Atlético MG', 'Botafogo', 'Atlético PR', 'Bahia',
          'São Paulo', 'Fluminense', 'Sport Recife', 'EC Vitória',
          'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético GO')
print(40*'-')
print(f'Os cinco primeiros colocados são: {tabela[0:5]}')
print(f'Os últimos quatro colocados da tabela são: {tabela[16:]}')
print(f'Tabela em ordem Alfabética: {sorted(tabela)}')
print(f'A Chapecoense está na {tabela.index("Chapecoense") + 1}ª posição')
