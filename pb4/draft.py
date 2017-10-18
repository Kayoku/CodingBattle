n = int(input())


def l(n):
    if n== 0:
        return 1
    return 3 * l(n - 1)

length = l(n)
grid = [[" " for _ in range(length)] for _ in range(length)]
x_center, y_center = length//2, length//2



ln = [1]

for i in range(1, n + 1):
    ln.append(3 * ln[i - 1])
    print(str(i) + ": " + str(ln[i]))
print(ln)



def fun(n, x_begin, y_begin, x_end, y_end ):
    if n == 1:

        # grid[x_begin][y_begin] = 'X'
        # grid[x_begin][y_end] = 'X'
        # grid[x_end][y_begin] = 'X'
        # grid[x_end][y_end] = 'X'
        # grid[x_begin + 1][y_begin + 1] = 'X'
        
        grid[x_begin][y_begin] = 'X'
        grid[x_begin][y_end - 1] = 'X'
        grid[x_end - 1][y_begin] = 'X'
        grid[x_end - 1][y_end - 1] = 'X'
        grid[x_begin + 1][y_begin + 1] = 'X'
        return

    
    if n == 0:
        grid[x_begin][y_begin] = 'X'
        return
    
    fun(n - 1, x_begin, y_begin, x_begin + ln[n - 1], y_begin + ln[n - 1])
    fun(n - 1, x_begin+ 2 * ln[n - 1],  y_begin, ln[n], y_begin + ln[n - 1])
    fun(n - 1, x_begin, y_begin + 2 * ln[n - 1], x_begin + ln[n - 1], ln[n])
    fun(n - 1, x_begin + 2 * ln[n - 1], y_begin + 2 * ln[n - 1],ln[n], ln[n])
    fun(n - 1, x_begin + ln[n - 1], y_begin + ln[n - 1],  x_begin+ 2 * ln[n - 1], y_begin + 2 * ln[n - 1])

fun(n,0, 0, ln[n] - 1, ln[n] - 1 )
# fun(n,0, 0, ln[n], ln[n])


for i in range(length):
    for j in range(length):
        print(grid[i][j], end="")
    print()

