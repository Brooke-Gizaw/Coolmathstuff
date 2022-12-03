for x in range(2, 1000):
    y = (x**3) % ((x - 1) * x)
    print(x, ":", y)
