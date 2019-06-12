from PyQt5.QtWidgets import *
from datetime import datetime
from App.SQLite_Database import delete_order_data, add_delete_order_data,\
    nb_actions_data, add_actions_data, check_order_data_before_del


class DeleteOrder(QWidget):

    """THE DeleteOrder APPLICATION WINDOW.

        DISPLAY A WINDOW TO DELETE AN ORDER REGARDING INFORMATION FILLED OUT AND SAVE IT IN THE SQL FILE
        delete_order_data AND IN THE MAIN SQL FILE FOR ALL THE ACTIONS EXECUTED

        REMARK : THE SQL FILE HAS TO BE CREATED BEFORE TO PROCESS, RUN THE FUNCTION FROM A DIFFERENT FILE IN THE FOLDER.
                YOU WILL FIND THE FUNCTION IN THE SQLite_Database.py.
        """

    def __init__(self, Crm):
        super(DeleteOrder, self).__init__()

        """SET THE DeleteOrder WINDOW AND Crm AS THE PARENT"""

        self.Crm = Crm

        self.setWindowTitle("DEL ORDER")

        self.grid = QGridLayout()
        self.setLayout(self.grid)

        self.home()

    def home(self):

        """SET ALL THE WIDGETS OF THE DeleteOrder WINDOW"""

        label_name = QLabel("Your name:")
        self.grid.addWidget(label_name, 0, 0)

        label_f_name = QLabel("First name:")
        self.grid.addWidget(label_f_name, 0, 1)
        self.box_f_name = QLineEdit(self)
        self.grid.addWidget(self.box_f_name, 0, 2)

        label_l_name = QLabel("Last name:")
        self.grid.addWidget(label_l_name, 1, 1)
        self.box_l_name = QLineEdit(self)
        self.grid.addWidget(self.box_l_name, 1, 2)

        label_ref_ord = QLabel("Order ref n°:")
        self.grid.addWidget(label_ref_ord, 2, 0)
        self.box_ref_ord = QLineEdit(self)
        self.grid.addWidget(self.box_ref_ord, 2, 1)

        label_reason = QLabel("Reason:")
        self.grid.addWidget(label_reason, 3, 0)
        self.box_reason = QLineEdit(self)
        self.grid.addWidget(self.box_reason, 3, 1)

        self.delete_message_box = QTextEdit(self)
        self.delete_message_box.setReadOnly(True)
        self.grid.addWidget(self.delete_message_box, 4, 0, 4, 3)

        self.delete = QPushButton("Delete", self)
        self.grid.addWidget(self.delete, 10, 0, 10, 3)
        self.delete.clicked.connect(self.btn_delete_on)

    def btn_delete_on(self):

        """DELETE THE ORDER, GET ALL THE DATA AND IMPLEMENT IT IN THE SQL FILE"""

        nb = nb_actions_data()
        date = str(datetime.today())
        choice = QMessageBox.question(self, "Execute",  "Do you confirm the delete ?",
                                      QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

        if choice == QMessageBox.Yes and check_order_data_before_del(self.box_ref_ord.text()) is True:

            delete_order_data(self.box_ref_ord.text())

            add_delete_order_data(self.box_ref_ord.text(), self.box_reason.text().upper(),
                                  self.box_f_name.text().upper(), self.box_l_name.text().upper(), date)

            self.delete_message_box.append(f"The order n°{self.box_ref_ord.text()} has been deleted...")

            self.Crm.message_box.append(f"The order n°{self.box_ref_ord.text().upper()} has been deleted by"
                                        f" {self.box_f_name.text().upper()} {self.box_l_name.text().upper()} the "
                                        f"{date}")

            add_actions_data(nb, "ORDER deleted " + str(self.box_ref_ord.text().upper()), date,
                             self.box_f_name.text().upper(), self.box_l_name.text().upper())

        elif choice == QMessageBox.Yes and check_order_data_before_del(self.box_ref_ord.text()) is False:

            print(f"The order {self.box_ref_ord.text()} doesn't match with our data.")

            self.delete_message_box.append(f"The order n°{self.box_ref_ord.text()} doesn't match with the record...")

        else:
            pass
