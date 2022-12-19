def biseccion(a ,b ,f ,TOL ):
    while ( (b - a)/2 > TOL ):
        c = (a + b)/2
        if ( f(c) == 0 ):
            break
        if ( f(a) * f(b) < 0 ):
            b = c
        else:
            a = c
    return ( a + b )/2