import sys
import random

from PySide6.QtGui import QPainter
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QGridLayout, QLabel, QPushButton, QLineEdit
)
from PySide6.QtCore import QTimer, Qt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class TradingBotUI(QWidget):
    def __init__(self) -> None:
        super().__init__()

        # Main Layout
        grid = QGridLayout()
        self.setLayout(grid)

        # Reat-time MatplotLib Graph (Top-Left)
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.ax = self.figure.add_subplot(111)
        grid.addWidget(self.canvas, 0, 0)

        # Portfolio - To display portfolio details (Bottom left)
        self.portfolio_label = QLabel("Portfolio")
        grid.addWidget(self.portfolio_label, 1, 0)

        # Bot parameters - input fields and buttons (Top right)
        self.params_layout = QVBoxLayout()
        self.param_label = QLabel("Bot Parameters")
        self.param1_input = QLineEdit("Parameter 1")
        self.param2_input = QLineEdit("Parameter 2")
        self.apply_button = QPushButton("Apply")

        self.params_layout.addWidget(self.param_label)
        self.params_layout.addWidget(self.param1_input)
        self.params_layout.addWidget(self.param2_input)
        self.params_layout.addWidget(self.apply_button)
        grid.addLayout(self.params_layout, 0, 1)

        # Bot performance - performance stats (Bottom right)
        self.performance_label = QLabel("Bot Performance")
        grid.addWidget(self.performance_label, 1, 1)

        # Timer for updating the matplotlib plot in real-time
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_plot)
        self.timer.start(1000)  # Update every second
        self.data = []

    def update_plot(self):
        # Simulate live data
        self.data.append(random.randint(0, 10))
        if len(self.data) > 20:
            self.data.pop(0)

        # Clear the axis and plot new data
        self.ax.clear()
        self.ax.plot(self.data, label="Live Data")
        self.ax.legend()

        # Refresh the canvas
        self.canvas.draw()

    @staticmethod
    def initialize_ui() -> tuple[QApplication, 'TradingBotUI']:
        """
        Returns app, window
        """
        app = QApplication(sys.argv)
        window = TradingBotUI()
        return app, window
    
    @staticmethod
    def start_event_loop(app, window) -> None:
        window.show()
        sys.exit(app.exec())

# Main execution
if __name__ == "__main__":
    app, window = TradingBotUI.initialize_ui()
    window.start_event_loop(app, window)
    