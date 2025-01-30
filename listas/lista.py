# m=[[[2,7,5],
#    [3,4,7]],
   
#    [[9,1,2],
#    [8,6,71]]]
# print(m[1][1])

# for i in m:
#     print(i)
# print(m)
# print(m[1][1][0])

# --------------- diccionario -------------
# diccionario={"nombre": "cesar huispe",
#              "fono":[988778882,
#                     988877776,
#                     877666333],
#              "activo": True}
# producto={
#     "uva":1400,
#     "pera":1200,
#     "melon":1000,
#     "verduras": {"papa": 600,
#                 "pepino": 500}
# }
# print(diccionario["activo"])

# for clave, valor in producto.items():
#     print(f"{clave} = ${valor}")

# caso 1
# nombres= [input(f"ingrese el nombre {i + 1}:") for i in range (3)]

# nombre_mas_largo= max(nombres, key=len)

# print(f"el nombre con mayor cantidad de caracteres es:{nombre_mas_largo}")

# # caso 2

# nombres = [input(f"ingrese el nombre { i + 1}:") for i in range(3)]
# apellidos = [input(f"ingrese el apellido {i + 1}:") for i in range(3)]
# nombres.sort()
# apellidos.sort()
# print("nombres ordenados:",",".join(nombres))
# print("nombres ordenados:",",".join(apellidos))

# # caso 3

# nombre = []
# while True:
#     nombre = input("ingrese un nombre:")
#     nombres.append(nombre)
#     continuar = input("¿desea agregar otro nombre? (si/no):").strip().lower()
#     if continuar == "no":
#         break

# nombre_mas_corto = min(nombres, key=len)
# nombres.remove(nombre_mas_corto)
# print(F"el nombre eliminado fue: {nombre_mas_corto}")
# print("lista final de nombres: ",",".join(nombres))



personas={}

while True:
    nombre=input("ingrese un nombre(o x para salir):")
    if nombre.lower() == "x":
        break
    edad= input("ingrese la edad:")
    if edad.isdigit:
        personas[nombre] = int(edad)
    else:
        print("por favor, ingrese una edad valida.")

with open("personas.txt", "w") as archivo:
    for nombre, edad in personas.items():
        archivo.write(f"{nombre}: {edad} años\n")
print("datos guardados en persona.txt .")
        
# print("\nlista de personas y edad valida:")
# for nombre, edad in personas.items():
#     print(f"{nombre}: {edad} años")