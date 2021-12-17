def carrega_cidades():
    resultado = []
    with open('cidades.csv', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            uf, ibge, nome, dia, mes, pop = linha.split(';')
            resultado.append(
                (uf, int(ibge), nome, int(dia), int(mes), int(pop))
            )
    arquivo.close()
    return resultado


cidades = carrega_cidades()



mes=int(input('Informe um mês em números: '))
pop=int(input('Informe um valor populacional: '))
mesesup=('JANEIRO', 'FEVEREIRO', 'MARÇO', 'ABRIL', 'MAIO', 'JUNHO', 'JULHO', 'AGOSTO', 'SETEMBRO', 'OUTUBRO', 'NOVEMBRO', 'DEZEMBRO')
meseslow=('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')

print(f'CIDADES COM MAIS DE {pop} HABITANTES E ANIVERSÁRIO EM {mesesup[mes-1]}:')
for c in cidades:
    if c[4]==mes and c[5]>pop:
        print(f'{c[2]}({c[0]}) tem {c[5]} habitantes e faz aniversário em {c[3]} de {meseslow[mes-1]}.')
