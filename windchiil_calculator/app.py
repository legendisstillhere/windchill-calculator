import sys
from PyQt6.QtGui import * 
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QGridLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QWidget,
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Windchill Calculator")

        self.UICompomnent()

    def UICompomnent(self):
        self.container = QWidget()
        self.container_layout = QVBoxLayout()
        self.container.setLayout(self.container_layout)

        self.title = QLabel("Windchill Calculator")
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title.setFont(QFont("Helvetica", 15))
        self.container_layout.addWidget(self.title)

        self.setCentralWidget(self.container)

        self.windchill_grid = QGridLayout()
        self.container_layout.addLayout(self.windchill_grid)
        self.temp_label = QLabel("Temperature")
        self.wind_label = QLabel("Wind Speed")
        
        self.wind_spin = QSpinBox()
        
        self.wind_spin.setMaximum(100)
        self.wind_spin.setMinimum(0)
        
        self.temp_spin = QSpinBox()

        self.temp_spin.setMaximum(50)  
        self.temp_spin.setMinimum(-50)
        
        self.windchill_grid.addWidget(self.temp_label, 0, 0)
        self.windchill_grid.addWidget(self.wind_label, 0, 1)
        self.windchill_grid.addWidget(self.temp_spin, 1, 0)
        self.windchill_grid.addWidget(self.wind_spin, 1, 1)

        self.calculate_button = QPushButton("Calculate")
        self.container_layout.addWidget(self.calculate_button)

   

app = QApplication(sys.argv)
window = MainWindow()
window.show()

sys.exit(app.exec())

