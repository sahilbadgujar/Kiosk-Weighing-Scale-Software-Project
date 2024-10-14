import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QDate

class DateApp(QWidget):
    def __init__(self):
        super().__init__()

        # Set up the user interface
        self.initUI()

    def initUI(self):
        # Create a label to display the date
        self.date_label = QLabel(self)
        
        # Fetch the current date
        current_date = QDate.currentDate()
        
        # Display the current date in the label
        self.date_label.setText(current_date.toString())

        # Set up layout
        layout = QVBoxLayout()
        layout.addWidget(self.date_label)
        
        # Set the layout for the main window
        self.setLayout(layout)
        
        # Set the window title and size
        self.setWindowTitle('Current Date')
        self.setGeometry(100, 100, 200, 100)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DateApp()
    ex.show()
    sys.exit(app.exec_())
