from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
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

        # Class variables
        self.images = {}
        self.scale_factor = 0.0

        self.init_ui()

    def init_ui(self):
        """Initiate UI"""

        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setLayoutDirection(Qt.LeftToRight)
        self.setStyleSheet(getStyles("main-window"))
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.centralwidget.setLayoutDirection(Qt.LeftToRight)
        self.centralwidget.setAutoFillBackground(True)
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.image_side_layout = QVBoxLayout()
        self.image_side_layout.setSpacing(6)
        self.image_side_layout.setObjectName(u"image_side_layout")
        self.image_side_layout.setSizeConstraint(QLayout.SetFixedSize)
        self.file_selection_layout = QHBoxLayout()
        self.file_selection_layout.setObjectName(u"file_selection_layout")
        self.file_selection_layout.setContentsMargins(-1, -1, -1, 50)
        self.file_selection_label = QLabel(self.centralwidget)
        self.file_selection_label.setObjectName(u"file_selection_label")
        sizePolicy.setHeightForWidth(
            self.file_selection_label.sizePolicy().hasHeightForWidth())
        self.file_selection_label.setSizePolicy(sizePolicy)

        self.file_selection_layout.addWidget(self.file_selection_label)

        self.line_edit = QLineEdit(self.centralwidget)
        self.line_edit.setObjectName(u"line-edit")

        self.file_selection_layout.addWidget(self.line_edit)

        self.explorer_open = QPushButton(self.centralwidget)
        self.explorer_open.setObjectName(u"explorer_open")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(
            self.explorer_open.sizePolicy().hasHeightForWidth())
        self.explorer_open.setSizePolicy(sizePolicy2)
        self.explorer_open.setStyleSheet("push-btn")

        self.explorer_open.setAutoDefault(False)
        self.explorer_open.setFlat(True)

        self.file_selection_layout.addWidget(self.explorer_open)

        self.image_side_layout.addLayout(self.file_selection_layout)

        self.image_list_descriptor = QLabel(self.centralwidget)
        self.image_list_descriptor.setObjectName(u"image_list_descriptor")
        sizePolicy2.setHeightForWidth(
            self.image_list_descriptor.sizePolicy().hasHeightForWidth())
        self.image_list_descriptor.setSizePolicy(sizePolicy2)

        self.image_side_layout.addWidget(self.image_list_descriptor)

        self.image_list = QListWidget(self.centralwidget)
        self.image_list.setObjectName(u"image_list")

        self.image_side_layout.addWidget(self.image_list)

        self.horizontalLayout.addLayout(self.image_side_layout)

        self.vertical_line = QFrame(self.centralwidget)
        self.vertical_line.setObjectName(u"vertical_line")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(
            self.vertical_line.sizePolicy().hasHeightForWidth())
        self.vertical_line.setSizePolicy(sizePolicy3)
        self.vertical_line.setLayoutDirection(Qt.LeftToRight)
        self.vertical_line.setStyleSheet(getStyles("v-line"))
        self.vertical_line.setFrameShape(QFrame.VLine)
        self.vertical_line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.vertical_line)

        self.image_placeholder_label = QLabel(self.centralwidget)
        self.image_placeholder_label.setObjectName(u"image_placeholder_label")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(
            self.image_placeholder_label.sizePolicy().hasHeightForWidth())
        self.image_placeholder_label.setSizePolicy(sizePolicy4)

        self.horizontalLayout.addWidget(self.image_placeholder_label)

        self.image_label = QLabel(self.centralwidget)
        self.image_label.setObjectName(u"image_label")
        sizePolicy1.setHeightForWidth(
            self.image_label.sizePolicy().hasHeightForWidth())
        self.image_label.setSizePolicy(sizePolicy1)
        self.image_label.setStyleSheet(u"text-align: center;")

        self.horizontalLayout.addWidget(self.image_label)

        self.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(self)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(0, 0, 800, 21)
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(
            self.menubar.sizePolicy().hasHeightForWidth())
        self.menubar.setSizePolicy(sizePolicy5)
        self.menu_about_PyQt5 = QMenu(self.menubar)
        self.menu_about_PyQt5.setObjectName(u"menu_about_PyQt5")
        self.menu_about = QMenu(self.menubar)
        self.menu_about.setObjectName(u"menu_about")
        self.setMenuBar(self.menubar)

        self.menubar.addAction(self.menu_about.menuAction())
        self.menubar.addAction(self.menu_about_PyQt5.menuAction())

        self.init_text()
        self.init_connections()

    def init_text(self):
        """Init the text for each widget"""

        _translate = QtCore.QCoreApplication.translate

        self.setWindowTitle(_translate("self", "ImageSee"))

        self.file_selection_label.setText(
            _translate("MainWindow", "Input the path: "))

        self.explorer_open.setToolTip(_translate(
            "MainWindow", "Click to find in Explorer. If you manually inputted the path in, it will open that."))

        self.explorer_open.setText(_translate(
            "MainWindow", "Open in Explorer"))

        self.image_list_descriptor.setText(_translate(
            "MainWindow", "Images found will go here."))

        self.image_placeholder_label.setText(
            _translate("MainWindow", "Image goes here..."))

        self.menu_about.setTitle(_translate("MainWindow", "About"))

        self.menu_about_PyQt5.setTitle(_translate("MainWindow", "About PyQt5"))

    def init_connections(self):
        """Init the connections for each widget"""

        # self.menuAbout.mousePressEvent(func)
        # self.menuAbout_PyQt5.mousePressEvent(func)
        self.explorer_open.clicked.connect(self.on_explorer_clicked)
        self.image_list.itemClicked.connect(self.on_image_list_item_clicked)

    # Event triggered functions

    def on_explorer_clicked(self):
        """Executes when the explorer_open buttons is clicked."""
        self.image_label.setVisible(False)
        self.image_placeholder_label.setVisible(True)
        self.image_list.clear()

        if not self.line_edit.text() == "":
            path = self.line_edit.text().lower()

            # print(f"path: {path}")

            try:
                for file in os.listdir(path):
                    # print(f"unfiltered file: {file}")

                    if file.endswith((".png", ".jpeg", ".jpg", ".gif")):
                        # print(f"filtered file: {file}")
                        # print(f"filtered file path: {os.path.join(path, file)}")

                        self.images[file] = os.path.join(path, file)

                        self.image_list.addItem(file)
            except FileNotFoundError:
                    msg_box = QtWidgets.QMessageBox.about(self, "File not found", "No file was found.")
                    msg_box.setIcon(QMessageBox.Critical)
                    msg_box.setStandardButtons(QMessageBox.Ok)

    def on_image_list_item_clicked(self):
        """Executes when you click a list item in self.image_list"""
        self.image_label.setVisible(True)

        path_to_image = self.images[str(self.image_list.currentItem().text())]

        pixmap = QtGui.QPixmap(path_to_image)

        scaled_pixmap = pixmap.scaled(391, 491, QtCore.Qt.KeepAspectRatio)

        self.image_placeholder_label.setVisible(False)
        self.image_label.setPixmap(scaled_pixmap)
        self.image_label.resize(scaled_pixmap.width(), scaled_pixmap.height())


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
