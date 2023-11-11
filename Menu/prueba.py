import sys
import json
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QMainWindow
from PyQt5.QtGui import QPixmap

class MenuWindow(QMainWindow):
    def __init__(self, menu_data):
        super().__init__()
        self.menu = menu_data
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Menú del Restaurante')
        layout = QVBoxLayout()

        for category, items in self.menu.items():
            layout.addWidget(QLabel(f'{category.capitalize()}:'))
            for item in items:
                button = QPushButton(f'{item["nombre"]} - ${item["precio"]}')
                button.clicked.connect(lambda checked, x=item: self.show_item_details(x))
                layout.addWidget(button)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.setGeometry(100, 100, 400, 400)
        self.show()

    def show_item_details(self, item):
        details = f'Detalles de {item["nombre"]} - Precio: ${item["precio"]}, Ingredientes: {", ".join(item["ingredientes"])}'
        print(details)
        # Cargar y mostrar la imagen
        if "imagen" in item:
            image_path = item["imagen"]
            pixmap = QPixmap(image_path)
            if not pixmap.isNull():
                label = QLabel()
                label.setPixmap(pixmap)
                label.show()

def load_menu_from_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        menu_data = json.load(file)
    return menu_data

def run_app():
    app = QApplication(sys.argv)
    menu_path = r"C:\\Users\\Jake\\Desktop\\Proyecto #3\\Menu\\menu.json"
    menu = load_menu_from_json(menu_path)
    window = MenuWindow(menu)
    sys.exit(app.exec_())

if __name__ == '__main__':
    run_app()
