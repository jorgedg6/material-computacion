import sys
from PyQt5.QtWidgets import QApplication

#Import Frontend
from frontend.ventana_inicio import VentanaInicio
from frontend.ventana_ranking import VentanaRankings
from frontend.ventana_principal import VentanaPrincipal
from frontend.ventana_juego import VentanaJuego
from frontend.ventana_post_juego import VentanaPostJuego

#Import Backend
from backend.logica_principal import LogicaPrincipal
from backend.logica_juego import LogicaJuego
from backend.logica_post_juego import LogicaPostJuego

if __name__ == '__main__':
    def hook(type, value, traceback):
        print(traceback)
    sys.__excepthook__ = hook
    app = QApplication([])

    # Instanciación de ventanas
    ventana_inicio = VentanaInicio()
    ventana_ranking = VentanaRankings()
    ventana_principal = VentanaPrincipal()
    ventana_juego = VentanaJuego()
    ventana_post_juego = VentanaPostJuego()

    #Instanciación de logica
    logica_principal = LogicaPrincipal()
    logica_juego = LogicaJuego()
    logica_post_juego = LogicaPostJuego()

    #-- SEÑALES --

    #VENTANA INICIO ->
    # -> Ventana Ranking
    ventana_inicio.senal_ranking.connect(
        ventana_ranking.mostrar_ventana
    )
    # -> Ventana Principal
    ventana_inicio.senal_jugar.connect(
        ventana_principal.mostrar_ventana
    )

    #VENTANA PRINCIPAL ->
    # -> Ventana Inicio
    ventana_ranking.senal_volver.connect(
        ventana_inicio.mostrar_ventana
    )
    # -> Logica Principal
    ventana_principal.senal_enviar_usuario.connect(
        logica_principal.chequear_datos
    )

    #LOGICA PRINCIPAL ->
    # -> Ventana Principal
    logica_principal.senal_error.connect(
        ventana_principal.pop_error
    )
    # -> Ventana Juego
    logica_principal.senal_iniciar.connect(
        ventana_juego.mostrar_ventana
    )
    # -> Logica Juego
    logica_principal.senal_iniciar.connect(
        logica_juego.crear_aliens
    )
    logica_principal.senal_iniciar.connect(
        logica_juego.crear_mira
    )
    logica_principal.senal_iniciar.connect(
        logica_juego.iniciar_timers
    )

    #VENTANA JUEGO ->
    # -> Logica Juego
    ventana_juego.senal_tecla.connect(
        logica_juego.mover_mira
    )
    ventana_juego.senal_disparo.connect(
        logica_juego.disparar_mira
    )
    ventana_juego.senal_pausa.connect(
        logica_juego.pausar
    )
    ventana_juego.senal_cheat.connect(
        logica_juego.chequeo_cheat
    )
    ventana_juego.senal_salir.connect(
        logica_post_juego.escribir
    )
    ventana_juego.senal_salir.connect(
        app.exit
    )
    #LOGICA JUEGO ->
    # -> Ventana Juego
    logica_juego.senal_enviar_aliens.connect(
        ventana_juego.conectar_aliens
    )
    logica_juego.senal_enviar_mira.connect(
        ventana_juego.conectar_mira
    )
    logica_juego.senal_balas.connect(
        ventana_juego.actualizar_balas
    )
    logica_juego.senal_actualizar_tiempo.connect(
        ventana_juego.actualizar_tiempo
    )
    logica_juego.senal_cerrar_ventana.connect(
        ventana_juego.cerrar_ventana
    )
    logica_juego.senal_label_termino.connect(
        ventana_juego.actualizar_label_termino
    )
    logica_juego.senal_post_juego.connect(
        ventana_juego.cerrar_ventana
    )
    logica_juego.senal_post_juego.connect(
        ventana_post_juego.mostrar_ventana
    )

    ventana_post_juego.senal_escritura.connect(
        logica_post_juego.escribir
    )
    ventana_post_juego.senal_escritura.connect(
        app.exit
    )
    ventana_post_juego.senal_continuar.connect(
        ventana_juego.nuevo_nivel
    )
    ventana_post_juego.senal_continuar.connect(
        logica_juego.nuevo_nivel
    )
    logica_juego.senal_pasar_nivel.connect(
        ventana_juego.nuevo_nivel
    )
    logica_principal.senal_confirmacion.connect(
        ventana_principal.cerrar_ventana
    )
    logica_juego.senal_cambio_puntaje.connect(
        ventana_juego.cambiar_puntaje
    )
    logica_juego.senal_animacion_terminator_dog.connect(
        ventana_juego.animacion_terminator_dog
    )
    logica_juego.senal_reset_sprite.connect(
        ventana_juego.reset_terminator_dog
    )
#Ejecución
    app.exec()