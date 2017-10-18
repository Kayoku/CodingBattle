n = int(input())


def l(n):
    if n== 0:
        return 1
    return 3 * l(n - 1)

length = l(n)
grid = [[" " for _ in range(length)] for _ in range(length)]
x_center, y_center = length//2, length//2



def fun(n, x_begin, y_begin, x_end, y_end ):
    if n == 0:
        grid[x_begin][y_begin] = 'X'
        return

    fun(n - 1, x_begin, y_begin, x_begin + l(n - 1), y_begin + l(n - 1))
    fun(n - 1, x_begin+ 2 * l(n - 1),  y_begin, l(n), y_begin + l(n - 1))
    fun(n - 1, x_begin, y_begin + 2 * l(n - 1), x_begin + l(n - 1), l(n))
    fun(n - 1, x_begin+ 2 * l(n - 1), y_begin + 2 * l(n - 1),l(n), l(n))
    fun(n - 1, x_begin + l(n - 1), y_begin + l(n - 1),  x_begin+ 2 * l(n - 1), y_begin + 2 * l(n - 1))

fun(n,0, 0, l(n) - 1, l(n) - 1 )


for i in range(length):
    for j in range(length):
        print(grid[i][j], end="")
    print()

