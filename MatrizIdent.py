#Ricardo


import random

def criaMatrizIdent():
	xMatriz= int(input('Digite a quantidade de linhas e colunas:'))
	mat= []
	for i in range(xMatriz):
		linha=[]
		for j in range(xMatriz):
			if j==i:
				linha.append(1)
			else:			
				linha.append(0)	
		mat.append(linha)
	for l in range(len(mat)):
		print (mat[l])
	return mat
	
x=criaMatrizIdent()
