ch='y'
while(ch=='y' or ch=='Y'):
    n = int(input("Enter the value: "))
    c = 1
    m = 0
    star = [[0 for i in range(n)] for j in range(n)]
    while (c > 0):
        c = 0
        for i in range(m, n - m):
            for j in range(m, n - m):
                if i == m or j == m or i == n - m - 1 or j == n - m - 1:
                    star[i][j] = '*'
                elif j == m + 1 or j == n - m - 2 or i == m + 1 or i == n - m - 2:
                    star[i][j] = ' '
                else:
                    star[i][j] = '0'
                    c += 1
        m = m + 2
    for i in range(n):
        for j in range(n):
            print(star[i][j], end=" ")
        print()
    ch = input('Do you want to run again? y/n')