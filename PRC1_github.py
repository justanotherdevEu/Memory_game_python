#January 2022

"""Objetivo: 

Poner en juego los conocimiento adquiridos para crear una aplicación que permita jugar al Memory. 

Requerimientos:

La aplicación debe cumplir las siguientes reglas:

Ofrecer una serie de números aleatorios cada vez mayores, de entre 1 y 99.999.999
El juego tendrá 7 rondas, deberá informar al usuario de la ronda en la que está. 
El jugador debe recordar cada uno de los números de cada ronda para ganar. Si falla 2 veces perderá el juego y se acabará la partida. 
Si recuerda todos los números en cada una de las rondas, ganará. 
Se deberá mostrar el resultado al usuario y ofrecerle jugar de nuevo o salir en cualquier caso. 
Dinámica del juego:

La dinámica del juego para cada ronda será:
                ofrece un numero aleatorio de 2 cifras.
                ofrece un numero aleatorio de 3 cifras.
                ofrece un numero aleatorio de 4 cifras.
                ofrece un numero aleatorio de 5 cifras.
                ofrece un numero aleatorio de 6 cifras.
                ofrece un numero aleatorio de 7 cifras.
                ofrece un numero aleatorio de 8 cifras.
De esta forma, en cada ronda mostrará el numero correspondiente a la ronda,
lo mantendrá en pantalla durante 7 segundos y lo borrará de la pantalla.
Pedirá por input al usuario que introduzca el numero que ha memorizado.
Cuando el usuario añada el numero deberá comprobar si ha acertado o fallado,
e informará al usuario del resultado. Si no ha consumido las vidas (2) , pasará a la siguiente ronda mostrando un nuevo numero correspondiente a la ronda. 

Información adicional:

Para algunas funcionalidades será necesario utilizar librerías adicionales como os (system), time (sleep) y random (randint).

Advertencias:

Se puede usar funciones. Aquí tienes que poner a prueba tu creatividad para programar scripts fáciles de entender y que hagan lo que se pide.
No se tolera la copia. En caso de detectar plagios, los alumnos implicados serán calificados con la mínima nota y tendrán que atenerse a las consecuencias especificadas en la guía docente.
Script que arroje un error que interrumpa la ejecución, implica una falta muy grave.
Se valorará mucho la calidad del código y la limpieza."""

import random,os,time,math
userRESTART = True
vidas = 2
def aleatorio_n(ronda):
    if ronda == 0:                          # cuando ronda es 0, es la ronda 1 realmente y hay 2 números, cuando ronda == 1, es la ronda 2 y hay 3 números, y así....
        aleatorio = random.randint(10,99)
        aleatorio = str(aleatorio)
        return aleatorio
        """elif ronda == 1:
        aleatorio = random.randint(100,999)  #realmente es un sólo 0, y si toca aleatorio el 0 el return devuelve un 0 y no 00 o 0000, independientemente de la ronda
        aleatorio = str(aleatorio)                           # ahí elevo a ronda+2 el número 10, para obtener el máximo que me puede dar el número de x cifras más uno, y le resto uno48
        return aleatorio"""
    else:                       #elif ronda not in (0,1):
        aleatorio = random.randint(pow(10,ronda+1),(pow(10,ronda+2)-1))  #realmente es un sólo 0, y si toca aleatorio el 0 el return devuelve un 0 y no 00 o 0000, independientemente de la ronda
        aleatorio = str(aleatorio)                           # ahí elevo a ronda+2 el número 10, para obtener el máximo que me puede dar el número de x cifras más uno, y le resto uno48
        return aleatorio
                                            #eso era la función que se llamará al inicio de cada ronda para obtener un número distinto en función del juego
