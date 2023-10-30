def cuenta_regresiva(numero):
    cuenta=[]
    for i in range(numero,-1,-1):
        cuenta.append(i)
    return cuenta
print(cuenta_regresiva(5))
print('-------------')   

def imprimir_y_devolver(lista):
    print(lista[0])
    return lista [1]
print(imprimir_y_devolver([1,2]))
print('-------------')   

def primero_mas_longitud(lista):
    return lista[0] + len(lista)
print(primero_mas_longitud([1,2,3,4,5]))
print('-------------')   

def valores_mayores (lista):
    if len(lista)<2:
        return False 
    lista_2=[]
    for i in range (0,len(lista)):
        if lista[1]<lista[i]:
            lista_2.append(lista[i])
    print(len(lista_2))
    return lista_2
print(valores_mayores([5,2,3,2,1,4]))
print(valores_mayores([3]))
print('-------------')   

def longitud_valor(tamaño,valor):
    lista= []
    for i in range(0,tamaño):
        lista.append(valor)
    return lista
print(longitud_valor(4,7))
print(longitud_valor(6,2))





