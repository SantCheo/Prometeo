number=0
def codigo_1( number ): 
    a = 0 
    for j in range(1, number+1): 
        a += a + j 
    for k in range(number, 0, -1): 
        a -= 1 
        a *= 2 
    return a
