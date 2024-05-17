import sys
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QGridLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QSpinBox,
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
        self.temp_label = QLabel("Temperature (°F)")
        self.wind_label = QLabel("Wind Speed (mph)")
        
        self.wind_spin = QSpinBox()
        self.wind_spin.setMaximum(100)
        self.wind_spin.setMinimum(3)
        
        self.temp_spin = QSpinBox()
        self.temp_spin.setMaximum(50)  
        self.temp_spin.setMinimum(-50)  
        
        self.windchill_grid.addWidget(self.temp_label, 0, 0)
        self.windchill_grid.addWidget(self.wind_label, 0, 1)
        self.windchill_grid.addWidget(self.temp_spin, 1, 0)
        self.windchill_grid.addWidget(self.wind_spin, 1, 1)

        self.calculate_button = QPushButton("Calculate")
        self.calculate_button.clicked.connect(self.calculate_windchill)
        self.container_layout.addWidget(self.calculate_button)

        # Label to display the result
        self.result_label = QLabel()
        self.container_layout.addWidget(self.result_label)

    def calculate_windchill(self):
        temperature = self.temp_spin.value()
        wind_speed = self.wind_spin.value()

        windchill = 35.74 + 0.6215 * temperature - 35.75 * wind_speed ** 0.16 + 0.4275 * temperature * wind_speed ** 0.16

        self.result_label.setText(f"Windchill: {windchill:.2f} °F")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()