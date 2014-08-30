# -*- coding: utf-8 -*-


from __future__ import unicode_literals

DESTRUIDO = 'Destruido'
ATIVO = 'Ativo'


class Ator():
    _caracter_ativo = 'A'
    _caracter_destruido = ' '

    def caracter(self, tempo):
        if self.status(tempo) == ATIVO:
            return self._caracter_ativo
        else:
            return self._caracter_destruido

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self._tempo_de_colisao = None

    def calcular_posicao(self, tempo):
        return self.arredondar_posicao()

    def arredondar_posicao(self):
        self.x, self.y = round(self.x), round(self.y)
        return self.x, self.y

    def colidir(self, outro_ator, tempo, intervalo=1):
        if self.status(tempo) == DESTRUIDO or outro_ator.status(tempo) == DESTRUIDO:
            return
        x1, y1 = self.arredondar_posicao()
        x2, y2 = outro_ator.arredondar_posicao()

        def esta_no_intervalo(coordenada1, coordenada2):
            coordenadas = sorted([coordenada1, coordenada2])
            return coordenadas[1] - intervalo <= coordenadas[0]

        if esta_no_intervalo(x1, x2) and esta_no_intervalo(y1, y2):
            self._tempo_de_colisao = tempo
            outro_ator._tempo_de_colisao = tempo

    def status(self, tempo):
        if self._tempo_de_colisao is None or self._tempo_de_colisao > tempo:
            return ATIVO
        return DESTRUIDO


class Obstaculo(Ator):
    _caracter_ativo = 'O'


class Porco(Ator):
   _caracter_ativo = '@'
   _caracter_destruido = '+'


class Passaro(Ator):
    pass


class PassaroAmarelo(Passaro):
    pass


class PassaroVermelho(Passaro):
    pass


# ob = Obstaculo()
# print(ob.x)
# print(ob._caracter_ativo)
# print(ob._caracter_destruido)
# print(Ator._caracter_ativo)


# print(Ator._caracter_ativo)
# renzo = Ator()
# print(renzo.colidir(None,None))
# print("nada, "+renzo._caracter_destruido)
# renzo._caracter_destruido='D'
# print("nada, "+renzo._caracter_destruido)
# print('vazio, '+Ator._caracter_destruido)
# print(type(renzo))
# renzo.x=0
# print(renzo.x)
# andre=Ator()
# print(type(andre))
# print(andre.x)
