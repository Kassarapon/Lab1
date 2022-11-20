daimond = (d) = 9
daimondlow = (l) = 7

i = d - 1
while i >= 0:
    j = 0
    while j < i:
        print('', end = ' ')
        j += 1
    k = i
    while k <= d - 1:
        print('*', end = ' ')
        k += 1
    print('')
    i -= 2

i = 0
while i <= l - 1:
    j = 0
    while j < i+2:
        print('', end = ' ')
        j += 1
    k = i
    while k <= l - 1:
        print('*', end = ' ')
        k += 1
    print( )
    i += 2


