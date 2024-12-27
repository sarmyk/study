def get_matrix(n,m , value):
    matrix = []
    for i in range(1, n+1):
        matrix.append([])
        for j in range(1, m+1):
            matrix[i-1].append(value)
    return matrix

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)