# Alejandro_Salinas_Victorino_objeto_seguro
Python &amp; Linux Proyecto

Tengo algunas dudas con respecto a mi implementación. 

1) Genere un diccionario que es para colocar las llaves publicas de todos los objetos, de momento solo es parte estructural aunque podria ser un obejto. ¿Es valida esta implementación para el cambio de llaves?, o en su defecto, debo de implementar un metodo en clase Objeto seguro.

2) El Método: almacenar_msj(msj: str) -> dict.   Nos retorna como tal un diccionario, pero en si, ¿tiene caso este tipo de retorno?, ya que no se ocupa en otros metodos, o al menos aun no encuentro la relación de este tipo de retorno. 

3) En el metodo Método: responder(msj: str) -> byte. Descripción: Este método se ejecuta automáticamente al recibir un saludo de otro objeto seguro, el parámetro de entrada es el nombre del objeto al que se responderá. La respuesta deber ser el mensaje recibido, concatenado con el string “MensajeRespuesta”.

Para este método considere que se deberia de cifrar el mensaje. Como se menciona es concatenar el mensaje: <saludo descifrado> + <MensajeRespuesta>, ¿es correcto?
  Otra cuestión, la descripción del metodo nos dice otra cosa de lo que se tiene escrito, ya que se deberia de enviar el nombre del objeto al que queremos responder, lo cual tiene sentido, entonces sería: responder(nombre: str) ->bytes: 
  O en su defecto implemento responder(nombre: str, mensaje: str) ->bytes:
  
4) ¿esta primera parte del proyecto solo se basa en realizar el enlace de comunicación de los 5 pasos que se muestran en el digrama de la pag 3 del pdf, es decir del paso 0 al 4?
  
5) ¿Es correcto suponer que al inciar un objeto su respectivo archivo de registros RegistoMsj_<NombredelObjetoSeguro>.txt debe generarse nuevamente, es decir, borrar historiales anteriores para que no exista conflictos de ID (ID repetidos)? 
  
  Nota: Algunas partes de mi código son implementadas solo para la depuración, tal es el caso de la impresión de texto en consola. 
  Cualquier comentario y sugerencia es una buena retroalimentación. Muchas gracias por tomarse el tiempo en la revisión. Salu2. 
