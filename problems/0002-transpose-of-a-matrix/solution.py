def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    n_cols, n_rows = len(a[0]), len(a)
    res = [[0]*n_rows for _ in range(n_cols)]
    for i in range(n_rows):
        for j in range(n_cols):
            res[j][i] = a[i][j]
    return res
    