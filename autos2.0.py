def calcular_precio(marca,puertas,color):
    marcas = {'Ford':100000, 'Chevrolet':120000, 'Fiat':80000}
    colores = {'Blanco':10000, 'Azul':20000, 'Negro':30000}
    puertas = {2:50000, 4:65000, 5:78000}
    precio = marcas[marca]+colores[color]+puertas[puerta]
    return precio


print('***PROGRAMA DE VENTAS DE AUTOS***')
mas_clientes = 'si'
ventas = []
marcas = ['Ford', 'Chevrolet', 'Fiat']
puertas = [2, 4, 5]
colores = ['Blanco', 'Azul', 'Negro']

while mas_clientes == 'si':
    nombre = input('Ingrese nombre del comprador: ')
    apellido = input('Ingrese apellido del comprador: ')
    marca= ''
    puerta= 0
    color= ''
    while marca not in marcas:
        marca = input('Ingrese marca: ')
    while puerta not in puertas:
        puerta = int(input('Ingrese cantidad de  puertas: '))    
    while color not in colores:
        color = input('Ingrese color: ')

    precio = calcular_precio(marca, puerta, color)    
    ventas.append({'nombre':nombre,'apellido':apellido,'marca':marca,'puertas':puerta ,'color':color, 'precio':precio})    
    mas_clientes = input('Hay más clientes?: ')

largo = len(ventas)
for i in ventas:
    if largo > 5 and largo < 11:
        i['precio'] = i['precio']*0.9
    if largo > 11 and largo < 51:
        i['precio'] = i['precio']*0.85
    if largo > 50:
        i['precio'] = i['precio']*0.82       
    print("La persona: " + i['nombre'] + " " + i['apellido'] +
     " compro un auto marca " + i['marca'] + " de "+str(i['puertas'])+
      " puertas y color " + i['color']+ " con un precio de $ "+ str(i['precio']))
# print("La persona: " + nombre + " " + apellido + " compro un auto marca "+marca+ " de "+str(puerta)+ " puertas y color " +color+ " con un precio de $ "+ str(precio) )

