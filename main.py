from Juego import Juego

def mostrar_menu():
    print("=== MENÚ PRINCIPAL ===")
    print("1. Iniciar juego")
    print("2. Salir")
    print("3. Encriptar")
    print("4. ordenar")
    print("======================")

def main():
    nombre = input("Ingresa tu nombre para comenzar: ")
    juego = Juego(nombre)
    valor=True
    while valor:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            juego.iniciar_juego()
        elif opcion == "2":
            juego.salir()
            valor=False
        elif opcion == "3":
            juego.encriptar()
        elif opcion == "4":
            juego.ordenar()
        elif opcion == "5":
            juego.desencriptar()
        else:
            print("Opción inválida. Intenta de nuevo.\n")

main()
