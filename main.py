
import utilidades as utils
import logica as logic

seguir = utils.stay("s") # Variable flag
# Iniciamos un bucle para que ejecute el programa todo el tiempo que sea necesario
while seguir == True:


    print(utils.bienvenida())
    usr = int(input("Que quieres hacer? ")) # aqui el usr pone un numero
    utils.limpiarConsola()
    logic.funcionParaLlamar(usr)



    # Al finalizar, le pregunto al usuario si quiere seguir
    seguirUsr = input("Deseas seguir en el programa? S/n: ")
    seguir = utils.stay(seguirUsr)

