# date : 2024-02-13
# desc : 선형리스트 응용 2

from multipledispatch import dispatch # overloading 대체...

@dispatch(list, list)
def printPoly(t_x, p_x):
    polyStr = 'P(x) = '

    for i in range(len(px)):
        term = t_x[i]
        coef = p_x[i] # 계수

        if (coef >= 0):
            polyStr += '+'
        polyStr += str(coef) + 'x^' + str(term) + ' '        

    return polyStr

@dispatch(list)
def printPoly(p_x):
    term = len(p_x) - 1
    polyStr = 'P(x) = '

    for i in range(len(px)):
        coef = p_x[i] # 계수

        if (coef >= 0):
            polyStr += '+'
        polyStr += str(coef) + 'x^' + str(term) + ' '
        term -= 1

    return polyStr

@dispatch(int, list, list)
def calcPoly(xVal, t_x, p_x):
    retVal = 0

    for i in range(len(px)):
        term = t_x[i]
        coef = p_x[i]
        retVal += coef * xVal ** term

    return retVal

@dispatch(int, list)
def calcPoly(xVal, p_x):
    retVal = 0
    term = len(p_x) - 1

    for i in range(len(px)):
        coef = p_x[i]
        retVal += coef * xVal ** term
        term -= 1

    return retVal

px = [7, -4, 5] # 7x^3 - 4x^2 + 0x^1 + 5x^0
tx = [300, 20, 0]
px2 = [7, -4, 0, 5]

if __name__ == '__main__':
    print('Simple')
    pStr = printPoly(px2)
    print(pStr)

    xVal = int(input('x값 ==> '))
    pxVal = calcPoly(xVal, px2)
    print(pxVal)

    print('Multi')
    pStr = printPoly(tx, px)
    print(pStr)

    xVal = int(input('x값 ==> '))
    pxVal = calcPoly(xVal, tx, px)
    print(pxVal)