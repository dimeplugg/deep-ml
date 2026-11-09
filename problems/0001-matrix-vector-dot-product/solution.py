def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	n_cols, n_rows = len(a[0]), len(a)
	if n_cols != len(b):
		return -1
	res = [0]*n_rows
	for i in range(n_rows):
		row = a[i]
		local_res = 0
		for j in range(n_cols):
			local_res += row[j]*b[j]
		res[i] = local_res
	return res 