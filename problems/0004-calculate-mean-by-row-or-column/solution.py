def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	res = []
	n_cols, n_rows = len(matrix[0]), len(matrix)
	if mode == 'row':
		for row in matrix:
			res.append(sum(row)/len(row))
	else:
		for i in range(n_cols):
			local_sum = 0
			for j in range(n_rows):
				local_sum += matrix[j][i]
			res.append(local_sum/n_rows)
	return res