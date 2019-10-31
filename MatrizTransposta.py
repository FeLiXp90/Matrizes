#Ricardo


import random

def criaMatriztransposta(matOrigin):
	mat= []
	for i in range(len(matOrigin[0])):
		linha=[]
		for j in range(len(matOrigin)):
			linha.append(matOrigin[j][i])	
		mat.append(linha)
	for l in range(len(mat)):
		print (mat[l])
	return mat
	
matriz= [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
criaMatriztransposta(matriz)
