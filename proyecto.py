#  Clase: ObjetoSeguro(nombre: str)
#  Descripción: Creación de un objeto seguro, se recibe el nombre en formato String
from ecies.utils import generate_eth_key
from ecies import encrypt, decrypt
import base64


#  Este diccionario nos permite hacer una coleccón de llaves publicas.
LlaveroPublico = {}  # se puede generar una clase.


def agregar_llave(nombre: str, llave_pub: str):
    LlaveroPublico[nombre] = llave_pub


def devolver_llave(name: str):
    return LlaveroPublico[name]


class ObjetoSeguro:
    def __init__(self, nombre: str):
        self.nombre = nombre
        #  print(f"El objeto seguro se llama {self.nombre}")
        self.__gen_llaves() # metodo privado
        self.__privKeyHex, self.pubKeyHex = self.__gen_llaves()
        agregar_llave(self.nombre, self.pubKeyHex)
        self.__usario_destino = "" # usuario al que se le envia un mensaje
        self.__id = 0
        self.__registro = {}
        self.__mensaje_recibido = ""

        # Generamos un archivo vacio cada vez que se inicia la clase.
        archivo = "RegistroMsj_" + self.nombre + ".txt"
        archivo = open(archivo, 'w')
        archivo.close()

#  Método: gen_llaves()
#  Descripción: Genera la llave y privada y su correspondiente llave pública.
    def __gen_llaves(self):
        privKey = generate_eth_key()
        privKeyHex = privKey.to_hex()
        pubKeyHex = privKey.public_key.to_hex()
        return privKeyHex, pubKeyHex

#  Método: saludar(name: str, msj: str)
#  Descripción: Método público accedido por el objeto que quiere comenzar la comunicación,
#  los parámetros de entrada son el nombre del objeto que comienza la comunicación y el mensaje cifrado con
#  la llave pública del destinatario.
    def saludar(self, name: str, msj: str) ->bytes:
        self.__usario_destino = name
        #self.__mensaje = msj
        llave_publica_destinatario = self.llave_publica()
        return self.__cifrar_msj(llave_publica_destinatario, msj)

#  Método: esperar_respuesta(msj: byte) Descripción: Este método sirve para esperar una respuesta cifrada con llave
#  pública que se desencadena de un hacer un saludo a otro objeto. Este método debe llamar al método para almacenar
#  automáticamente el mensaje de respuesta recibido en texto plano.

    def esperar_respuesta(self, msj: bytes):
        msj = self.__decodificar64(self.__descifrar_msj(msj))
        print("El mensaje recibido descifrado es: ", msj)
        self.__almacenar_msj(msj)
        self.__mensaje_recibido = msj
        #self.__responder(msj, "Alejandro")
#  Método: almacenar_msj(msj: str) -> dict. Descripción: Este método sirve para almacenar un mensaje en texto plano
#  en un archivo de texto y le es asignado un ID para identificarlo. El retorno es el ID asignado
#  en el formato {“ID”:<id>}. Nota: el ID y el mensaje es la mínima información que deberá tener el registro,
#  el alumno puede asignar más campos de acuerdo con su criterio.

#  Los mensaje enviados y recibidos deben ser almacenados automáticamente en un archivo de texto
#  llamado: RegistoMsj_<NombredelObjetoSeguro>.txt

    def __almacenar_msj(self, msj:str) -> dict:
        archivo = "RegistroMsj_" + self.nombre + ".txt"
        self.__registro[self.__id] = {
            "ID": self.__id,
            "MSJ": msj
            }
        with open(archivo, 'a') as f:
            f.write(str(self.__registro[self.__id]) + str("\n"))
        self.__id += 1
        return {"ID": self.__id}

# Método: consultar_msj(id: int) -> dict. Descripción: Este método sirve para consultar un mensaje del registro
# en el archivo de texto utilizando el ID asignado. El retorno de esta función es el mensaje en el siguiente
# formato {“ID”:”id”, MSJ”:”Mensaje_consultado”, “campo1”:”valor1”, ...}
    def consultar_msj(self, id: int):
        archivo = "RegistroMsj_" + self.nombre + ".txt"
        cont = 0
        with open(archivo, 'r') as buscar:
            for line in buscar:
                if cont == id:
                    print(line)
                    return (line)
                cont += 1
        return "No se encontro la consula"  # opcinal

#  Método: responder(msj: str) -> byte. Descripción: Este método se ejecuta automáticamente al recibir un saludo de otro
#  objeto seguro, el parámetro de entrada es el nombre del objeto al que se responderá. La respuesta deber ser el
#  mensaje recibido, concatenado con el string “MensajeRespuesta”.
    def responder(self, nombre: str):
        self.__usario_destino = nombre
        msj = self.__mensaje_recibido
        print("El mensaje se recibio exitosamente, ahora respondemos")
        llave_pub = self.llave_publica()
        return self.__cifrar_msj(llave_pub, msj + " MensajeRespuesta")


    # Método: llave_publica() -> str.
# Descripción: Este método sirve para obtener la llave pública del objeto seguro.
    def llave_publica(self) -> str:
        #print (f"LLAVE PUBLICA OBTENIDA DE: { self.__usario_destino}")
        #print(devolver_llave(self.__usario_destino))
        return devolver_llave(self.__usario_destino)
        # return self.pubKeyHex

#  Método: codificar64(msj: str) -> bytes. Descripción: Este método sirve para codificar un mensaje en texto plano
#  en base64, el retorno es el mensaje en texto plano codificado en base64.
    def __codificar64(self, msj : str) -> bytes:
        msj_bytes = msj.encode('ascii')
        return base64.b64encode(msj_bytes)

#  Método: decodificar64(msj: bytes) -> str. Descripción: Este método sirve para decodificar un mensaje en base64
#  un mensaje en texto plano, el retorno es el mensaje en texto plano.
    def __decodificar64(self, msj: bytes) -> str:
        msj_bytes = base64.b64decode(msj)
        return msj_bytes.decode('ascii')

#  Método: cifrar_msj(pub_key: str, msj: str) -> bytes.
#  Descripción: Este método sirve para cifrar un mensaje con la llave pública del destinatario,
#  el retorno es el mensaje cifrado.

    def __cifrar_msj(self, pub_key: str, msj: str) -> bytes:
        return encrypt(pub_key, self.__codificar64(msj))

#  Método: descifrar_msj(msj: byte) -> byte.
#  Descripción: Este método sirve para descifrar un mensaje cifrado, el retorno es el
#  mensaje en texto plano codificado en base64.

    def __descifrar_msj(self, msj: bytes) -> bytes:
        return decrypt(self.__privKeyHex, msj)
