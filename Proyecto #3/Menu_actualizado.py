#POO

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QTimer, Qt


class MiAplicacion(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Monkey's Garden Oasis: Sabores Saludables de la Selva")
        self.setGeometry(350, 100, 600, 400)
        self.setStyleSheet("background-color: #171B26;")

        self.initUI()


#Configuración de una imagen en la interfaz gráfica:  
############################################################################
    def initUI(self):                                                      #
        label = QLabel(self)                                               #
        pixmap = QPixmap("C:/Users/Jake/Desktop/Proyecto #3/img/IMG2.PNG") # 
        label.setPixmap(pixmap)                                            #
        label.setGeometry(255, 0, 350, 400)                                #
                                                                           #
############################################################################


#Creación de widgets y elementos interactivos:
#########################################################################################################################################
                                                                                                                                        #
        self.boton = QPushButton('Ver Menú', self)                                                                                      #
        self.boton.setStyleSheet("background-color: #0094FF; border-radius: 5%; color: white; font: bold 12px; font-family: Arial")     #
        self.boton.setGeometry(62, 100, 130, 25)                                                                                        #
        self.boton.pressed.connect(self.change_color_boton1)                                                                            #
        self.boton.released.connect(self.restore_color_boton1)                                                                          #
                                                                                                                                        #
        titulo_usuario = QLabel('Nombre de Usuario:', self)                                                                             #
        titulo_usuario.setStyleSheet("background: transparent;color: white; font: bold 12px; font-family: Arial")                       #
        titulo_usuario.setGeometry(62, 170, 200, 20)                                                                                    #
                                                                                                                                        #
        self.entrada_usuario = QLineEdit(self)                                                                                          #
        self.entrada_usuario.setStyleSheet("background-color: #D9D9D9; color: #000000; font: Arial")                                    #
        self.entrada_usuario.setGeometry(62, 200, 130, 25)                                                                              #
                                                                                                                                        #
        titulo_contrasena = QLabel('Contraseña:', self)                                                                                 #
        titulo_contrasena.setStyleSheet("background: transparent;color: white; font: bold 12px; font-family: Arial")                    #
        titulo_contrasena.setGeometry(62, 230, 200, 20)                                                                                 #
                                                                                                                                        #
        self.entrada_contrasena = QLineEdit(self)                                                                                       #
        self.entrada_contrasena.setEchoMode(QLineEdit.Password)                                                                         #
        self.entrada_contrasena.setStyleSheet("background-color: #D9D9D9; color: #000000; font: Arial")                                 #
        self.entrada_contrasena.setGeometry(62, 250, 130, 25)                                                                           #
                                                                                                                                        #
        self.boton2 = QPushButton('Iniciar Sesión', self)                                                                               #
        self.boton2.setStyleSheet("background-color: #0094FF; border-radius: 5%; color: white; font: bold 12px; font-family: Arial")    #
        self.boton2.setGeometry(62, 300, 130, 25)                                                                                       #
        self.boton2.pressed.connect(self.change_color_boton2)                                                                           #
        self.boton2.released.connect(self.restore_color_boton2)                                                                         #
        self.boton2.clicked.connect(self.abrir_nueva_ventana)                                                                           #
                                                                                                                                        #
#########################################################################################################################################
        
#Mostrar la ventana
########################
        self.show()    #
########################
        

# Funciones de cambio y restauración de color del botón
########################################################################################################################################
    def change_color_boton1(self):                                                                                                     #
        self.boton.setStyleSheet("background-color: #81c43b; border-radius: 5%; color: black; font: bold 12px; font-family: Arial")    #
                                                                                                                                       #
    def restore_color_boton1(self):                                                                                                    #
        self.boton.setStyleSheet("background-color: #0094FF; border-radius: 5%; color: white; font: bold 12px; font-family: Arial")    #
                                                                                                                                       #
    def change_color_boton2(self):                                                                                                     #
        self.boton2.setStyleSheet("background-color: #81c43b; border-radius: 5%; color: black; font: bold 12px; font-family: Arial")   #
                                                                                                                                       # 
    def restore_color_boton2(self):                                                                                                    #
        self.boton2.setStyleSheet("background-color: #0094FF; border-radius: 5%; color: white; font: bold 12px; font-family: Arial")   #
                                                                                                                                       #
########################################################################################################################################
        

#cierra la ventana de mi aplicaccion
###############################
    def cerrar_ventanas(self):#
        self.close()          #
###############################
        
    def abrir_nueva_ventana(self):         
#Obtener la información del usuario y contraseña:
#####################################################
        usuario = self.entrada_usuario.text()       #
        contrasena = self.entrada_contrasena.text() #
#####################################################


#Verifica la contrasena y usuario
###############################################
        if usuario == '' and contrasena == '':#
###############################################


#Si las credenciales son válidas esto abre una nueva ventana
##############################################################################################################
            self.nueva_ventana = QWidget()                                                                   # 
            self.nueva_ventana.setWindowIcon(QIcon("C:/Users/Jake/Desktop/Proyecto #3/monkey.ico"))          #
            self.nueva_ventana.setWindowTitle("Monkey's Garden Oasis: Sabores Saludables de la Selva")       #
            self.nueva_ventana.setGeometry(0, 0, 1080, 720)                                                  #
            self.nueva_ventana.setStyleSheet("background-color: #171B26")                                    #
            self.titulo_nueva_ventana = QLabel("BIENVENIDO AL\nGESTOR DEL\nRESTAURANTE", self.nueva_ventana) #
            self.titulo_nueva_ventana.setStyleSheet("font: bold 100px; font-family: Arial; color: white")    #
            self.titulo_nueva_ventana.setGeometry(200, 20, 800, 500)                                         #
                                                                                                             # 
            rutas_imagenes = [                                                                               #
                "C:/Users/Jake/Desktop/Proyecto #3/iconos/orden.png",                                        #
                "C:/Users/Jake/Desktop/Proyecto #3/iconos/tarjeta.png",                                      #
                "C:/Users/Jake/Desktop/Proyecto #3/iconos/grafico.png",                                      #
                "C:/Users/Jake/Desktop/Proyecto #3/iconos/carrito.png",                                      #
                "C:/Users/Jake/Desktop/Proyecto #3/iconos/menu.png"                                          #
            ]                                                                                                #
##############################################################################################################



#lista que contiene referencias a diferentes métodos que se encargarán de actualizar la información mostrada en la nueva ventana.
#################################################################################################################################################################
            actualizar_funciones = [self.actualizar_pagina1, self.actualizar_pagina2, self.actualizar_pagina3, self.actualizar_pagina4, self.actualizar_pagina5]#
#################################################################################################################################################################


#Configuración de botones en la nueva ventana
##############################################################################################
            for i in range(5):                                                               #
                boton_nueva_ventana = QPushButton('', self.nueva_ventana)                    #
                boton_nueva_ventana.setGeometry(0, 144 * i, 120, 150)                        #
                                                                                             #
                icono = QPixmap(rutas_imagenes[i])                                           #
                icono_redimensionado = icono.scaled(80, 80)                                  #
                boton_nueva_ventana.setIcon(QIcon(icono_redimensionado))                     #
                boton_nueva_ventana.setIconSize(icono_redimensionado.rect().size())          #
                boton_nueva_ventana.setStyleSheet("background-color: #1C3659;")              #
                boton_nueva_ventana.clicked.connect(actualizar_funciones[i])                 #
                                                                                             #
                boton_nueva_ventana.show()                                                   #
##############################################################################################

#Mostrar y manipular las ventanas
##########################################################
            self.hide()                                  #
            self.nueva_ventana.show()                    #
            QTimer.singleShot(3000, self.cerrar_ventanas)#
        else:                                            #
            print("Credenciales incorrectas")            #
##########################################################


# Funciones donde se da las opciones del las paginas
########################################################################

    def actualizar_pagina1(self):
        if self.titulo_nueva_ventana:
            self.titulo_nueva_ventana.setText("Aqui la mierda del primero")
            self.titulo_nueva_ventana.setStyleSheet("font: bold 42px; font-family: Arial")

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
                    boton_nueva_ventana = QPushButton(f' {fila * 4 + columna + 1}', self.nueva_ventana)  # Utiliza self.nueva_ventana
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
                    

    def actualizar_pagina2(self):
        if self.titulo_nueva_ventana:
            self.titulo_nueva_ventana.setText("La del segundo")


    def actualizar_pagina3(self):
        if self.titulo_nueva_ventana:
            self.titulo_nueva_ventana.setText("lo mismo de la tercera")


    def actualizar_pagina4(self):
        if self.titulo_nueva_ventana:
            self.titulo_nueva_ventana.setText("y la cuerta de negecia")


    def actualizar_pagina5(self):
        if self.titulo_nueva_ventana:
            self.titulo_nueva_ventana.setText("La ultima porfiiiiin")


#Lo ejecuta
#########################################
if __name__ == '__main__':              #
    app = QApplication(sys.argv)        #
    ventana_principal = MiAplicacion()  #
    sys.exit(app.exec_())               #
#########################################
