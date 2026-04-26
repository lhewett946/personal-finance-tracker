"""Window implementations for the personal finance tracker UI."""
from PySide6.QtWidgets import QMainWindow

class MainWindow(QMainWindow):
   """Main application window."""

   def __init__(self):
      super().__init__()
      self.setup_ui()

   def setup_ui(self):
      """Set up the main window UI"""
      self.setWindowTitle("Personal Finance Tracker")
