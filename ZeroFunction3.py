def heipo(x):
    return x ** 2 - x - 20


def heipoPRIME(x):
    return 2 * x - 1


def bissection(func, a, b, tol=1e-5):
    while 1:
        x = (a + b) / 2
        res1 = x
        if func(x) * func(a) < 0:
            b = x
        else:
            a = x
        res2 = (a + b) / 2

        if abs(res2 - res1) < tol:
            return x


def NewtonRaphson(func, derivative, xold, tol=1e-5):
    while 1:
        x = xold - func(xold) / derivative(xold)

        if abs(x - xold) < tol:
            return x
        else:
            xold = x


def Secante(func, xold, xold2, tol=1e-5):
    while 1:
        derivative = (func(xold) - func(xold2)) / (xold - xold2)
        x = xold - func(xold) / derivative
        if abs(x - xold) < tol:
            return x
        else:
            xold2 = xold
            xold = x


print(bissection(heipo, -30, 0, tol=1e-5))

print(NewtonRaphson(heipo, heipoPRIME, -2, tol=1e-5))

print(Secante(heipo, -4, -5, tol=1e-5))
