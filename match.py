# usuarios = {}
# def iniciar_sesion():
#     if not usuarios:
#         print("\nAdvertencia: no hay usuarios registrados. por favor registre usuarios primero.")
#         return
#     print("\nInicio de secion:")
#     usuario = input("ingrese su nombre de usuario")
#     contraseña = input("ingrese su contraseña")
#     if usuario in usuario and usuarios[usuario] == contraseña:
#         print(f"bienvenido, {usuario}. has iniciado sesion exitosamente.")
#     else:
#         print("usuario o contraseña incorrectos.")
# def registrar_usuarios():
#     while len (usuarios) < 3:
#         print("\nRegistrar usuario:")
#         usuario = input("ingrese un nombre de usuario (3 - 12 caracteres): ")
#         if len (usuario) < 3 or len (usuario) > 12:
#             print("el nombre de usuario debe tener entre 3 a 12 caracteres.")
#             continue
#         if usuario in usuario:
#             print("el usuario ya existe intente con otro.")
#             continue
#         contraseña = input("ingrese una contraseña (4 - 10 caracteres):")
#         if len (contraseña) < 4 or len (contraseña) > 10:
#             print("la contraseña debe tener entre 4 a 10 caracteres")
#             continue
#         usuario [usuario] = contraseña
#         print(f"Usuario '{usuario}' registrado exitosamente.")
#         print("\nSe alcanzó el límite de 3 usuarios registrados.")
# def mostrar_menu():
#     print("1.- iniciar sesion")
#     print("2.- registrarse")
#     print("3.- salir")
    
#     opcion = input("seleccione una opcion")

#     if opcion == "1" :
#         iniciar_sesion
#     elif opcion == "2" :
#         registrar_usuarios
#     elif opcion == "3" :
#         print("¡hasta luego!")
#         break
#     else:
#         ("opcion no valida, intente nuevamente.")
   