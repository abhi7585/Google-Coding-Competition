n = int(input("Enter the dimention: "))
matrix = []

for i in range(n):
    temp = list(map(int, input().split()))
    matrix.append(temp)

diagSum = 0
rowRepeat = 0
colRepeat = 0

for i in range(n):
    for j in range(n):
        if i == j:
            diagSum += matrix[i][j]

    temp = matrix[i]
    if len(temp) != len(set(temp)):
        rowRepeat += 1

for j in range(n):
    temp = []
    for i in range(n):
        temp.append(matrix[i][j])
    else:
        if len(temp) != len(set(temp)):
            colRepeat += 1


print(f"{diagSum} {rowRepeat} {colRepeat}")
