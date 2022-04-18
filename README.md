# Ejercicios-de-Estructura-de-Datos
## Link del repositorio
https://github.com/emherraiz/Ejercicios-de-Estructura-de-Datos

## Ejercicio 1
Enunciado: aquí hay clases que representan los elementos de sintaxis de un lenguaje de programación:

class Bloque: 
    # Un bloque es un conjunto de instrucciones ejecutadas 
    # unas detrás de otras. 
    def __init__(self): 
        # Por defecto, un bloque no contiene ninguna instrucción. 
        self.instrucciones = [] 
 
    def agregarInstruction(self, instruccion): 
        self.instrucciones.append(instruccion) 
 
class Si: 
    # Representa una instrucción 'if'. 'condicion' es una cadena 
    # de caracteres que contiene la evaluación de la condición, 
    # 'entonces' es el bloque de instrucciones ejecutadas si la condición 
    # se verifica, 'si_no' es el bloque de instrucciones ejecutadas 
    # si no se verifica. 
 
    def __init__(self, condicion, entonces, si_no): 
        self.condicion = condicion 
        self.entonces = entonces 
        self.si_no = si_no 
 
class MientrasQue: 
    # Representa una instrucción 'while'. 
    # 'condicion' es una cadena que contiene el valor evaluado 
    # para decidir si el bucle continúa o no, 
    # 'bloque' es la secuencia de instrucciones ejecutadas en bucle. 
    def __init__(self, condicion, bloque): 
        self.condicion = condicion 
        self.bloque = bloque 
 
class Mostrar: 
    # Una instrucción para mostrar un mensaje 
    # en salida estándar. 
    def __init__(self, mensaje): 
        self.mensaje = mensaje 
Y aquí hay un pequeño "programa" escrito usando estas clases:

mostrar_ok = Mostrar('"OK"') 
mostrar_ko = Mostrar('"KO"') 
alternativa = Si("2 + 2 == 4", mostrar_ok, mostrar_ko) 
bloque_alternativa = Bloque() 
bloque_alternativa.agregarInstruccion(alternativa) 
bucle = MientrasQue(True, bloque_alternativa) 
Escriba un visitante que pueda recorrer este programa y convertirlo en un programa de Python, como este:

> python visitante.py 
while True: 
   if 2 + 2 == 4: 
          print("OK") 
   else: 
          print("KO") 
Consejo: no intente resolver todos los problemas a la vez. Al principio, solo preocúpese de mostrar las instrucciones de Python. Seguidamente cuide las tabulaciones.

## Ejercicio 2

Enunciado: siguiendo la filosofía MVC, escriba un programa que lea dos líneas en la entrada estándar, las convierta a mayúsculas y las escriba en un archivo. Tenga en cuenta que para beneficiarse plenamente de las ventajas del design pattern MVC, los atributos, en particular los del modelo, se deben encapsular.

## Ejercicio 3

Enunciado: Implementar un programa que factura productos por valor de 100, con la tasa de IVA correcta, según sean productos de alimentación o servicios.

Comportamiento esperado:

producto = Producto(Naturaleza.ALIMENTARIA) # IVA 5,5% 
precio_neto = FactoryFactura.crear(producto).facturar() 
print(precio_neto) 
# 105.5 
 
producto = Producto(Naturaleza.SERVICIO) # IVA 20% 
precio_neto = FactoryFactura.crear(producto).facturar() 
print(precio_neto) 
# 120 
