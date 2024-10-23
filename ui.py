import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QLabel, QPushButton, QComboBox, QMessageBox

class InputCollectorApp(QWidget):
    def __init__(self):
        super().__init__()

        # Initialize the layout and UI components
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Input Collector')
        self.setGeometry(100, 100, 400, 300)

        self.layout = QVBoxLayout()

        # Create a combo box for selecting modes
        self.mode_combo_box = QComboBox()
        self.mode_combo_box.addItems(["Select Mode", "Mode 1", "Mode 2", "Mode 3"])
        self.mode_combo_box.currentIndexChanged.connect(self.on_mode_change)

        # Create input fields for different modes
        self.input_field_1 = QLineEdit()
        self.input_field_1.setPlaceholderText("Input for Mode 1")
        self.input_field_2 = QLineEdit()
        self.input_field_2.setPlaceholderText("Input for Mode 2")
        self.input_field_3 = QLineEdit()
        self.input_field_3.setPlaceholderText("Input for Mode 3")

        # Create a button to confirm the input
        self.confirm_button = QPushButton('Confirm Input')
        self.confirm_button.clicked.connect(self.on_confirm)

        # Add components to the layout
        self.layout.addWidget(self.mode_combo_box)
        self.layout.addWidget(self.input_field_1)
        self.layout.addWidget(self.input_field_2)
        self.layout.addWidget(self.input_field_3)
        self.layout.addWidget(self.confirm_button)

        # Initially hide all input fields
        self.input_field_1.hide()
        self.input_field_2.hide()
        self.input_field_3.hide()

        self.setLayout(self.layout)

    def on_mode_change(self):
        """Handle mode change to show/hide input fields."""
        selected_mode = self.mode_combo_box.currentText()

        # Hide all input fields initially
        self.input_field_1.hide()
        self.input_field_2.hide()
        self.input_field_3.hide()

        # Show the relevant input field based on the selected mode
        if selected_mode == "Mode 1":
            self.input_field_1.show()
        elif selected_mode == "Mode 2":
            self.input_field_2.show()
        elif selected_mode == "Mode 3":
            self.input_field_3.show()

    def on_confirm(self):
        """Handle the confirm button click."""
        selected_mode = self.mode_combo_box.currentText()
        if selected_mode == "Mode 1":
            input_text = self.input_field_1.text()
            message = f"Mode 1 Input: {input_text}"
        elif selected_mode == "Mode 2":
            input_text = self.input_field_2.text()
            message = f"Mode 2 Input: {input_text}"
        elif selected_mode == "Mode 3":
            input_text = self.input_field_3.text()
            message = f"Mode 3 Input: {input_text}"
        else:
            message = "Please select a mode and enter input."

        # Show the collected input in a message box
        QMessageBox.information(self, "Input Collected", message)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    input_collector = InputCollectorApp()
    input_collector.show()
    sys.exit(app.exec_())