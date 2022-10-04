import utilidades as utils
import comandosSql as comandosql

funcionesUtilidades = ["",lambda: comandosql.crearBaseDatos(),lambda: comandosql.dropDatabase()]

def numeroValido(numero): #Comprobamos si el numero es valido
    numero = int(numero)
    if numero == 0 or numero >= len(funcionesUtilidades):
        return False
    elif numero <=len(funcionesUtilidades):
        return True

def funcionParaLlamar (numeroUsuario):
    if(numeroValido(numeroUsuario)):
        return funcionesUtilidades[numeroUsuario]()
    else:
        print("ERR:01, ese numero no es valido")
        exit()