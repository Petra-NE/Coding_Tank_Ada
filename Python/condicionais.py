#Estruturas condicionais

idade = 20

if idade >=18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")    


"""
    Imprimir "Aprovado(a), caso o estudante tenha uma média superior ou igual a 7, 
    e "Reprovado", caso a média seja inferior a 7.
    
"""
"""
media = float(input('Informe a media do estudante: '))

if media >= 7:
    print('Você foi aprovado')
elif media >=5:
    print('Você está em recuperação')
else:
    print('Você foi reprovado!')"""

    
media = 7
presença = 100

if media >=7 and presença >= 70:
    print('Aprovado!')
else:
    print('Reprovado')
