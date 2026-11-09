import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	n_cols, n_rows = len(a[0]), len(a)
	if n_cols*n_rows != new_shape[0]*new_shape[1]:
		return []
	res = [[0]*new_shape[1] for i in range(new_shape[0])]
	for i in range(n_rows):
		for j in range(n_cols):
			number = i*n_cols+j
			new_i = number//new_shape[1]
			new_j = number%new_shape[1] 
			res[new_i][new_j] = a[i][j]
	return res