def matrix(vidas, userRESTART,aleatorio_n):
  while vidas != 0 and userRESTART == True:   
    ronda = 0
    numerar = aleatorio_n(ronda)
    """vidas = 2""" # esto para cuando se reinicie el juego por el usuario
    print("""\n\nBienvenido al juego de memoria. hay 7 rondas, en cada una se te muestra un número y tienes que memorizarlo en los 7 segundos disponibles. Tienes 2 vidas a lo largo de
    la partida, pero la 0 no existe, eso díselo a Shigeru Miyamoto. Ojalá una práctica de Súper Mario o una simulación trader de criptomonedas / acciones...\n\nDe todas formas tampoco entiendo por qué un número del 1 al 99.999.999 si empezamos por números de 2 cifras y aumentando hasta los de 8 cifras. ( ಠ ͜ʖ ರೃ)\n\n\nÉste es tu primer número:\t"""+numerar)
    time.sleep(7)
    os.system("cls")
    print("¿Cuál era el número?\t\tNúmero + Enter:  ")
    usr = input("")
    while len(usr) != 2 or usr.isdecimal() == False:
        print("̿̿\n\n\n\n   ̿̿ ̿̿ ̿'̿'\̵͇̿̿\з= ( ▀ ͜͞ʖ▀) =ε/̵͇̿̿/’̿’̿ ̿ ̿̿ ̿̿ ̿̿         oye amigo, tienes que meter números, en concreto 2 cifras, esto no me sirve ("+usr+")      ╾━╤デ╦︻(▀̿Ĺ̯▀̿ ̿)  te vigilo.....\n\n\n")
        os.system("pause")
        print("¿Cuál era el número?\t\tNúmero + Enter:  ")   
        usr = input("")
    if numerar == "0":
        print("Recuerda que si es 0 sólo escribes 0 una vez") # si el ususario escribe 0 más de 4 veces lo siento pero una cosa es código a prueba de errores y otra a prueba de tontos
    elif usr == numerar or (usr in (0,00,000,0000) and numerar == "0"): 
        print("\n\tAcertaste,vidas:\t"+str(vidas))
    else:
        vidas -= 1
        print("\n\tFallaste,vidas:\t"+str(vidas))
        os.system("pause")
    while ronda != 7 and vidas != 0:
        ronda += 1
        os.system("cls")
        print("\t\t\tNUEVA RONDA\t"+str(ronda+1))
        numerar = aleatorio_n(ronda)
        print("Tu siguiente número es:\t\t"+numerar)
        # lo siento por repetirte ahora lo de antes, esto me pasa por dejar de planificar el funcionamiento antes de programarlo en Python
        time.sleep(7)
        os.system("cls")
        print("¿Cuál era el número?\t\tNúmero + Enter:  ")
        usr = input("")
        os.system("cls")
        while len(usr) != (ronda+2) or usr.isdecimal() == False:
            os.system("cls")
            print("̿̿\n\n\n\n  ̿̿ ̿̿ ̿'̿'\̵͇̿̿\з= ( ▀ ͜͞ʖ▀) =ε/̵͇̿̿/’̿’̿ ̿ ̿̿ ̿̿ ̿̿   oye amigo, tienes que meter números, en concreto  "+str(ronda+2)+", esto no me sirve ("+usr+")      ╾━╤デ╦︻(▀̿Ĺ̯▀̿ ̿)  te vigilo.....\n\n\n")
            os.system("pause")
            print("¿Cuál era el número?\t\tNúmero + Enter:  ")   
            usr = input("")
        if numerar == "0":
            print("Recuerda que si es 0 sólo escribes 0 una vez") # si el ususario escribe 0 más de 4 veces lo siento pero una cosa es código a prueba de errores y otra a prueba de tontos
        elif usr == numerar:  # or (usr in (0,00,000,0000) and numerar == "0")  
            print("\n\tAcertaste,vidas:\t"+str(vidas))
        else:
            vidas -= 1
            print("\n\tFallaste,vidas:\t"+str(vidas))
            os.system("pause")
    os.system("cls")
    print("\n\t\t\tEl juego ha terminado, ¿quieres jugar de nuevo?:\n--->1\t\tSí\n--->2\t\tNo\n")
    userOK = input("")
    while userOK.isdecimal() == False:
        os.system("cls")
        print("\n\t\t\tEl juego ha terminado, ¿quieres jugar de nuevo?:\n--->1\t\tSí\n--->2\t\tNo\n")
        userOK = input("")
    if userOK == "1":
        os.system("cls")
        vidas = 2
        pass
    elif userOK == "2" or userOK != "1":   #realmente me serviría con un simple else porque ya controlé que introduzca el user solamente 1 o 2, pero por buena práctica  😎
        userRESTART == False
        vidas = 0  # se acabó el juego, le dijo OTAN a Putin
        os.system("cls")
        print('''"""
             .-----.
            /       \       _____________
            \       /      /             \"""
     .-----.-`.-.-.<  _   /   GG EASY     \"""
    /      _,-\ O_O-_/ )  \               /
    \     / ,  `   . `|    \  ___________/
     '-..-| \-.,__~ ~ /     |/
           \ `-.__/  / ====/  _
          / `-.__.-\`-._     , ,
         / /|    ___\-._`-._;    ,.----.   """ -------------------------->> 
        ( ( |.-"`   `'\ '-(       -.---' 
         \ \/    {}{}  |   \.__.-'
          \|           /     
           \        , /
           ( __`;-;'__`)
           `//'`   `||`
          _//       ||
  .-"-._,(__)     .(__).-""-.
 /          \    /           \"
 \          /    \           /
  `'-------`      `--------'`'''+"\n\n\t\t\t\t\t\t\t\tEso es todo amigos")    #   https://texteditor.com/gallery/
        break  # freeeee!
matrix(vidas, userRESTART,aleatorio_n)
"""   .    _  .  _____________
   |\_|/__/|    /             \
  / / \/ \  \  / Your message  \
 /__|O||O|__ \ \     here      /
|/_ \_/\_/ _\ | \  ___________/
| | (____) | ||  |/
\/\___/\__/  // _/
(_/         ||
 |          ||\
  \        //_/ 
   \______//
  __|| __||
 (____(____)"""    #            If u see commented code, uncomment under your responsability. Commented code was testing parts for completing task, not definitive code