matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

flattened_matrix = []

for row in matrix:
    for cell in row:
        flattened_matrix.append(cell)

print(flattened_matrix)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

print([cell for row in matrix for cell in row if cell % 2 == 0])