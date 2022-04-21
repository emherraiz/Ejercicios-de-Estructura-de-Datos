class Bloque:
    # Un bloque es un conjunto de instrucciones ejecutadas
    # unas detrás de otras.
    def __init__(self):
        # Por defecto, un bloque no contiene ninguna instrucción.
        self.instrucciones = []

    def agregarInstruccion(self, instruccion):
        for i in instruccion:
            self.instrucciones.append(i)

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

    def lista(self):
        return [self.condicion, self.entonces, self.si_no]

class MientrasQue:
    # Representa una instrucción 'while'.
    # 'condicion' es una cadena que contiene el valor evaluado
    # para decidir si el bucle continúa o no,
    # 'bloque' es la secuencia de instrucciones ejecutadas en bucle.
    def __init__(self, condicion, bloque):
        self.condicion = condicion
        self.bloque = bloque

    def si_se_cumple(self):
        if self.condicion == bool(self.bloque.instrucciones[0]):
            return self.bloque.instrucciones[1]
        else:
            return self.bloque.instrucciones[2]


class Mostrar:
    # Una instrucción para mostrar un mensaje
    # en salida estándar.
    def __init__(self, mensaje):
        self.mensaje = mensaje

    def __str__(self):
        return self.mensaje



mostrar_ok = Mostrar('"OK"')
mostrar_ko = Mostrar('"KO"')
alternativa = Si("2 + 2 == 4", mostrar_ok, mostrar_ko)
bloque_alternativa = Bloque()
bloque_alternativa.agregarInstruccion(alternativa.lista())
bucle = MientrasQue(True, bloque_alternativa)
print(bucle.si_se_cumple())

