row = 12
col = 15
grid = [['.' for i in range(col)] for j in range(row)]

for i in range(col):
    print(i+1, '\t')

for i in range(row):
    print('\n')
    for j in range(col):
        print(grid[i][j], '\t')
        
