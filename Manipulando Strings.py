#frase = 'Curso em Video Python'
#print(frase)
#print(frase[3])
#print(frase[3:13])
#print(frase[:13])
#print(frase[1:15]) #Imprime a frase da posição 1 a posição 15
#print(frase[1:15:2]) #da posição 1 até a posição 15 pulando de 2 em 2
#print(frase[1::2]) #da posição1 até o final pulando de 2 em 2
#print(frase.count('o')) #Conta quantos 'o' tem na frase
#print(frase.upper().count('O')) #Coloca a frase para maiúsculo
#print(len(frase)) #Quantas letras tem a frase
#print(frase.replace('Python','Android')) #Troca a palavra Python por Android
#print('Curso' in frase) #Existe a palavra Curso na frase?
#print(frase.lower().find('video')) #porque Lower coloca as letras para minúsculo

#nome = str(input('Digite seu nome completo:')).strip()
#print('Seu nome em letras maiúculas é: {} '.format(nome.upper()))
#print('Seu nome em letras minúsculas é : {} '.format(nome.lower()))
#print('Seu nome tem {} letras.'.format(len(nome)-nome.count(' ')))
#print(len(nome[0:6]))

# num = str(input("Digite um número de 0 a 9999: "))
# print('O número digitado foi: {}' .format(num))
# print('A unidade deste número é: {}'.format(num[3::]))
# print('A dezena deste número é: {}'.format(num[2:3]))
# print('A centena deste número é: {}'.format(num[1:2]))
# print('O milhar deste número é: {}'.format(num[0:1]))
#*Informar na tela do computador a unidade, dezena, centena e milhar de um numero, com String.


#*Informar na tela do computador a unidade, dezena, centena e milhar de um numero, com numeros inteiros.
# num = int(input('Digite um número de 0 a 9999:'))
# u = num // 1 % 10
# d = num // 10 % 10
# c = num // 100 % 10
# m = num // 1000 % 10
# print('unidade: {}'.format(u))
# print('dezena: {}'.format(d))
# print('centena: {}'.format(c))
# print('milhar: {}'.format(m))


#print('Curso' in frase) #Existe a palavra Curso na frase?
#print(frase.upper().count('O')) #Coloca a frase para maiúsculo

#cidade = str(input('Emque cidade você nasceu?')).strip() #*porque Strip elimina os espaços em branco
#print(cidade[0:5].upper()== 'SANTO') #porque Upper joga tudo para maiúsculo

#nome = str(input('Digite o seu nome completo:')).strip()
#print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper()))


#frase = str(input('Digite uma frase qualquer: ')).upper().strip()

#Quantas vezes aparece a letra "A"
#Em que posição ela aparece a primeira vez?
#Em que posição ela aparece a última vez?
#print(frase.upper().count('O')) #Coloca a frase para maiúsculo

#print('Na sua frase aparece {} vezes a letra A'.format(frase.count('A')))
#print('A primeira letra A aparece na posição {}'.format(frase.find('A')+1))
#print('A última letra A aparece na posição {}'.format(frase.rfind('A')+1))

#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último
#nome separadamente.
nome = str(input('Digite seu nome completo: ')).upper().strip()
n = nome.split()
print('Seu nome completo é: {}'.format(nome))
print('Seu primeiro nome é: {}'.format(n[0]))
print('Seu último nome é: {}'.format(n[len(n)-1]))
