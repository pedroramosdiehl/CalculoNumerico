if __name__ == '__main__':
    x0, y0 = 0.0, 0.5
    x1, y1 = 1.0, 0.0
    n = 5

    h = (x1 - x0) / n

    g = lambda x, y: y - x ** 2 + 1

    f0 = lambda x, y: g(x, y)
    f1 = lambda x, y: g(x + h / 2, y + h / 2 * f0(x, y))
    f2 = lambda x, y: g(x + h / 2, y + h / 2 * f1(x, y))
    f3 = lambda x, y: g(x + h, y + h * f2(x, y))

    while x0 < x1:
        y1 = y0 + h / 6 * (f0(x0, y0) + 2 * f1(x0, y0) + 2 * f2(x0, y0) + f3(x0, y0))
        x0 += h
        y0 = y1

    print 'x1:', x1,'  y1:', y1
