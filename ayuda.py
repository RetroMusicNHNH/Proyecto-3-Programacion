
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QMenu, QAction, QLabel

class MiVentana(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Ejemplo PyQt5')
        self.setGeometry(100, 100, 400, 300)

        self.layout = QVBoxLayout()

        # Botón para mostrar opciones
        self.btn_mostrar_opciones = QPushButton('Mostrar Opciones', self)
        self.btn_mostrar_opciones.clicked.connect(self.mostrar_opciones)
        self.layout.addWidget(self.btn_mostrar_opciones)

        # Botón GENERAR
        self.btn_generar = QPushButton('GENERAR', self)
        self.btn_generar.clicked.connect(self.mostrar_menu_generar)
        self.layout.addWidget(self.btn_generar)
        self.btn_generar.hide()

        # Etiqueta para mostrar opciones seleccionadas
        self.label_opciones_seleccionadas = QLabel(self)
        self.layout.addWidget(self.label_opciones_seleccionadas)

        self.setLayout(self.layout)

    def mostrar_opciones(self):
        menu = QMenu(self)

        opcion1 = QAction('Opción 1', self)
        opcion1.triggered.connect(lambda: self.opcion_seleccionada('Opción 1'))

        opcion2 = QAction('Opción 2', self)
        opcion2.triggered.connect(lambda: self.opcion_seleccionada('Opción 2'))

        opcion3 = QAction('Opción 3', self)
        opcion3.triggered.connect(lambda: self.opcion_seleccionada('Opción 3'))

        menu.addAction(opcion1)
        menu.addAction(opcion2)
        menu.addAction(opcion3)

        # Muestra el menú en la posición del botón
        menu.exec_(self.btn_mostrar_opciones.mapToGlobal(self.btn_mostrar_opciones.rect().bottomLeft()))

    def opcion_seleccionada(self, opcion):
        self.label_opciones_seleccionadas.setText(f'Opción seleccionada: {opcion}')

    def mostrar_menu_generar(self):
        # Aquí puedes agregar la lógica para modificar tamaño y posición
        print("Menú GENERAR")

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    ventana = MiVentana()
    ventana.show()
    sys.exit(app.exec_())