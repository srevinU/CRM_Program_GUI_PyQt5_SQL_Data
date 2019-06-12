from PyQt5.QtWidgets import *
import sys
from App.A_Client import NewClient
from App.A_Supplier import NewSupplier
from App.A_Order import NewOrder
from App.E_Client import EmailClient
from App.E_Supplier import EmailSupplier
from App.D_Order import DeleteOrder


class Crm(QWidget):

    """MAIN WINDOW APPLICATION.

    APPLICATION TO MANAGE CLIENT, SUPPLIER, ORDERS, EMAILING CAMPAIGN WITH SQL FILE (DATA)

    OPTIONS BY TOPIC :

        1: CLIENT : ADD CLIENT / CLIENT EMAILING CAMPAIGN AUTOMATED FROM SQL CLIENT DATA
        2: SUPPLIER : ADD SUPPLIER / SUPPLIER EMAILING CAMPAIGN AUTOMATED FROM SQL SUPPLIER DATA
        3: ORDER : PLACE ORDER / DELETE ORDER FROM SQL ORDER DATA

    APPLICATION FILE COMPOSITION : 14 FILES, 7 FOR 7 WINDOWS, 1 FOR SQL FUNCTIONS, 6 SQL DATA FILES

        FILE App_main : MAIN WINDOW GIVING ACCESS TO ALL THE FEATURES
        FILE A_Client : TO ADD CLIENT AND REGISTER IT TO THE SQL DATA FILE "DATA_CLIENTS"
        FILE A_Order : TO ADD ORDER AND REGISTER IT TO THE SQL DATA FILE "DATA_ORDERS"
        FILE A_Supplier : TO ADD SUPPLIER AND REGISTER IT TO THE SQL FILE "DATA_SUPPLIER"
        FILE D_Order : TO DELETE ORDER FROM THE SQL DATA FILE "DATA_ORDERS" AND
                        ADD THE DELETE INFORMATION TO THE SQL DATA FILE "DATA_ORDER_DELETED"
        FILE E_Client : TO LAUNCH AN EMAILING CAMPAIGN FOR CLIENT AND
                        ADD THE CAMPAIGN TO THE SQL DATA FILE "DATA_E_MAILING"
        FILE E_Supplier : TO LAUNCH AN EMAILING CAMPAIGN FOR SUPPLIER AND
                        ADD THE CAMPAIGN TO THE SQL DATA FILE "DATA_E_MAILING"
        FILE SQLite_Database : ALL THE FUNCTIONS TO MANAGE THE DATA WITH THE SQL FILES
        6 SQL DATA FILES : 6 DIFFERENT SQL FILES TO SAVE DATA. 5 FOR EACH WINDOWS AND ONE MAIN FOR ALL THE ACTIONS
                            EXECUTED. FUNCTIONS AVAILABLE TO CREATE THESE FILES IN SQLite_Database.py (IMPORTANT).

    """

    def __init__(self, parent=None):
        super(Crm, self).__init__()

        """SET THE FIRST MAIN WINDOW"""

        self.setGeometry(50, 50, 400, 100)
        self.setWindowTitle("CRM TEST")

        self.grid = QGridLayout()
        self.grid.setSpacing(10)
        self.setLayout(self.grid)

        self.home()

    def home(self):

        """SET ALL THE WIDGETS OF THE MAIN WINDOW"""

        self.btn1 = QPushButton("New client", self)
        self.grid.addWidget(self.btn1, 1, 0)
        self.btn1.clicked.connect(self.btn1_on)

        self.btn2 = QPushButton("New supplier", self)
        self.grid.addWidget(self.btn2, 1, 1)
        self.btn2.clicked.connect(self.btn2_on)

        self.btn3 = QPushButton("Place an order", self)
        self.grid.addWidget(self.btn3, 1, 2)
        self.btn3.clicked.connect(self.btn3_on)

        self.btn4 = QPushButton("E-mailing client", self)
        self.grid.addWidget(self.btn4, 2, 0)
        self.btn4.clicked.connect(self.btn4_on)

        self.btn5 = QPushButton("E-mailing supplier", self)
        self.grid.addWidget(self.btn5, 2, 1)
        self.btn5.clicked.connect(self.btn5_on)

        self.btn6 = QPushButton("Del an order", self)
        self.grid.addWidget(self.btn6, 2, 2)
        self.btn6.clicked.connect(self.btn6_on)

        self.message_box = QTextEdit()
        self.message_box.setReadOnly(True)
        self.grid.addWidget(self.message_box, 3, 0, 5, 3)

        self.btn_q = QPushButton("Quit", self)
        self.grid.addWidget(self.btn_q, 10, 0, 10, 3)
        self.btn_q.clicked.connect(self.close_application)

        self.dialogs = list()

        self.show()

    def btn1_on(self):

        """GIVES ACCESS TO THE NewClient WINDOW"""

        dialog = NewClient(self)
        self.dialogs.append(dialog)
        dialog.show()

    def btn2_on(self):

        """GIVES ACCESS TO THE NewSupplier WINDOW"""

        dialog = NewSupplier(self)
        self.dialogs.append(dialog)
        dialog.show()

    def btn3_on(self):

        """GIVES ACCESS TO THE NewOrder WINDOW"""

        dialog = NewOrder(self)
        self.dialogs.append(dialog)
        dialog.show()

    def btn4_on(self):

        """GIVES ACCESS TO THE EmailClient WINDOW"""

        dialog = EmailClient(self)
        self.dialogs.append(dialog)
        dialog.show()

    def btn5_on(self):

        """GIVES ACCESS TO THE EmailSupplier WINDOW"""

        dialog = EmailSupplier(self)
        self.dialogs.append(dialog)
        dialog.show()

    def btn6_on(self):

        """GIVES ACCESS TO THE DeleteOrder WINDOW"""

        dialog = DeleteOrder(self)
        self.dialogs.append(dialog)
        dialog.show()

    def close_application(self):

        """CLOSE APPLICATION"""

        choice = QMessageBox.question(self, "Execute", "Do you want to quit the application?",
                                      QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

        if choice == QMessageBox.Yes:
            sys.exit(self)
        else:
            pass


if __name__ == "__main__":

    app = QApplication([])
    launch = Crm()
    app.exec_()

