from tkinter.tix import INTEGER


def reverse(x: int) -> int:
    x = str(x)

    x = x[::-1]
    if x[-1] == '-':
        x = '-' + x[:-1]
    
    return int(x) if int(x) > -2**31 and int(x) < 2**31-1 else 0

print(reverse(123))