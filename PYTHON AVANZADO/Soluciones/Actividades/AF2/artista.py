from parametros import (AFINIDAD_HIT, AFINIDAD_INICIAL, AFINIDAD_PUBLICO_POP,
                        AFINIDAD_STAFF_POP, AFINIDAD_PUBLICO_ROCK,
                        AFINIDAD_STAFF_ROCK, AFINIDAD_PUBLICO_RAP,
                        AFINIDAD_STAFF_RAP, AFINIDAD_PUBLICO_REG,
                        AFINIDAD_STAFF_REG, AFINIDAD_ACCION_POP,
                        AFINIDAD_ACCION_ROCK, AFINIDAD_ACCION_RAP,
                        AFINIDAD_ACCION_REG, AFINIDAD_MIN, AFINIDAD_MAX)

class Artista:
    def __init__(self, nombre, genero, dia_presentacion,
                 hit_del_momento):
        self.nombre = nombre
        self.hit_del_momento = hit_del_momento
        self.genero = genero
        self.dia_presentacion = dia_presentacion
        self._afinidad_con_publico = AFINIDAD_INICIAL
        self._afinidad_con_staff = AFINIDAD_INICIAL

    @property
    def afinidad_con_publico(self):
        # COMPLETAR
        return self._afinidad_con_publico
        pass

    @afinidad_con_publico.setter
    def afinidad_con_publico(self,valor):
        if AFINIDAD_MAX >= valor >= AFINIDAD_MIN:
            self._afinidad_con_publico = valor
        elif valor < AFINIDAD_MIN:
            self._afinidad_con_publico = AFINIDAD_MIN
        elif valor > AFINIDAD_MAX:
            self._afinidad_con_publico = AFINIDAD_MAX
    
    @property
    def afinidad_con_staff(self):
        # COMPLETAR
        return self._afinidad_con_staff
        pass

    @afinidad_con_staff.setter
    def afinidad_con_staff(self, valor):
        if AFINIDAD_MAX >= valor >= AFINIDAD_MIN:
            self._afinidad_con_staff = valor
        elif valor < AFINIDAD_MIN:
            self._afinidad_con_staff = AFINIDAD_MIN
        elif valor > AFINIDAD_MAX:
            self._afinidad_con_staff = AFINIDAD_MAX

    @property
    def animo(self):
        # COMPLETAR
        return self.afinidad_con_publico * 0.5 + self.afinidad_con_staff * 0.5
        pass

    def recibir_suministros(self, suministro):
        # COMPLETAR
        self.afinidad_con_staff += suministro.valor_de_satisfaccion
        if suministro.valor_de_satisfaccion <= 0:
            print(f"{self.nombre} recibió {suministro.nombre} en malas condiciones.")
        else:
            print(f"{self.nombre} recibió un {suministro.nombre} a tiempo!")
        pass

    def cantar_hit(self):
        # COMPLETAR
        self.afinidad_con_publico += AFINIDAD_HIT
        print(f"{self.nombre} está tocando su hit: {self.hit_del_momento}!")
        pass

    def __str__(self):
        # COMPLETAR
        return f"Nombre: {self.nombre}\nGénero: {self.genero}\nÁnimo:{self.animo}"
        pass


class ArtistaPop(Artista):
    def __init__(self, *args, **kwargs):
        # COMPLETAR
        super().__init__(*args,**kwargs)
        self.accion = "Cambio de vestuario"
        self._afinidad_con_publico = AFINIDAD_PUBLICO_POP
        self._afinidad_con_staff = AFINIDAD_STAFF_POP
        pass

    def accion_especial(self):
        # COMPLETAR
        print(f"{self.nombre} hará un {self.accion}")
        self.afinidad_con_publico += AFINIDAD_ACCION_POP
        pass

    @property
    def animo(self):###
        # COMPLETAR
        if super().animo < 10:
            print(f"ArtistaPop peligrando en el concierto. Animo: {super().animo}")
        return super().animo
        pass


class ArtistaRock(Artista):
    def __init__(self, *args, **kwargs):
        # COMPLETAR
        super().__init__(*args,**kwargs)
        self.accion = "Solo de guitarra"
        self._afinidad_con_publico = AFINIDAD_PUBLICO_ROCK
        self._afinidad_con_staff = AFINIDAD_STAFF_ROCK
        pass

    def accion_especial(self):
        # COMPLETAR
        print(f"{self.nombre} hará un {self.accion}")
        self.afinidad_con_publico += AFINIDAD_ACCION_ROCK
        pass

    @property
    def animo(self):
        # COMPLETAR
        if super().animo < 5:    
            print(f"ArtistaRock peligrando en el concierto. Animo: {super().animo}")
        return super().animo
        pass


class ArtistaRap(Artista):
    def __init__(self, *args, **kwargs):
        # COMPLETAR
        super().__init__(*args,**kwargs)
        self.accion = "Doble tempo"
        self._afinidad_con_publico = AFINIDAD_PUBLICO_RAP
        self._afinidad_con_staff = AFINIDAD_STAFF_RAP
        pass

    def accion_especial(self):
        # COMPLETAR
        print(f"{self.nombre} hará un {self.accion}")
        self.afinidad_con_publico += AFINIDAD_ACCION_RAP
        pass

    @property
    def animo(self):
        # COMPLETAR
        if super().animo < 20:
            print(f"ArtistaRap peligrando en el concierto. Animo: {super().animo}")
        return super().animo
        pass


class ArtistaReggaeton(Artista):
    def __init__(self, *args, **kwargs):
        # COMPLETAR
        super().__init__(*args,**kwargs)
        self.accion = "Perrear"
        self._afinidad_con_publico = AFINIDAD_PUBLICO_REG
        self._afinidad_con_staff = AFINIDAD_STAFF_REG
        pass

    def accion_especial(self):
        # COMPLETAR
        print(f"{self.nombre} hará un {self.accion}")
        self.afinidad_con_publico += AFINIDAD_ACCION_REG
        pass

    @property
    def animo(self):
        # COMPLETAR
        if super().animo < 2:
            print(f"ArtistaReggaeton peligrando en el concierto. Animo: {super().animo}")
        return super().animo
        pass