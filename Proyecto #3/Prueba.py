import json
import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QComboBox, QPushButton, QListWidget, QMessageBox
from PyQt5.QtCore import Qt
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment


class Mesero:
    def __init__(self, nombre_usuario, contrasena):
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena

def autenticar_mesero(usuario, contrasena):
    mesero_admin = Mesero("", "")
    return usuario == mesero_admin.nombre_usuario and contrasena == mesero_admin.contrasena

class VentanaInicioSesion(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Iniciar Sesión - Restaurante Jake's Monkey")
        self.setGeometry(300, 100, 600, 400)
        self.setStyleSheet("background-color: #FFFFFF; color: #FFFFFF;")
        layout = QVBoxLayout()

        self.nombre_label = QLabel('Nombre del miembro del staff:')
        self.nombre_entry = QLineEdit()
        self.nombre_entry.setStyleSheet("background-color: #444444; color: #FFFFFF;")
        layout.addWidget(self.nombre_label)
        layout.addWidget(self.nombre_entry)

        self.contrasena_label = QLabel('Contraseña:')
        self.contrasena_entry = QLineEdit()
        self.contrasena_entry.setEchoMode(QLineEdit.Password)
        self.contrasena_entry.setStyleSheet("background-color: #444444; color: #FFFFFF;")
        layout.addWidget(self.contrasena_label)
        layout.addWidget(self.contrasena_entry)

        iniciar_sesion_button = QPushButton('Iniciar Sesión')
        iniciar_sesion_button.clicked.connect(self.iniciar_sesion)
        layout.addWidget(iniciar_sesion_button)

        self.setLayout(layout)

    def iniciar_sesion(self):
        nombre_ingresado = self.nombre_entry.text()
        contrasena_ingresada = self.contrasena_entry.text()

        if autenticar_mesero(nombre_ingresado, contrasena_ingresada):
            print("¡Inicio de sesión exitoso! Puedes acceder al restaurante.")
            self.ventana_principal = VentanaPrincipal()  # Crear la ventana principal
            self.ventana_principal.show()  # Mostrar la ventana principal
            self.close()  # Cierra la ventana actual después del inicio de sesión exitoso
        else:
            QMessageBox.warning(self, 'Error', 'Nombre de usuario o contraseña incorrectos')

class VentanaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana Principal - Restaurante Jake's Monkey")
        self.setGeometry(300, 100, 800, 500)
        self.setStyleSheet("background-color: #333333; color: #FFFFFF;")
        layout = QVBoxLayout()

        label = QLabel('¡Bienvenido! Esta es la ventana principal.')
        layout.addWidget(label)

        self.setLayout(layout)

def main():
    app = QApplication(sys.argv)
    ventana_inicio = VentanaInicioSesion()
    ventana_inicio.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

    def menu_login(self):
        # Lógica para mostrar el menú de login para el mesero
        pass

    def tomar_pedidos(self):
        # Lógica para tomar los pedidos de los clientes
        pass

class Cocina:
    def preparar_comidas(self):
        # Lógica para recibir pedidos, preparar platos y marcar los pedidos como completados
        pass

class SistemaRestaurante:
    def gestion_pedidos(self):
        # Lógica para recibir, procesar y rastrear pedidos realizados por los meseros
        pass

    def facturacion_pagos(self):
        # Lógica para gestionar la facturación de pedidos, separado por mesa
        pass