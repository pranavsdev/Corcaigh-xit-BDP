"""
R00183777
Corcaigh-xit problem
"""

filename= 'input_files/input_1.txt'

#store the dimension from the input file
with open(filename, 'r') as f:
    dim = f.readline()

#get the data from the file
with open(filename, 'r') as f:
    data = f.readlines()[1:] # read lines, except the first one

input_matrix = [] 
for raw_line in data:
    split_line = raw_line.strip().split(" ")
    input_matrix.append(split_line)

dim_data = dim.strip().split(" ")

m = int(dim_data[0])
n = int(dim_data[1])

output_matrix =[]

print("input matrix is ---> ", input_matrix)

for i in range(0, m):
    row = []
    for j in range(0, n):
        #print("i,j is", i,",",j)
        count_flag = 0
        if input_matrix[i][j] == 'x':
            #print(matrix[i][j])
            row.append(input_matrix[i][j])
        else:
            if i > 0:
                if input_matrix[i-1][j] == 'x':
                   count_flag += 1 
            if i+1 < m:
                if input_matrix[i+1][j] == 'x':
                    count_flag += 1
            if j > 0:
                if input_matrix[i][j-1] == 'x':
                    count_flag += 1
            if j+1 < n:
                if input_matrix[i][j+1] == 'x':
                    count_flag += 1
            if i+1<m and j+1 <n:
                if input_matrix[i+1][j+1] == 'x':
                    count_flag += 1
            if i-1>=0 and j-1>=0:
                if input_matrix[i-1][j-1] == 'x':
                    count_flag += 1
            if i+1<m and j-1>=0:
                if input_matrix[i+1][j-1] == 'x':
                    count_flag += 1
            if i-1>=0 and j+1<n:
                if input_matrix[i-1][j+1] == 'x':
                    count_flag += 1
            row.append(count_flag)
    output_matrix.append(row)

print("output matrix is --->",output_matrix)