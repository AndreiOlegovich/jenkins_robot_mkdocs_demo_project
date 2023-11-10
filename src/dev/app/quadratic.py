from math import sqrt

TYPE_ERROR_TEXT = "Not valid argument type"

def quadratic_solve(a ,b, c):
    if not all(
        map(
            lambda p: isinstance(p, (int, float)),
            (a, b, c)
        )
    ):
        raise TypeError(TYPE_ERROR_TEXT)
    print("Types are OK")

    if a == 0:
        if b == 0:
            # a и b 0: решения нет
            return None, None
        return -c / b, None
    d = b ** 2 - 4 * a * c
    if d < 0:
        return None, None
    
    d_root = sqrt(d)
    divider = 2 * a
    x1 = (-b + d_root) / divider
    x2 = (-b - d_root) / divider

    if d == 0:
        x2 = None
    elif x2 > x1:
        x1, x2 = x2, x1

    return x1, x2

if __name__ == "__main__":
    print(quadratic_solve(1, -1, -2))
    print(quadratic_solve("", 2, 3))
    
