class Automovil:
    #nuestra primera clase

    def __init__(self, modelo, marca, color):
        #Simpre se inicializa con __init__ la primera instancia de una clase
        self.modelo = modelo
        # inicialisamos las variables de instancias al usar self.(el nombre de la variable parametro)
        self.marca = marca
        self.color = color
        self._estado = 'en_reposo'
        # Variable privada usando el _ no tienen por que saber esta variable los demas
        self._motor = Motor(cilindros=4)

    def acelerar(self, tipo='despacio'):
        # usammos un parametro por defecto al usar (tipo="nombre del parametro")
        if tipo == 'rapida':
            self._motor.inyecta_gasolina(10)
        else:
            self._motor.inyecta_gasolina(3)

        self._estado = 'en_movimiento'
        # cambiamos nuestra variable privada


class Motor:

    def __init__(self, cilindros, tipo='gasolina'):
        #Simpre se inicializa con __init__ la primera instancia de una clase
        self.cilindros = cilindros
        self.tipo = tipo
        self._temperatura = 0
        # variable privada

    def inyecta_gasolina(self, cantidad):
        pass