# date : 2024-02-13
# desc : 선형리스트 응용

px = [7, -4, 0, 5] # 7x^3 - 4x^2 + 0x^1 + 5x^0

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

def calcPoly(xVal, p_x):
    retVal = 0
    term = len(p_x) - 1

    for i in range(len(px)):
        coef = p_x[i]
        retVal += coef * xVal ** term
        term -= 1

    return retVal

if __name__ == '__main__':
    pStr = printPoly(px)
    print(pStr)

    xVal = int(input('x값 --> '))

    pxVal = calcPoly(xVal, px)
    print(pxVal)

## 못쓴거있다 수정해라