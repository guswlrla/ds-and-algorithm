# date : 2024-02-13
# desc : 선형리스트 응용 2

def printPoly(t_x, p_x):
    polyStr = 'P(x) = '

    for i in range(len(px)):
        term = t_x[i]
        coef = p_x[i] # 계수

        if (coef >= 0):
            polyStr += '+'
        polyStr += str(coef) + 'x^' + str(term) + ' '        

    return polyStr

def calcPoly(xVal, t_x, p_x):
    retVal = 0

    for i in range(len(px)):
        term = t_x[i]
        coef = p_x[i]
        retVal += coef * xVal ** term

    return retVal

px = [7, -4, 5] # 7x^3 - 4x^2 + 0x^1 + 5x^0
tx = [300, 20, 0]

if __name__ == '__main__':
    print('Simple')
    pStr = printPoly(tx, px)
    print(pStr)

    xVal = int(input('x값 ==> '))

    pxVal = calcPoly(xVal, tx, px)
    print(pxVal)