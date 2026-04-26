"""Application entry point for the personal finance tracker."""

import sys
from PySide6.QtWidgets import QApplication
from ui import windows

# Create the application instance
app = QApplication(sys.argv)

# Create a main window
window = windows.MainWindow()
window.show()

# Run the application's event loop
sys.exit(app.exec())
