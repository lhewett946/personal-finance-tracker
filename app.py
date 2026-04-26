import sys
from PySide6.QtWidgets import QApplication
from ui import Windows

# Create the application instance
app = QApplication(sys.argv)

# Create a main window
window = Windows.MainWindow()
window.show()

# Run the application's event loop
sys.exit(app.exec())