inputed_num = input("Введіть своє число : ")
all_num = [ ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
            [' # ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
            [' # ', ' # ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
            [' # ', ' # ', ' # ', '   ', '   ', '   ', '   ', '   ', '   '],
            [' # ', ' # ', ' # ', ' # ', '   ', '   ', '   ', '   ', '   '],
            [' # ', ' # ', ' # ', ' # ', ' # ', '   ', '   ', '   ', '   '],
            [' # ', ' # ', ' # ', ' # ', ' # ', ' # ', '   ', '   ', '   '],
            [' # ', ' # ', ' # ', ' # ', ' # ', ' # ', ' # ', '   ', '   '],
            [' # ', ' # ', ' # ', ' # ', ' # ', ' # ', ' # ', ' # ', '   '],
            [' # ', ' # ', ' # ', ' # ', ' # ', ' # ', ' # ', ' # ', ' # ']]

def height(n, your_num, num):
    width = ''
    if n < 0:
        return width
    else :
        for digit in your_num:
            digited = int(digit)
            width += num[digited][n]
        if '#' in width:
            print(width)
    return height(n-1, your_num, num)

print(height(8, inputed_num, all_num))