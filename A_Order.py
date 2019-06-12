from PyQt5.QtWidgets import *
from App.SQLite_Database import add_order_data, nb_actions_data, add_actions_data
from datetime import datetime
import sqlite3


class NewOrder(QWidget):

    """THE NewOrder APPLICATION WINDOW.

       DISPLAY A WINDOW TO REGISTER ALL THE CLIENT INFORMATION AND SAVE IT IN THE SQL FILE data_orders AND
       IN THE MAIN SQL FILE FOR ALL THE ACTIONS EXECUTED

       REMARK : THE SQL FILE HAS TO BE CREATED BEFORE TO PROCESS, RUN THE FUNCTION FROM A DIFFERENT FILE IN THE FOLDER.
               YOU WILL FIND THE FUNCTION IN THE SQLite_Database.py.
       """

    def __init__(self, Crm):
        super(NewOrder, self).__init__()

        """SET THE NewOrder WINDOW AND Crm AS THE PARENT"""

        self.Crm = Crm

        self.setWindowTitle("ADD ORDER")

        self.grid = QGridLayout()

        self.setLayout(self.grid)

        self.home()

    def home(self):

        """SET ALL THE WIDGETS OF THE NewOrder WINDOW"""

        label_your_name = QLabel("Your name:", self)
        self.grid.addWidget(label_your_name, 0, 0)

        label_your_f_name = QLabel("First name:", self)
        self.grid.addWidget(label_your_f_name, 0, 1)
        self.box_your_f_name = QLineEdit(self)
        self.grid.addWidget(self.box_your_f_name, 0, 2)

        label_your_l_name = QLabel("Last name:", self)
        self.grid.addWidget(label_your_l_name, 1, 1)
        self.box_your_l_name = QLineEdit(self)
        self.grid.addWidget(self.box_your_l_name, 1, 2)

        label_client_name = QLabel("Client:", self)
        self.grid.addWidget(label_client_name, 2, 0)

        label_company_name = QLabel("Company:", self)
        self.grid.addWidget(label_company_name,2, 1)
        self.box_company_name = QLineEdit(self)
        self.grid.addWidget(self.box_company_name, 2, 2)

        label_client_f_name = QLabel("First name:", self)
        self.grid.addWidget(label_client_f_name, 3, 1)
        self.box_client_f_name = QLineEdit(self)
        self.grid.addWidget(self.box_client_f_name, 3, 2)

        label_client_l_name = QLabel("Last name:", self)
        self.grid.addWidget(label_client_l_name, 4, 1)
        self.box_client_l_name = QLineEdit(self)
        self.grid.addWidget(self.box_client_l_name, 4, 2)

        label_client_reference = QLabel("Reference n°:", self)
        self.grid.addWidget(label_client_reference, 5, 1)
        self.box_client_reference = QLineEdit(self)
        self.grid.addWidget(self.box_client_reference, 5, 2)

        label_order = QLabel("Order:", self)
        self.grid.addWidget(label_order, 6, 0)

        label_order_date = QLabel("Date:", self)
        self.grid.addWidget(label_order_date, 7, 1)
        self.box_order_date = QLineEdit(self)
        self.grid.addWidget(self.box_order_date, 7, 2)

        label_reference_product_1 = QLabel("Ref product(1):", self)
        self.grid.addWidget(label_reference_product_1, 8, 1)
        self.box_reference_product_1 = QLineEdit(self)
        self.grid.addWidget(self.box_reference_product_1, 8, 2)

        label_quantity_product_1 = QLabel("Quatity:", self)
        self.grid.addWidget(label_quantity_product_1, 8, 3)
        self.box_quantity_product_1 = QLineEdit(self)
        self.grid.addWidget(self.box_quantity_product_1, 8, 4)

        label_reference_product_2 = QLabel("Ref product(2):", self)
        self.grid.addWidget(label_reference_product_2, 9, 1)
        self.box_reference_product_2 = QLineEdit(self)
        self.grid.addWidget(self.box_reference_product_2, 9, 2)

        label_quantity_product_2 = QLabel("Quatity:", self)
        self.grid.addWidget(label_quantity_product_2, 9, 3)
        self.box_quantity_product_2 = QLineEdit(self)
        self.grid.addWidget(self.box_quantity_product_2, 9, 4)

        label_reference_product_3 = QLabel("Ref product(3):", self)
        self.grid.addWidget(label_reference_product_3, 10, 1)
        self.box_reference_product_3 = QLineEdit(self)
        self.grid.addWidget(self.box_reference_product_3, 10, 2)

        label_quantity_product_3 = QLabel("Quatity:", self)
        self.grid.addWidget(label_quantity_product_3, 10, 3)
        self.box_quantity_product_3 = QLineEdit(self)
        self.grid.addWidget(self.box_quantity_product_3, 10, 4)

        label_reference_product_4 = QLabel("Ref product(4):", self)
        self.grid.addWidget(label_reference_product_4, 11, 1)
        self.box_reference_product_4 = QLineEdit(self)
        self.grid.addWidget(self.box_reference_product_4, 11, 2)

        label_quantity_product_4 = QLabel("Quatity:", self)
        self.grid.addWidget(label_quantity_product_4, 11, 3)
        self.box_quantity_product_4 = QLineEdit(self)
        self.grid.addWidget(self.box_quantity_product_4, 11, 4)

        label_reference_product_5 = QLabel("Ref product(5):", self)
        self.grid.addWidget(label_reference_product_5, 12, 1)
        self.box_reference_product_5 = QLineEdit(self)
        self.grid.addWidget(self.box_reference_product_5, 12, 2)

        label_quantity_product_5 = QLabel("Quatity:", self)
        self.grid.addWidget(label_quantity_product_5, 12, 3)
        self.box_quantity_product_5 = QLineEdit(self)
        self.grid.addWidget(self.box_quantity_product_5, 12, 4)

        self.btn_add_order = QPushButton("Place Order", self)
        self.grid.addWidget(self.btn_add_order, 13, 0, 13, 5)
        self.btn_add_order.clicked.connect(self.btn_place_order_on)

    def reference_order_creation(self):

        """CREATE A REFERENCE NUMBER EVERY TIME AN ORDER IS CREATED"""

        date = datetime.strftime(datetime.today(), "%d, %m, %Y")
        y = date[-2:]
        m = date[-8:-6]

        order_nb = 0
        conn = sqlite3.connect("data_orders.db")
        c = conn.cursor()

        with conn:

            for i in c.execute("SELECT * from data_orders"):
                order_nb += 1

        self.ref_order = str(order_nb) + m + y

        with conn:

            x = c.execute("SELECT :ref_order FROM data_orders WHERE ref_order = :ref_order", {'ref_order': self.ref_order})

            for i in x:
                if i[0] == self.ref_order:
                    self.ref_order += "*"
                else:
                    pass

    def btn_place_order_on(self):

        """GET ALL THE DATA AND IMPLEMENT IT IN THE SQL FILE"""

        date = datetime.today()

        self.reference_order_creation()

        add_order_data(self.ref_order, self.box_your_f_name.text().upper(), self.box_your_l_name.text().upper(),
            self.box_company_name.text().upper(), self.box_client_f_name.text().upper(),
            self.box_client_l_name.text().upper(), self.box_client_reference.text().upper(),
            self.box_order_date.text().upper(), self.box_reference_product_1.text().upper(),
            self.box_quantity_product_1.text().upper(), self.box_reference_product_2.text().upper(),
            self.box_quantity_product_2.text().upper(), self.box_reference_product_3.text().upper(),
            self.box_quantity_product_3.text().upper(), self.box_reference_product_4.text().upper(),
            self.box_quantity_product_4.text().upper(), self.box_reference_product_5.text().upper(),
            self.box_quantity_product_5.text().upper())

        self.Crm.message_box.append(f"The order n°{self.ref_order} "
                                    f"has been placed the {date}")

        nb = nb_actions_data()

        add_actions_data(nb, "ORDER ADDED " + self.ref_order, date, self.box_your_f_name.text().upper(), self.box_your_l_name.text().upper())



