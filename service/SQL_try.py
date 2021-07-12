def Z(x, y, px, py):

    Z = list()
    for i in range(0, len(x)):
        for j in range(0, len(y)):
            Z.append(2*x[i]-y[j])

    Zp = list()
    for i in range(0, len(x)):
        for j in range(0, len(y)):
            Zp.append(round((px[i]*py[j]), 3))

    return Z, Zp


def M(x, px):
    MX = list()
    for i in range(0, len(x)):
        MX.append(round(x[i]*px[i], 3))
    return MX

x = (-2, -1, 0, 1)
y = (0, 1, 2, 3)
px = (0.3, 0.2, 0.4, 0.1)
py = (0.4, 0.2, 0.3, 0.1)

z, zp = Z(x, y, px, py)

n = [item**2 for item in y]
print(M(n, py), sum(M(n, py)))
print(4*1.5+4*(-0.7)*1.1+2.3-0.09)
