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
	
