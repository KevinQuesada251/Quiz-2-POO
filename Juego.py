class Juego:
    def __init__(self, nombre_jugador):
      
        self.nombre_jugador = nombre_jugador
        self.jugando = False


    def iniciar_juego(self):
        self.jugando = True
        print(f"\n¡Bienvenido al juego, {self.nombre_jugador}!")
        print("El juego ha comenzado..")
        print("Aqui va el juego o los metodos de instancia donde vas a crear la logica del juego.")
        self.menu()
        print("¡Gracias por jugar!\n")

    def salir(self):
        print(f"\nHasta luego, {self.nombre_jugador}. ¡Vuelve pronto!")
        
    def encriptar(self):
        letrasEncriptadas = []
        palabra = input("ingrese la palabra: ")
        abecedario =  "abcdefghijklmnñopqrstuvwxyza"
       
        for letra in palabra:
            x = abecedario.index(letra)+1
            letrasEncriptadas.append(abecedario[x])
            palabraEncriptada = "".join(letrasEncriptadas)
            
        print(f"Ahora la palabra es {palabraEncriptada}")
        
        
    def desencriptar(self):
        letrasEncriptadas = []
        palabra = input("ingrese la palabra: ")
        abecedario =  "abcdefghijklmnñopqrstuvwxyza"
       
        for letra in palabra:
            x = abecedario.index(letra)-1
            letrasEncriptadas.append(abecedario[x])
            palabraEncriptada = "".join(letrasEncriptadas)
            
        print(f"La palabra es {palabraEncriptada}")
        
    def ordenar(self):
        
        lista = input("Ingrese los numeros a ordenar separados por coma: ")
        lista_numeros = []
        for numero in lista.split(","):
            lista_numeros.append(int(numero))
       
        tamanoLista = len(lista_numeros)-1
        
        for i in range(tamanoLista):
             for numero in range(tamanoLista-i):
                 if lista_numeros[numero] > lista_numeros[numero+1]:
                     lista_numeros[numero], lista_numeros[numero+1] = lista_numeros[numero+1], lista_numeros[numero]
        
        print(lista_numeros)
                     
        
                    
        
    
    def menu(self):
        print("Qué juego desaes ejecutar?")
        print("1-Ensalada César")
        print("2-Bomba burbuja")
        opcion = input("elija")
        if opcion == "1":
            self.encriptar()
        elif opcion == "2":
            self.laotrafuncion()
        elif opcion == "3":
            self.ordenar()
        
        
        
            
            
            
            

  
    


