n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1+n2) / 2
print(f'Média: {media:.1f}')
if media < 5:
    print('REPROVADO')
elif 5.0 <= media < 7:
    print('RECUPERAÇÃO')
else:
    print('APROVADO')
