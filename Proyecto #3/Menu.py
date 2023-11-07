import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QGraphicsDropShadowEffect, QLineEdit, QVBoxLayout
from PyQt5.QtGui import QColor, QPixmap, QIcon, QFont
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QTimer


    ########################################################################
    # Funciones de cambio y restauración de color del botón
    ########################################################################

    
def change_color_boton1():
    boton.setStyleSheet("background-color: #81c43b; border-radius: 5%; color: black; font: bold 12px; font-family: Arial")

def restore_color_boton1():
    boton.setStyleSheet("background-color: #0094FF; border-radius: 5%; color: white; font: bold 12px; font-family: Arial")

def change_color_boton2():
    boton2.setStyleSheet("background-color: #81c43b; border-radius: 5%; color: black; font: bold 12px; font-family: Arial")

def restore_color_boton2():
    boton2.setStyleSheet("background-color: #0094FF; border-radius: 5%; color: white; font: bold 12px; font-family: Arial")


    ########################################################################
    # Funciones donde se da las opciones del las paginas
    ########################################################################
    
def actualizar_pagina1():
    global titulo_nueva_ventana
    if titulo_nueva_ventana:
        titulo_nueva_ventana.setText("Aqui la mierda del primero")
        titulo_nueva_ventana.setStyleSheet("font: bold 42px; font-family: Arial")

        # Define la posición de inicio para los botones
        start_x = 150
        start_y = 70

        button_width = 200
        button_height = 160
        button_spacing_x = 30  # Espacio horizontal
        button_spacing_y = 50  # Espacio vertical
        
        ruta_icono_comun = r"C:\Users\Jake\Desktop\Proyecto #3\iconos\mesaG.png"  # Ruta del icono que se aplicará a todos los botones

        for fila in range(3):  # Iterar sobre 3 filas
            for columna in range(4):  # 4 botones en cada fila
                # Crea los botones
                boton_nueva_ventana = QPushButton(f' {fila * 4 + columna + 1}', nueva_ventana)
                boton_nueva_ventana.setGeometry(start_x + columna * (button_width + button_spacing_x),
                                               start_y + fila * (button_height + button_spacing_y),
                                               button_width, button_height)
                
                # Establece un color específico para los botones
                boton_nueva_ventana.setStyleSheet("background-color: #0798F2; border-radius: 15%; color: white; font: bold 40px; font-family: Arial")

                # Carga el icono y redimensiona
                icono = QIcon(ruta_icono_comun)
                icono_redimensionado = icono.pixmap(80, 80)

                # Asigna el icono redimensionado a los botones
                boton_nueva_ventana.setIcon(QIcon(icono_redimensionado))
                boton_nueva_ventana.setIconSize(icono_redimensionado.rect().size())

                # Conecta los botones a alguna función si es necesario
                # boton_nueva_ventana.clicked.connect(tu_funcion)

                boton_nueva_ventana.show()
                

def actualizar_pagina2():
    global titulo_nueva_ventana
    if titulo_nueva_ventana:
        titulo_nueva_ventana.setText("La del segundo")

def actualizar_pagina3():
    global titulo_nueva_ventana
    if titulo_nueva_ventana:
        titulo_nueva_ventana.setText("lo mismo de la tercera")

def actualizar_pagina4():
    global titulo_nueva_ventana
    if titulo_nueva_ventana:
        titulo_nueva_ventana.setText("y la cuerta de negecia")

def actualizar_pagina5():
    global titulo_nueva_ventana
    if titulo_nueva_ventana:
        titulo_nueva_ventana.setText("La ultima porfiiiiin")
        
        
        
    ########################################################################
    # Funcion cuando la ventada de login se cierra y abra
    ########################################################################

def cerrar_ventanas():
    ventana_principal.close()

