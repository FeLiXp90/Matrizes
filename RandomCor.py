import os
os.system('echo on')
from random import randrange
def limpaTela():
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')


def jogo():
	jogo=1
	while jogo==1:
		print('Bem vindo ao jogo\n O jogo é o seguinte, vou te passar uma sequencia e você tem que me dizer\n a sequencia de cores das palavras de antes mais a cor da palavra atual')
		print('\nAzul claro é ciano, alias\n\n')
		sequencia=''
		pontos= 0
		Cor='branco'
		fake=''
		while pontos<10:
			
			Random =(randrange(30, 37))

			if Random==30:
				Cor= "branco"
				fake= 'Preto'
			elif Random == 31: 
				Cor= "vermelho" 
				fake='roxo'
			elif Random == 32: 
				Cor= "verde"  
				fake='amarelo'
			elif Random == 33: 	
				Cor= "amarelo" 
				fake='ciano'
			elif Random == 34: 
				Cor= "azul" 
				fake='cinza'
			elif Random == 35: 
				Cor= "roxo" 
				fake='verde'
			elif Random == 36: 
				Cor= "ciano" 
				fake= 'vermelho'
			elif Random == 37: 
				Cor= "cinza" 
				fake= 'azul'
			Random=str(Random)
			sequencia=sequencia+Cor
			SequenciaRecebida=input('Cor atual:{}{}{}\n\nDigite a sequencia: '.format('\033[4;'+Random+'m',fake, '\033[m'))
			if SequenciaRecebida==sequencia:
				pontos=pontos+1
				print('acertou\nPróxima')
			else:
				print('Errooou,Mas pode continuar tentando\n')
		print('\n\nParabéns, ganhou o jogo!!!')
		jogo=0

jogo()
