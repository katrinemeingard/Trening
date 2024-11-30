def get_matrix(n, m, value):
    matrix = []
    if n <= 0 or m <= 0:
        matrix_ = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    return matrix

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)

#  for n in get_matrix():  #В первом цикле добавляйте пустой список в список matrix. n повторов.
#Напишите второй(внутренний) цикл for для кол-ва столбцов матрицы, m повторов.
 #       for m in get_matrix():  #Во втором цикле пополняйте ранее добавленный пустой список значениями value.
