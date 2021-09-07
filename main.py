from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication
import os
from styles import getStyles


class Main_UI(QMainWindow):
    """The main UI for the app"""

    def __init__(self):
        """Initiate the Window"""

        super(Main_UI, self).__init__()

        # Window setup
        self.setGeometry(100, 100, 800, 520)
        self.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.setStyleSheet(getStyles("main-window"))

        self.init_ui()

    def init_ui(self):
        """Initiate UI"""

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setObjectName("centralwidget")

        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(390, 0, 1, 520))
        self.line.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.line.setStyleSheet(getStyles("v-line"))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.image_label = QtWidgets.QLabel(self.centralwidget)
        self.image_label.setGeometry(QtCore.QRect(400, 0, 391, 491))
        self.image_label.setText("")
        self.image_label.setObjectName("image_label")

        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 341, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")

        self.file_selection_layout = QtWidgets.QHBoxLayout(
            self.horizontalLayoutWidget)
        self.file_selection_layout.setContentsMargins(0, 0, 0, 0)
        self.file_selection_layout.setObjectName("file_selection_layout")

        self.file_selection_label = QtWidgets.QLabel(
            self.horizontalLayoutWidget)
        self.file_selection_label.setObjectName("file_selection_label")
        self.file_selection_layout.addWidget(self.file_selection_label)

        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")

        self.file_selection_layout.addWidget(self.lineEdit)
        self.explorer_open = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.explorer_open.setStyleSheet(getStyles("push-btn"))
        self.explorer_open.setAutoDefault(False)
        self.explorer_open.setDefault(False)
        self.explorer_open.setFlat(True)
        self.explorer_open.setObjectName("explorer_open")

        self.file_selection_layout.addWidget(self.explorer_open)
        self.image_list = QtWidgets.QListView(self.centralwidget)
        self.image_list.setGeometry(QtCore.QRect(20, 100, 341, 371))
        self.image_list.setObjectName("image_list")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 80, 131, 16))
        self.label.setObjectName("label")

        self.image_placeholder_label = QtWidgets.QLabel(self.centralwidget)
        self.image_placeholder_label.setGeometry(
            QtCore.QRect(420, 230, 391, 78))
        self.image_placeholder_label.setObjectName("image_placeholder_label")
        self.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")

        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")

        self.menuAbout_PyQt5 = QtWidgets.QMenu(self.menubar)
        self.menuAbout_PyQt5.setObjectName("menuAbout_PyQt5")

        self.setMenuBar(self.menubar)
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menubar.addAction(self.menuAbout_PyQt5.menuAction())

        self.init_text()
        self.init_connections()

    def init_text(self):
        """Init the text for each widget"""

        _translate = QtCore.QCoreApplication.translate

        self.setWindowTitle(_translate("MainWindow", "ImageSee"))

        self.file_selection_label.setText(
            _translate("MainWindow", "Input the path: "))

        self.explorer_open.setToolTip(_translate(
            "MainWindow", "Click to find in Explorer. If you manually inputted the path in, it will open that."))

        self.explorer_open.setText(_translate(
            "MainWindow", "Open in Explorer"))

        self.label.setText(_translate(
            "MainWindow", "Images found will go here."))

        self.image_placeholder_label.setText(
            _translate("MainWindow", "Image goes here..."))

        self.menuAbout.setTitle(_translate("MainWindow", "About"))

        self.menuAbout_PyQt5.setTitle(_translate("MainWindow", "About PyQt5"))

    def init_connections(self):
        """Init the connections for each widget"""

        self.explorer_open.clicked.connect(self.on_explorer_clicked)

    # Event triggered functions

    def on_explorer_clicked(self):
        """Executes when the explorer_open buttons is clicked."""

        if not self.lineEdit.text() == "":
            path = self.lineEdit.text().lower()

            for files in os.walk(path.lower()):
                for file in files:
                    if ( 
                    file.endswith(".png") 
                    or file.endswith(".bmp") 
                    or file.endswith(".gif") 
                    or file.endswith(".jpg")
                    or file.endswith(".jpeg")
                    ):
                        print(file)



def main():
    """Setup and run/show the UI"""

    from sys import argv, exit

    app = QApplication(argv)
    window = Main_UI()

    # Run it, and exit gracefully when closed
    window.show()
    exit(app.exec_())


if __name__ == "__main__":
    main()
