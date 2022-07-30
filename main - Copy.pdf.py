import numpy as np
from numpy import double
#input
# [1,2,3]
# [1,2,3]
# [1,2,3]
Num_V = int(input("Enter the number of variables: "))
matrix = []
values = []
print("Enter the system as an augmented matrix:  ")
print("Enter the values of each row respectively:  ")
for i in range(Num_V):
    row = []
    for j in range(Num_V):
        row.append(int(input("")))
    values.append(int(input("")))
    matrix.append(row)

matrix_a = np.array(matrix)
vlaues_m = np.array(values)



original_mat_det = double(np.linalg.det(matrix_a))

if int(np.linalg.matrix_rank(matrix_a)) >= Num_V:
    Original_Det = int(np.linalg.det(matrix_a))
    for i in range(Num_V):
        temp_matrix = []
        for k in range(Num_V):
            row = []
            for j in range(Num_V):
                if i == j:
                    row.append(values[k])
                else:
                    row.append(matrix[k][j])
            temp_matrix.append(row)

        matrix_temp = np.array(temp_matrix)
        tem_det= double(np.linalg.det(matrix_temp))
        print("The value of x"+str(i+1)+" = "+ str (round((tem_det/original_mat_det))))
else:
    print("No Solution")