def abrir_nueva_ventana():
    global titulo_nueva_ventana  
    usuario = entrada_usuario.text()
    contrasena = entrada_contrasena.text()

    if usuario == '' and contrasena == '':
        global nueva_ventana
        nueva_ventana = QWidget()
        nueva_ventana.setWindowIcon(QIcon(r"C:\Users\Jake\Desktop\Proyecto #3\monkey.ico"))
        nueva_ventana.setWindowTitle("Monkey's Garden Oasis: Sabores Saludables de la Selva")
        nueva_ventana.setGeometry(0, 0, 1080, 720)  # Tamaño 1080 x 720
        nueva_ventana.setStyleSheet("background-color: #171B26")

        global titulo_nueva_ventana
        titulo_nueva_ventana = QLabel("BIENVENIDO AL\nGESTOR DEL\nRESTAURANTE", nueva_ventana)
        titulo_nueva_ventana.setStyleSheet("font: bold 100px; font-family: Arial; color: white")
        titulo_nueva_ventana.setGeometry(200, 20, 800, 500)  # Ajusta las coordenadas y tamaño según sea necesario

        rutas_imagenes = [
        r"C:\Users\Jake\Desktop\Proyecto #3\iconos\orden.png",
        r"C:\Users\Jake\Desktop\Proyecto #3\iconos\tarjeta.png",
        r"C:\Users\Jake\Desktop\Proyecto #3\iconos\grafico.png",
        r"C:\Users\Jake\Desktop\Proyecto #3\iconos\carrito.png",
        r"C:\Users\Jake\Desktop\Proyecto #3\iconos\menu.png"
        ]

        actualizar_funciones = [actualizar_pagina1, actualizar_pagina2,actualizar_pagina3 ,actualizar_pagina4, actualizar_pagina5]  # Agrega las otras funciones de actualización

        for i in range(5):  # Crea dos botones (actualiza según el número de funciones)
            boton_nueva_ventana = QPushButton('', nueva_ventana)
            boton_nueva_ventana.setGeometry(0, 144 * i, 120, 150)

            icono = QPixmap(rutas_imagenes[i])
            icono_redimensionado = icono.scaled(80, 80)
            boton_nueva_ventana.setIcon(QIcon(icono_redimensionado))
            boton_nueva_ventana.setIconSize(icono_redimensionado.rect().size())
            boton_nueva_ventana.setStyleSheet("background-color: #1C3659;")
            boton_nueva_ventana.clicked.connect(actualizar_funciones[i])

            boton_nueva_ventana.show()

        ventana_principal.hide()
        nueva_ventana.show()
        QTimer.singleShot(3000, cerrar_ventanas)
    else:
        print("Credenciales incorrectas")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    ########################################################################
    # Ventana Principal
    ########################################################################
    ventana_principal = QWidget()
    ventana_principal.setWindowTitle("Monkey's Garden Oasis: Sabores Saludables de la Selva")
    ventana_principal.setWindowIcon(QIcon(r"C:\Users\Jake\Desktop\Proyecto #3\monkey.ico"))
    ventana_principal.setGeometry(350, 100, 600, 400)
    ventana_principal.setStyleSheet("background-color: #171B26;")
    
    

    ########################################################################
    # Etiqueta con imagen
    ########################################################################
    label = QLabel(ventana_principal)
    pixmap = QPixmap(r"C:\Users\Jake\Desktop\Proyecto #3\img\IMG2.PNG")
    label.setPixmap(pixmap)
    label.setGeometry(255, 0, 350, 400)
    
    ########################################################################
    # Boton ver menu
    ########################################################################
    boton = QPushButton('Ver Menú', ventana_principal)
    boton.setStyleSheet("background-color: #0094FF; border-radius: 5%; color: white; font: bold 12px; font-family: Arial")
    boton.setGeometry(62, 100, 130, 25)

    ########################################################################
    # Etiqueta "Nombre de Usuario" y campo de entrada de texto para el usuario
    ########################################################################

    titulo_usuario = QLabel('Nombre de Usuario:', ventana_principal)
    titulo_usuario.setStyleSheet("background: transparent;color: white; font: bold 12px; font-family: Arial")
    titulo_usuario.setGeometry(62, 170, 200, 20)

    entrada_usuario = QLineEdit(ventana_principal)
    entrada_usuario.setStyleSheet("background-color: #D9D9D9; color: #000000; font: Arial")
    entrada_usuario.setGeometry(62, 200, 130, 25)

    ########################################################################
    # Etiqueta "Contraseña" y campo de entrada de texto para la contraseña
    ########################################################################

    titulo_contrasena = QLabel('Contraseña:', ventana_principal)
    titulo_contrasena.setStyleSheet("background: transparent;color: white; font: bold 12px; font-family: Arial")
    titulo_contrasena.setGeometry(62, 230, 200, 20)

    entrada_contrasena = QLineEdit(ventana_principal)
    entrada_contrasena.setEchoMode(QLineEdit.Password)
    entrada_contrasena.setStyleSheet("background-color: #D9D9D9; color: #000000; font: Arial")
    entrada_contrasena.setGeometry(62, 250, 130, 25)
    
    ########################################################################
    # Boton iniciar Secion
    ########################################################################
    boton2 = QPushButton('Iniciar Seccion', ventana_principal)
    boton2.setStyleSheet("background-color: #0094FF; border-radius: 5%; color: white; font: bold 12px; font-family: Arial")
    boton2.setGeometry(62, 300, 130, 25)

    ########################################################################
    # Conectar la funcionalidad de cambio y restauración de color del botón
    ########################################################################

    boton.pressed.connect(change_color_boton1)
    boton.released.connect(restore_color_boton1)
    
    boton2.pressed.connect(change_color_boton2)
    boton2.released.connect(restore_color_boton2)
    
    boton2.clicked.connect(abrir_nueva_ventana)

    ########################################################################
    # Mostrar la ventana principal y ejecutar la aplicación
    ########################################################################

    # Mostrar la ventana principal
    ventana_principal.show()

    # Ejecutar la aplicación
    sys.exit(app.exec_())