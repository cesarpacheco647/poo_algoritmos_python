class Lavadora:
# inicio de clase
    def __init__(self):
        #declaramos primera funcion con __init__ y siempre usamos el parametro self
        pass
        # pasamos  con pass

    def lavar(self, temperatura='caliente'):#parametro de default
        #declaramos nuestro primer metodo publico
        self._llenar_tanque_de_agua(temperatura) #llenar el tanque con la temperatura parametro en default
        #variable privada
        self._anadir_jabon()
        #variable privada
        self._lavar()
        #variable privada
        self._centrifugar()
        #variable privada

    def _llenar_tanque_de_agua(self, temperatura):
        #metodo privado _
        print(f'Llenando el tanque con agua {temperatura}')
        #concatenacion (interpolacion)

    def _anadir_jabon(self):
        #privada _
        print('Anadiendo jabon')

    def _lavar(self):
        #diferente por una ser un metodo publica y esta privada
        print('Lavando la ropa')

    def _centrifugar(self):
        #funcion privada _
        print('Centrifugando la ropa')


if __name__ == '__main__':
    #entry point
    lavadora = Lavadora()
    lavadora.lavar()