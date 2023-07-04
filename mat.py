# Prompt the user to input matrix dimensions
m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))

# Initialize an empty matrix
matrix = []

# Prompt the user to input matrix elements
for i in range(m):
    row = []
    for j in range(n):
        element = int(input(f"Enter element ({i},{j}): "))
        row.append(element)
    matrix.append(row)

# Print the matrix
for row in matrix:
    print(row)
