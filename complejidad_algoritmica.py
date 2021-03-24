import time
#Para poder medir el tiempo en python importamos el modulo time

def factorial(n): #(n) recibimos un numero para el factorial
    #Implementacion iterativa
    respuesta = 1

    while n > 1:
        #mietras n sea mayor que 1
        respuesta *= n # es lo mismo que respuesta = respuesta * n (este shorcut lo usamos mejor)
        # vamos a multiplicar la respuesta por n
        n -= 1
        #vamos haciendo n cada vez mas chica

    return respuesta
    #regresamos la respuesta (aqui tenemos nuesto primer factorial)


def factorial_r(n):
    #implementacion recursiva
    if n == 1:
        # caso base si n es igual a 1
        return 1
        # regresa 1

    return n * factorial(n - 1) #codigo recursivo
    # sino regresa n por factorial de n - 1


if __name__ == '__main__': #inicializamos
    n = 200000
    #primera variable

    comienzo = time.time()
    # comienzo es igual a time con la fnncion time (estamos ejecutando el modulo time que adentro tiene la funcion time)
    factorial(n)
    #factorial de n
    final = time.time()
    # final es time . time
    print(final - comienzo)
    #vamos a imprimir el tiempo que es igual a el tiempo final menos el comienzo

    comienzo = time.time()
    # reasignamos la misma variable
    factorial_r(n)
    final = time.time()
    print(final - comienzo)
    #vamos a imprimir el tiempo que es igual a el tiempo final menos el comienzo