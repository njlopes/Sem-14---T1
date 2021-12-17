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



pop=int(input())
print(f'CIDADES COM MAIS DE {pop} HABITANTES:')
for c in cidades:
    if c[5]>pop:
        print(f'IBGE: {c[1]} - {c[2]}({c[0]}) - POPULAÇÃO: {c[5]}')
