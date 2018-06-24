# encoding: utf-8
import sys
from src import image_tools, compressor

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QApplication, QGridLayout, QStackedWidget,
                             QLabel, QAction, qApp, QTabWidget,
                             QFileDialog, QPushButton, QMainWindow,
                             QWidget, QSpinBox, QVBoxLayout,
                             QTextBrowser)
from PyQt5.QtCore import QObject, QThread, pyqtSignal, pyqtSlot


class ProcessingWorker(QObject):
    done_sig = pyqtSignal(tuple)

    def __init__(self, m_size, matrix):
        super().__init__()
        self.__abort = False
        self.m_size = m_size
        self.matrix = matrix

    @pyqtSlot()
    def work(self):
        # result = compressor.csr(self.m_size, self.matrix, self.__abort)
        result = compressor.csr(self.m_size, self.matrix)
        self.done_sig.emit(result)

    @pyqtSlot()
    def abort(self):
        self.__abort = True


class MatrixInputWidget(QWidget):
    abort_sig = pyqtSignal()
    wk_sig_done = pyqtSignal(tuple)

    def __init__(self):
        super().__init__()
        # Widget variables #
        self.dim_input = None
        self.m_size = None
        self.matrix = None
        self.processing_btn = None
        self.stop_btn = None
        self.__threads = list()
        self.init_layout()

    def init_layout(self):
        # Widget layout #
        grid = QGridLayout()
        grid.setSpacing(10)
        self.setLayout(grid)

        # Random matrix generation widgets #
        random_label = QLabel("Crea una imagen 4D aleatoria simétrica "
                              "con el siguiente tamaño:")
        self.dim_input = QSpinBox()
        self.dim_input.setRange(1, 10)
        random_btn = QPushButton("Generar matriz", self)
        random_btn.clicked.connect(self.random_click)

        # File load widgets #
        file_label = QLabel("O carga un fichero con la imagen 4D")
        file_btn = QPushButton("Cargar...")
        file_btn.clicked.connect(self.open_file_dialog)

        # Processing widgets #
        self.processing_btn = QPushButton("Iniciar compresión")
        self.processing_btn.setDisabled(True)
        self.processing_btn.clicked.connect(self.do_processing)
        self.stop_btn = QPushButton("Detener compresión")
        self.stop_btn.setDisabled(True)
        self.stop_btn.clicked.connect(self.abort_processing)

        # Grid widgets positioning #
        grid.addWidget(random_label, 0, 0)
        grid.addWidget(self.dim_input, 0, 1)
        grid.addWidget(random_btn, 0, 2)

        grid.addWidget(file_label, 1, 0, 1, 1)
        grid.addWidget(file_btn, 1, 2)

        grid.addWidget(self.stop_btn, 2, 2)
        grid.addWidget(self.processing_btn, 2, 1)

    def open_file_dialog(self):
        file_name = QFileDialog.getOpenFileName(caption="Abrir archivo")
        path = file_name[0]

        if path:
            try:
                self.m_size, self.matrix = image_tools.load_image(path)
                self.processing_btn.setEnabled(True)
            except:
                pass

    def random_click(self):
        self.m_size = self.dim_input.value()
        self.matrix = image_tools.generate_random_img(shape=self.m_size)
        self.processing_btn.setEnabled(True)

    def do_processing(self):
        self.processing_btn.setDisabled(True)
        self.stop_btn.setEnabled(True)
        worker = ProcessingWorker(self.m_size, self.matrix)
        thread = QThread()
        self.__threads.append((thread, worker))
        worker.moveToThread(thread)

        worker.done_sig.connect(self.on_processing_done)
        self.abort_sig.connect(worker.abort)

        thread.started.connect(worker.work)
        thread.start()

    def abort_processing(self):
        self.abort_sig.emit()
        for thread, worker in self.__threads:
            thread.quit()
            thread.wait()
        self.__threads = list()

    @pyqtSlot(tuple)
    def on_processing_done(self, results: tuple):
        self.wk_sig_done.emit(results)
        self.processing_btn.setEnabled(True)
        self.stop_btn.setDisabled(True)
        self.__threads = list()


class ResultsWidget(QWidget):
    go_input_sig = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.base_layout = QVBoxLayout()
        self.tab_layout = QTabWidget()
        self.init_layout()

    def init_layout(self):
        # Layout setup #
        self.setLayout(self.base_layout)
        self.base_layout.addWidget(self.tab_layout)

        # Tabs creation #
        """
        At the first program execution no results will be available, but tabs
        need to be created with a QWidget. We populate them with a base string.
        """
        self.init_tabs()

        # Return button #
        back_btn = QPushButton("Volver")
        self.base_layout.addWidget(back_btn)
        back_btn.clicked.connect(self.show_input)

    def init_tabs(self, results=None):
        if results:
            self.tab_layout.deleteLater()
            self.tab_layout = QTabWidget()
            self.base_layout.addWidget(self.tab_layout)
        for idx in range(4):
            tab = QWidget()
            tab_l = QVBoxLayout()
            tab.setLayout(tab_l)
            if results:
                tb = QTextBrowser()
                tb.setText(str(results[idx]))
                tab_l.addWidget(tb)
            else:
                tab_l.addWidget(QLabel("No hay resultados"))
            tab_name = "M_" + str(4 - idx) + str(3 - idx)
            self.tab_layout.addTab(tab, tab_name)

    def show_input(self):
        self.go_input_sig.emit()

    @pyqtSlot(tuple)
    def update_results(self, results: tuple):
        self.init_tabs(results)


class App(QMainWindow):
    results_sig = pyqtSignal(tuple)

    def __init__(self):
        super().__init__()
        self.title = 'Compress4D'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.widget_stacks = QStackedWidget()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.init_layout()
        self.show()

    def init_layout(self):
        base_widget = QWidget()
        # Widgets for stacks #
        matrix_input_widget = MatrixInputWidget()
        results_widget = ResultsWidget()

        # Widget stacking #
        self.widget_stacks.addWidget(matrix_input_widget)
        self.widget_stacks.addWidget(results_widget)

        # Layout setup #
        base_layout = QVBoxLayout()
        base_layout.addWidget(self.widget_stacks)
        base_widget.setLayout(base_layout)

        # Menubar actions #
        exit_action = QAction(QIcon("exit.png"), "Salir", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.setStatusTip("Salir de la aplicación")
        exit_action.triggered.connect(qApp.quit)

        # Menubar configuration #
        menubar = self.menuBar()
        file_menu = menubar.addMenu("&Archivo")
        file_menu.addAction(exit_action)

        # Signals connection #
        matrix_input_widget.wk_sig_done.connect(self.show_results)
        results_widget.go_input_sig.connect(self.show_input)
        self.results_sig.connect(results_widget.update_results)

        self.setCentralWidget(base_widget)

    @pyqtSlot(tuple)
    def show_results(self, results: tuple):
        self.results_sig.emit(results)
        self.widget_stacks.setCurrentIndex(1)

    @pyqtSlot()
    def show_input(self):
        self.widget_stacks.setCurrentIndex(0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
