# encoding: utf-8
import sys
import image_tools

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QApplication, QGridLayout, QLabel, QAction, qApp,
                             QFileDialog, QPushButton, QMainWindow,
                             QWidget, QSpinBox)

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Compress4D'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.dim_input = None
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.init_layout()

        self.show()

    def init_layout(self):
        # Layout generation #
        main_widget = QWidget()
        grid = QGridLayout()
        grid.setSpacing(10)
        main_widget.setLayout(grid)

        # Random matrix generation widgets #
        random_label = QLabel("Crea una imagen 4D aleatoria simétrica con el siguiente tamaño:")
        self.dim_input = QSpinBox()
        self.dim_input.setRange(1, 10)
        random_btn = QPushButton("Generar matriz", main_widget)
        random_btn.clicked.connect(self.random_click)

        # File load widgets #
        file_label = QLabel("O carga un fichero con la imagen 4D")
        file_btn = QPushButton("Cargar...", main_widget)
        file_btn.clicked.connect(self.open_file_dialog)

        # Grid widgets positioning #
        grid.addWidget(random_label, 0, 0)
        grid.addWidget(self.dim_input, 0, 1)
        grid.addWidget(random_btn, 0, 2)

        grid.addWidget(file_label, 1, 0, 1, 1)
        grid.addWidget(file_btn, 1, 2)

        # Menubar actions #
        exit_action = QAction(QIcon("exit.png"), "Salir", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.setStatusTip("Salir de la aplicación")
        exit_action.triggered.connect(qApp.quit)

        # Menubar configuration #
        menubar = self.menuBar()
        file_menu = menubar.addMenu("&Archivo")
        file_menu.addAction(exit_action)

        self.setCentralWidget(main_widget)

    @staticmethod
    def open_file_dialog():
        file_name = QFileDialog.getOpenFileName(caption="Abrir archivo")
        path = file_name[0]

        if path:
            image = image_tools.load_image(path)
            # TODO: Finish this method

    @staticmethod
    def random_click():
        image = image_tools.generate_random_img()
        # TODO: Process the generated matrix


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
