def voto(ano):	
	from datetime import date
	idade = date.today().year - ano
	if 65 > idade >= 18:
		return f'Com {idade} anos: VOTO OBRIGATÓRIO.'
	elif 15 < idade < 18 or idade >= 65:
		return f'Com {idade} anos: VOTO OPCIONAL.'
	elif idade <= 15:
		return f'Com {idade} anos: VOTO PROIBIDO.'


# Programa Principal
nasc = int(input('Ano de Nascimento: '))
print(voto(nasc))
